import math
from tf.transformations import quaternion_from_euler, euler_from_quaternion

ANGLE_TOLERANCE = (30) * (math.pi/180) # camera FOV is 72, so we divide that by 2 and reduce it a bit for safety
DISTANCE_TOLERANCE = 1.0

def bound_angle(angle):
    while angle > math.pi:
        angle -= 2.0 * math.pi

    while angle < -math.pi:
        angle += 2.0 * math.pi

    return angle

def get_point_aimed(path, main_pose, follower_pose, max_dist, min_dist):
    closest_angle = 10000000000
    closest_pose = None
    

    for pose in path:
        point = pose.position
        main_point = main_pose.position
        follower_point = follower_pose.position
        this_dist = math.hypot(main_point.x - point.x, main_point.y - point.y)

        if this_dist > min_dist and this_dist > max_dist:
            midpt_heading = angle_to_midpoint(pose, main_point, follower_point)
            if midpt_heading != -503 and midpt_heading != None:
                print(midpt_heading)
                midpt_heading += math.pi
                midpt_heading = bound_angle(midpt_heading)
                
                quat = quaternion_from_euler(0, 0, midpt_heading)
                pose.orientation.x = quat[0]
                pose.orientation.y = quat[1]
                pose.orientation.z = quat[2]
                pose.orientation.w = quat[3]

                return pose

    if max_dist / min_dist < 2.0:
        print("lookup failed, trying 10% more")
        return get_point_aimed(path, main_pose, follower_pose, max_dist * 1.10, min_dist)

def angle_to_midpoint(pose, main_point, follower_point):
    point = pose.position

    midpoint = [(main_point.x + follower_point.x)/2, (main_point.y + follower_point.y)/2]    
    
    disp_from_follower = math.atan((point.y - follower_point.y)/(point.x - follower_point.x))
    disp_from_main = math.atan((point.y - main_point.y)/(point.x - main_point.x))

    if abs(disp_from_follower) < ANGLE_TOLERANCE and abs(disp_from_main) < ANGLE_TOLERANCE:
        # orientation_q = pose.orientation
        # orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
        # (roll, pitch, yaw) = euler_from_quaternion(orientation_list) 
        return math.atan2(point.y - midpoint[1], point.x - midpoint[0])
    return -503
 

def fit_in_fov(pose, main_point, follower_point):
    point = pose.position
    orientation_q = pose.orientation
    orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
    (roll, pitch, yaw) = euler_from_quaternion(orientation_list)

    delta_follower = [point.x - follower_point.x, point.y - follower_point.y]
    delta_main = [point.x - main_point.x, point.y - main_point.x]

    if (delta_follower[0] * delta_follower[0]) + (delta_follower[1] * delta_follower[1]) < (DISTANCE_TOLERANCE * DISTANCE_TOLERANCE):
        angle_to_follower = math.atan2(delta_follower[1], delta_follower[0])
        follower_angle_diff = abs(yaw - angle_to_follower)

        angle_to_main = math.atan2(delta_main[1], delta_main[0])
        main_angle_diff = abs(yaw - angle_to_main)

        return follower_angle_diff < ANGLE_TOLERANCE and main_angle_diff < ANGLE_TOLERANCE
    return False

    