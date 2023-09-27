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

0. **My name is Betty**
    - **[0-iam_betty:](0-iam_betty)** Switch the current user to the user betty.

1. **Who am I**
    - **[1-who_am_i:](1-who_am_i)** Print the effective username of the current user.

2. **Groups**
    - **[2-groups:](2-groups)** Print all the groups the current user is part of.

3. **New owner**
    - **[3-new_owner:](3-new_owner)** Change the owner of the file hello to the user betty.

4. **Empty!**
    - **[4-empty:](4-empty)** Create an empty file called hello.

5. **Execute**
    - **[5-execute:](5-execute)** Add execute permission to the owner of the file hello.

6. **Multiple permissions**
    - **[6-multiple_permissions:](6-multiple_permissions)** Add execute permission to the owner and the group owner and read permission to other users to the file hello.

7. **Everybody!**
    - **[7-everybody:](7-everybody)** Add execution permission to the owner, the group owner, and the other users to the file hello.

8. **James Bond**
    - **[8-James_Bond:](8-James_Bond)** Set the permission to the file hello as follows: Owner: no permission at all, Group: no permission at all, Other users: all the permissions.

9. **John Doe**
    - **[9-John_Doe:](9-John_Doe)** Set the mode of the file hello to this: -rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello.

10. **Look in the mirror**
    - **[10-mirror_permissions:](10-mirror_permissions)** Set the mode of the file hello the same as olleh's mode.

11. **Directories**
    - **[11-directories_permissions:](11-directories_permissions)** Add execute permission to all subdirectories of the current directory for the owner, the group owner, and all other users.

12. **More directories**
    - **[12-directory_permissions:](12-directory_permissions)** Create a directory called my_dir with permissions 751 in the working directory.

13. **Change group**
    - **[13-change_group:](13-change_group)** Change the group owner to school for the file hello.

14. **Owner and group (Advanced)**
    - **[100-change_owner_and_group:](100-change_owner_and_group)** Change the owner to vincent and the group owner to staff for all the files and directories in the working directory.

15. **Symbolic links (Advanced)**
    - **[101-symbolic_link_permissions:](101-symbolic_link_permissions)** Change the owner and the group owner of _hello to vincent and staff respectively.

16. **If only (Advanced)**
    - **[102-if_only:](102-if_only)** Change the owner of the file hello to betty only if it is owned by the user guillaume.

17. **Star Wars (Advanced)**
    - **[103-Star_Wars:](103-Star_Wars)** Write a script that will play the Star Wars IV episode in the terminal.

## Resources

### Read or watch:

- [Permissions](http://linuxcommand.org/lc3_lts0090.php)

### man or help:

`chmod`
`sudo`
`su`
`chown`
`chgrp`
`id`
`groups`
`whoami`
`adduser`
`useradd`
`addgroup`

For detailed instructions and examples, refer to the respective script files in this repository.

---

## Special Thanks for Project Guidance to 

- **Julien Barbier**

[YouTube](https://www.youtube.com/@0xJulien) | [Twitter](https://twitter.com/julienbarbier42) | [LinkedIn](https://www.linkedin.com/in/julienbarbier/)

## License

This project is licensed under the terms of the [MIT License](https://www.alxafrica.com/terms-conditions-portal/).

---

© 2023 [ALX](https://www.alxafrica.com/). All rights reserved.
