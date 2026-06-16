FROM docker.io/osrf/ros:lyrical-desktop

COPY ./src /tmp/workspace/
RUN bash -c "source /opt/ros/lyrical/setup.bash && \
    cd /tmp/workspace/ && \
    colcon build --install-base=/opt/ros/lyrical/workshop \
      --cmake-args -DCMAKE_BUILD_TYPE=Release && \
    rm -rf /tmp/workspace"
