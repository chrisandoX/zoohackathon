# zoohackathon
zoohackathon at Geneve 2019

# Simulation

We have used [Robot Operating System](https://www.ros.org/) to create the LiDAR simulation environment. For anyone not experienced with ROS trying to run the simulation it's advised to follow [ROS installation tutorial](http://wiki.ros.org/kinetic/Installation) and [ROS Package Building Tutorials](http://wiki.ros.org/ROS/Tutorials/BuildingPackages). We have tested this setup on computers running Ubuntu 16.04 and 18.04 running ROS Kinetic and ROS Melodic respectively.

After building the package we have launched the 'gazebo_example launch_example.launch`. Then we manually sent a velocity request by publishing to "/cmd_vel" topic. We had visualised the data in rviz.

# Mapbox

All the files we had used to create a MapBox based WebApp were placed in ui_example directory with an entry point being the 'slider.html' file. We removed the access tokens from the html file, therefore if anyone wanted to reproduce our result he or she will need to generate a MapBox token for their account. In case of questions feel free to create an issue in the project repository.
