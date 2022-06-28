## *********************************************************
##
## File autogenerated for the stereo_image_proc package
## by the dynamic_reconfigure package.
## Please do not edit.
##
## ********************************************************/

from dynamic_reconfigure.encoding import extract_params

inf = float('inf')

config_description = {'upper': 'DEFAULT', 'lower': 'groups', 'srcline': 246, 'name': 'Default', 'parent': 0, 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'cstate': 'true', 'parentname': 'Default', 'class': 'DEFAULT', 'field': 'default', 'state': True, 'parentclass': '', 'groups': [], 'parameters': [{'srcline': 291, 'description': 'stereo algorithm', 'max': 1, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'stereo_algorithm', 'edit_method': "{'enum_description': 'stereo algorithm', 'enum': [{'srcline': 11, 'description': 'Block Matching', 'srcfile': '/home/nvidia/projects/rosproject/src/image_pipeline/stereo_image_proc/cfg/Disparity.cfg', 'cconsttype': 'const int', 'value': 0, 'ctype': 'int', 'type': 'int', 'name': 'StereoBM'}, {'srcline': 12, 'description': 'SemiGlobal Block Matching', 'srcfile': '/home/nvidia/projects/rosproject/src/image_pipeline/stereo_image_proc/cfg/Disparity.cfg', 'cconsttype': 'const int', 'value': 1, 'ctype': 'int', 'type': 'int', 'name': 'StereoSGBM'}]}", 'default': 0, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 291, 'description': 'Normalization window size, pixels', 'max': 255, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'prefilter_size', 'edit_method': '', 'default': 9, 'level': 0, 'min': 5, 'type': 'int'}, {'srcline': 291, 'description': 'Bound on normalized pixel values', 'max': 63, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'prefilter_cap', 'edit_method': '', 'default': 31, 'level': 0, 'min': 1, 'type': 'int'}, {'srcline': 291, 'description': 'SAD correlation window width, pixels', 'max': 255, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'correlation_window_size', 'edit_method': '', 'default': 15, 'level': 0, 'min': 5, 'type': 'int'}, {'srcline': 291, 'description': 'Disparity to begin search at, pixels (may be negative)', 'max': 2048, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'min_disparity', 'edit_method': '', 'default': 0, 'level': 0, 'min': -2048, 'type': 'int'}, {'srcline': 291, 'description': 'Number of disparities to search, pixels', 'max': 4096, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'disparity_range', 'edit_method': '', 'default': 64, 'level': 0, 'min': 32, 'type': 'int'}, {'srcline': 291, 'description': 'Filter out if best match does not sufficiently exceed the next-best match', 'max': 100.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'uniqueness_ratio', 'edit_method': '', 'default': 15.0, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 291, 'description': 'Filter out if SAD window response does not exceed texture threshold', 'max': 10000, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'texture_threshold', 'edit_method': '', 'default': 10, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 291, 'description': 'Reject regions smaller than this size, pixels', 'max': 1000, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'speckle_size', 'edit_method': '', 'default': 100, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 291, 'description': 'Max allowed difference between detected disparities', 'max': 31, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'speckle_range', 'edit_method': '', 'default': 4, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 291, 'description': 'Run the full variant of the algorithm, only available in SGBM', 'max': True, 'cconsttype': 'const bool', 'ctype': 'bool', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'fullDP', 'edit_method': '', 'default': False, 'level': 0, 'min': False, 'type': 'bool'}, {'srcline': 291, 'description': 'The first parameter controlling the disparity smoothness, only available in SGBM', 'max': 4000.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'P1', 'edit_method': '', 'default': 200.0, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 291, 'description': 'The second parameter controlling the disparity smoothness., only available in SGBM', 'max': 4000.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'P2', 'edit_method': '', 'default': 400.0, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 291, 'description': 'Maximum allowed difference (in integer pixel units) in the left-right disparity check, only available in SGBM', 'max': 128, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'disp12MaxDiff', 'edit_method': '', 'default': 0, 'level': 0, 'min': 0, 'type': 'int'}], 'type': '', 'id': 0}

min = {}
max = {}
defaults = {}
level = {}
type = {}
all_level = 0

#def extract_params(config):
#    params = []
#    params.extend(config['parameters'])
#    for group in config['groups']:
#        params.extend(extract_params(group))
#    return params

for param in extract_params(config_description):
    min[param['name']] = param['min']
    max[param['name']] = param['max']
    defaults[param['name']] = param['default']
    level[param['name']] = param['level']
    type[param['name']] = param['type']
    all_level = all_level | param['level']

Disparity_StereoBM = 0
Disparity_StereoSGBM = 1
