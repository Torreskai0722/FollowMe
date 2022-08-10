#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/nvidia/projects/rosproject/src/navigation/base_local_planner"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/nvidia/projects/rosproject/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/nvidia/projects/rosproject/install/lib/python2.7/dist-packages:/home/nvidia/projects/rosproject/build/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/nvidia/projects/rosproject/build" \
    "/usr/bin/python2" \
    "/home/nvidia/projects/rosproject/src/navigation/base_local_planner/setup.py" \
     \
    build --build-base "/home/nvidia/projects/rosproject/build/navigation/base_local_planner" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/nvidia/projects/rosproject/install" --install-scripts="/home/nvidia/projects/rosproject/install/bin"
