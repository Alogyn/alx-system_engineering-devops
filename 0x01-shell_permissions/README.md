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

1. **My name is Betty**: Create a script that switches the current user to the user betty.

2. **Who am I**: Write a script that prints the effective username of the current user.

3. **Groups**: Write a script that prints all the groups the current user is part of.

4. **New owner**: Write a script that changes the owner of the file hello to the user betty.

5. **Empty!**: Write a script that creates an empty file called hello.

6. **Execute**: Write a script that adds execute permission to the owner of the file hello.

7. **Multiple permissions**: Write a script that adds execute permission to the owner and the group owner and read permission to other users to the file hello.

8. **Everybody!**: Write a script that adds execution permission to the owner, the group owner, and the other users to the file hello.

9. **James Bond**: Write a script that sets the permission to the file hello as follows: Owner: no permission at all, Group: no permission at all, Other users: all the permissions.

10. **John Doe**: Write a script that sets the mode of the file hello to this: -rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello.

11. **Look in the mirror**: Write a script that sets the mode of the file hello the same as olleh's mode.

12. **Directories**: Create a script that adds execute permission to all subdirectories of the current directory for the owner, the group owner, and all other users.

13. **More directories**: Create a script that creates a directory called my_dir with permissions 751 in the working directory.

14. **Change group**: Write a script that changes the group owner to school for the file hello.

15. **Owner and group (Advanced)**: Write a script that changes the owner to vincent and the group owner to staff for all the files and directories in the working directory.

16. **Symbolic links (Advanced)**: Write a script that changes the owner and the group owner of _hello to vincent and staff respectively.

17. **If only (Advanced)**: Write a script that changes the owner of the file hello to betty only if it is owned by the user guillaume.

18. **Star Wars (Advanced)**: Write a script that will play the Star Wars IV episode in the terminal.

## Requirements and Guidelines

- Use allowed editors: vi, vim, emacs.
- Scripts will be tested on Ubuntu 20.04 LTS.
- Ensure that scripts are exactly two lines long.
- End all files with a new line.
- Start all scripts with `#!/bin/bash`.
- Provide a README.md file with a description of the repository and explanations of each script.
- Avoid using backticks, `&&`, `||`, or `;` in your scripts.
- Make all scripts executable using `chmod`.

For detailed instructions and examples, refer to the respective script files in this repository.

---

## Author

- **Julien Barbier**

[YouTube](https://www.youtube.com/@0xJulien) | [Twitter](https://twitter.com/julienbarbier42) | [LinkedIn](https://www.linkedin.com/in/julienbarbier/)

## License

This project is licensed under the terms of the [MIT License](LICENSE).

---

© 2023 [ALX](https://www.alxafrica.com/). All rights reserved.
