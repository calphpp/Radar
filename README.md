# Radar
Pi Zero Ultrasonic Radar 
This project is uses a Pi Zero, acting as a server and drive for 5 ultrasonic sensors, measuring distance.

Using the Flask webserver - install the package using PIP3:

sudo pip3 install flask

run the server using python3:

sudo python3 radarServer.py

Counter-clockwise each sensor/sector is numbered 0-4.

To make a range measurement call:

http://192.168.0.197/?sector=0 sector is 0 thru 4.
