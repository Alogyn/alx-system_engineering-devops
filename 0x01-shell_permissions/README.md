# 0x01. Shell, Permissions - DevOps Project

This project is part of the DevOps curriculum and focuses on shell basics and permissions in a Linux environment. The project consists of a series of tasks that cover various aspects of shell scripting, user permissions, and file ownership.

## Overview

- **Project Name**: Shell, Permissions
- **Project Type**: DevOps
- **Shell**: Bash
- **Author**: Julien Barbier
- **Weight**: 1
- **Start Date**: August 31, 2023, 4:00 AM
- **End Date**: September 2, 2023, 4:00 AM

## Project Description

This is an ongoing second chance project with an auto-review that will be launched at the deadline. The project is designed to test your knowledge and understanding of shell commands, Linux file permissions, and related topics.

## Learning Objectives

By completing this project, you will gain knowledge and skills in the following areas:

- Understanding Linux file permissions.
- Familiarity with commands like `chmod`, `sudo`, `su`, `chown`, and `chgrp`.
- Representing file permissions for owner, group, and others.
- Changing file permissions, ownership, and groups.
- Running commands with root privileges.
- Creating users and groups.
- Printing user and group information.

## Resources

To successfully complete this project, you can refer to the following resources:

- [Linux Permissions](https://www.tutorialspoint.com/unix/unix-file-permission.htm)
- `man` or `help` pages for commands like `chmod`, `sudo`, `su`, `chown`, `chgrp`, `id`, `groups`, `whoami`, `adduser`, `useradd`, `addgroup`

## Requirements

### General

- Allowed Editors: vi, vim, emacs
- All scripts will be tested on Ubuntu 20.04 LTS.
- Each script should be exactly two lines long (`$ wc -l file` should print 2).
- All script files should end with a new line.
- The first line of each script should be `#!/bin/bash`.
- Provide a `README.md` file at the root of the project folder, describing each script's purpose.
- Avoid using backticks, `&&`, `||`, or `;` in your scripts.
- Ensure that all script files are executable using `chmod`.

### Quiz Questions

- Complete the quiz successfully.

## Project Structure

The project consists of the following tasks:

1. **My name is Betty**
   - Create a script that switches the current user to the user betty.
   - Example: `$ ./0-iam_betty`

2. **Who am I**
   - Write a script that prints the effective username of the current user.
   - Example: `$ ./1-who_am_i`

3. **Groups**
   - Write a script that prints all the groups the current user is part of.
   - Example: `$ ./2-groups`

4. **New owner**
   - Write a script that changes the owner of the file "hello" to the user betty.
   - Example: `$ sudo ./3-new_owner`

5. **Empty!**
   - Write a script that creates an empty file called "hello."
   - Example: `$ ./4-empty`

6. **Execute**
   - Write a script that adds execute permission to the owner of the file "hello."
   - Example: `$ ./5-execute`

7. **Multiple permissions**
   - Write a script that adds execute permission to the owner and group owner, and read permission to other users, to the file "hello."
   - Example: `$ ./6-multiple_permissions`

8. **Everybody!**
   - Write a script that adds execution permission to the owner, group owner, and other users, to the file "hello."
   - Example: `$ ./7-everybody`

9. **James Bond**
   - Write a script that sets permissions to the file "hello" as follows:
     - Owner: no permission at all
     - Group: no permission at all
     - Other users: all permissions
   - Example: `$ ./8-James_Bond`

... (continue for all tasks)

## Copyright & Plagiarism

- You are responsible for coming up with solutions for the tasks.
- Copying and pasting someone else's work is strictly forbidden and will result in removal from the program.
- You are not allowed to publish any content of this project.

## License

This project is licensed under the terms of the [MIT License](LICENSE).

---

© 2023 ALX. All rights reserved.
