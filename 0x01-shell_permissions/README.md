# 0x01. Shell, Permissions - DevOps Project

This project is part of the DevOps curriculum and focuses on gaining proficiency in working with shell basics and permissions in a Linux environment. The project consists of a series of tasks that cover various aspects of shell scripting, user permissions, and file ownership.

## Learning Objectives

By completing this project, you will:

- Gain a deep understanding of Linux file permissions.
- Familiarize yourself with essential shell commands like `chmod`, `sudo`, and `chown`.
- Learn to represent and manipulate file permissions.
- Understand how to change file ownership and group.
- Master the execution of commands with root privileges.

## Project Structure

The project contains a series of scripts, each addressing specific tasks related to shell basics and permissions. Here's a brief overview of the tasks:

0. **[My name is Betty](https://github.com/Alogyn/alx-system_engineering-devops/blob/master/0x01-shell_permissions/0-iam_betty)**: Create a script that switches the current user to the user betty.

1. **[Who am I](https://github.com/Alogyn/alx-system_engineering-devops/blob/master/0x01-shell_permissions/1-who_am_i)**: Write a script that prints the effective username of the current user.

2. **[Groups](https://github.com/Alogyn/alx-system_engineering-devops/blob/master/0x01-shell_permissions/2-groups)**: Write a script that prints all the groups the current user is part of.

3. **[New owner](https://github.com/Alogyn/alx-system_engineering-devops/blob/master/0x01-shell_permissions/3-new_owner)**: Write a script that changes the owner of the file hello to the user betty.

4. **[Empty!](https://github.com/Alogyn/alx-system_engineering-devops/blob/master/0x01-shell_permissions/4-empty)**: Write a script that creates an empty file called hello.

5. **[Execute](https://github.com/Alogyn/alx-system_engineering-devops/blob/master/0x01-shell_permissions/5-execute)**: Write a script that adds execute permission to the owner of the file hello.

6. **[Multiple permissions](https://github.com/Alogyn/alx-system_engineering-devops/blob/master/0x01-shell_permissions/6-multiple_permissions)**: Write a script that adds execute permission to the owner and the group owner and read permission to other users to the file hello.

7. **[Everybody!](https://github.com/Alogyn/alx-system_engineering-devops/blob/master/0x01-shell_permissions/7-everybody)**: Write a script that adds execution permission to the owner, the group owner, and the other users to the file hello.

8. **[James Bond](https://github.com/Alogyn/alx-system_engineering-devops/blob/master/0x01-shell_permissions/8-James_Bond)**: Write a script that sets the permission to the file hello as follows: Owner: no permission at all, Group: no permission at all, Other users: all the permissions.

9. **[John Doe](https://github.com/Alogyn/alx-system_engineering-devops/blob/master/0x01-shell_permissions/9-John_Doe)**: Write a script that sets the mode of the file hello to this: -rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello.

10. **[Look in the mirror](https://github.com/Alogyn/alx-system_engineering-devops/blob/master/0x01-shell_permissions/10-mirror_permissions)**: Write a script that sets the mode of the file hello the same as olleh's mode.

11. **[Directories](https://github.com/Alogyn/alx-system_engineering-devops/blob/master/0x01-shell_permissions/11-directories_permissions)**: Create a script that adds execute permission to all subdirectories of the current directory for the owner, the group owner, and all other users.

12. **[More directories](https://github.com/Alogyn/alx-system_engineering-devops/blob/master/0x01-shell_permissions/12-directory_permissions)**: Create a script that creates a directory called my_dir with permissions 751 in the working directory.

13. **[Change group](https://github.com/Alogyn/alx-system_engineering-devops/blob/master/0x01-shell_permissions/13-change_group)**: Write a script that changes the group owner to school for the file hello.

14. **[Owner and group (Advanced)](https://github.com/Alogyn/alx-system_engineering-devops/blob/master/0x01-shell_permissions/100-change_owner_and_group)**: Write a script that changes the owner to vincent and the group owner to staff for all the files and directories in the working directory.

15. **[Symbolic links (Advanced)](https://github.com/Alogyn/alx-system_engineering-devops/blob/master/0x01-shell_permissions/101-symbolic_link_permissions)**: Write a script that changes the owner and the group owner of _hello to vincent and staff respectively.

16. **[If only (Advanced)](https://github.com/Alogyn/alx-system_engineering-devops/blob/master/0x01-shell_permissions/102-if_only)**: Write a script that changes the owner of the file hello to betty only if it is owned by the user guillaume.

17. **[Star Wars (Advanced)](https://github.com/Alogyn/alx-system_engineering-devops/blob/master/0x01-shell_permissions/103-Star_Wars)**: Write a script that will play the Star Wars IV episode in the terminal.

## Resources

- [Permissions](http://linuxcommand.org/lc3_lts0090.php)

For detailed instructions and examples, refer to the respective script files in this repository.

---

## Special Thanks for Project Guidance to 

- **Julien Barbier**

[YouTube](https://www.youtube.com/@0xJulien) | [Twitter](https://twitter.com/julienbarbier42) | [LinkedIn](https://www.linkedin.com/in/julienbarbier/)

## License

This project is licensed under the terms of the [MIT License](https://www.alxafrica.com/privacy-policy/).

---

© 2023 [ALX](https://www.alxafrica.com/). All rights reserved.
