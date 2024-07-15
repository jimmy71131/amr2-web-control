# Web Controller for Devices (Android, iOS, Computer) with ROS Integration

This project provides a simple web-based controller for devices like Android, iOS, and computers to communicate with ROS. The web interface sends linear and angular velocity commands to the `/cmd_vel` topic. Follow the steps below to set up the server and test the functionality.

## Step 1: Install Apache Web Server

1. Update package lists and install Apache:
   ```sh
   sudo apt update && sudo apt install apache2
   
2. Allow OpenSSH and Apache through the firewall:
   ```sh
   sudo ufw allow OpenSSH
   sudo ufw allow in "Apache Full"
   sudo ufw enable
   ```
3. Check the status of Apache service:
   ```sh
   sudo service apache2 status
   ```
## Step 2: Deploy the HTML File

1. Navigate to the Apache web directory:
   ```sh
   cd /var/www/html
   ```
2. Replace the existing HTML file with your web controller HTML file.

3. Ensure the HTML file is set up correctly. You can find a guide and an example HTML file here.

## Testing

To verify that the web controller is functioning correctly, use the following ROS command to echo messages from the /cmd_vel topic:

You should see messages containing linear and angular velocity values when you interact with the web interface.

## Additional Resources
# Visualizing a Map
For visualizing a map in your web controller, refer to the ROS 2D JS tutorial: Visualizing a Map.

Basic ROS Functionality
To understand the basic ROS functionalities and how to use roslibjs, check out the tutorial: Basic ROS Functionality.
