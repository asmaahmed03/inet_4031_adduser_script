#!/usr/bin/python3
import os
import re
import sys

def main():
    for line in sys.stdin:

        # Using re.match to detect and skip lines that start with a '#'.
        match = re.match(r'^#', line)

        # Strip whitespace and split the line at ':'.
        fields = line.strip().split(':')

        # Skip lines with '#' or not having 5 fields.
        if match or len(fields) != 5:
            continue

        # Extract user details from the fields.
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3], fields[2])

        # Split group details at ','.
        groups = fields[4].split(',')

        # Create the user account.
        print("==> Creating account for %s..." % username)
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)
        os.system(cmd)  # Execute the command.

        # Set the user password.
        print("==> Setting the password for %s..." % username)
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)
        os.system(cmd)

        # Assign the user to groups.
        for group in groups:
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username, group))
                cmd = "/usr/sbin/adduser %s %s" % (username, group)
                os.system(cmd)  # Execute the command.

if __name__ == '__main__':
    main()
