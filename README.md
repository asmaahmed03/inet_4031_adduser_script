# INET 4031 Add User Script (Python)

## Description

os: This module enables the script to interface with the operating system, specifically to add users.

re: This is for pattern matching. It helps the script detect lines starting with # and process other text patterns.

sys: It lets the script use outside arguments, which in this case is the input file.

## Operation 

### Input File Specification 

The input file should have the following format:

*** username:default_password:last_name:first_name:comma_separated_list_of_groups

For example:

jdoe11:mypass:Doe:John:admins, reviewers

The name of the input file is up to the user. Convention is create-users.input

### Running the Script
Set Permissions: You might need to give the script permission to execute. You can do this by : chmod +x create-users.py
Using Python 3: This script requires Python 3. Double-check your Python 3 version: python3 --version
Executing the Script: Navigate to the directory containing the script and input file. Then: sudo python3 create-users.py < create-users.input
