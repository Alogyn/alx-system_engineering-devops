# 0x02. Shell, I/O Redirections and filters - DevOps Project

This project is a part of the DevOps curriculum and aims to enhance your proficiency in working with the shell, specifically Bash, within a Linux environment. Throughout this project, you will engage in tasks that explore various aspects of shell commands, file manipulation, and input/output redirection.

## Learning Objectives

By completing this project, you will:

- Develop a deep understanding of shell commands and their applications.
- Gain familiarity with essential commands like `head`, `tail`, `find`, `wc`, `sort`, `uniq`, `grep`, and `tr`.
- Learn to redirect standard input/output to and from files.
- Discover how to chain commands and filters using redirections.
- Acquire knowledge about special characters and their usage in the shell

## Project Structure

The project contains a series of scripts, each addressing specific tasks related to shell redirections. Here's a brief overview of the tasks:

0. **Hello World**
    - **[0-hello_world:](0-hello_world)** Write a script that prints "Hello, World" followed by a new line to the standard output.

1. **Confused Smiley**
    - **[1-confused_smiley:](1-confused_smiley)** Write a script that displays a confused smiley "(Ôo)'.

2. **Let's Display a File**
    - **[2-hellofile:](2-hellofile)** Display the content of the /etc/passwd file.

3. **What About 2?**
    - **[3-twofiles:](3-twofiles)** Display the content of both /etc/passwd and /etc/hosts files.

4. **Last Lines of a File**
    - **[4-lastlines:](4-lastlines)** Display the last 10 lines of the /etc/passwd file.

5. **I'd Prefer the First Ones Actually**
    - **[5-firstlines:](5-firstlines)** Display the first 10 lines of the /etc/passwd file.

6. **Line #2**
    - **[6-third_line:](6-third_line)** Display the third line of the file iacta.

7. **It is a Good File That Cuts Iron Without Making a Noise**
    - **[7-file:](7-file)** Create a shell script that creates a file named exactly \*\\'"Best School"\'\\*$\?\*\*\*\*\*:) containing the text "Best School" ending with a new line.

8. **Save Current State of Directory**
    - **[8-cwd_state:](8-cwd_state)** Write a script that writes into the file ls_cwd_content the result of the command ls -la. If the file ls_cwd_content already exists, it should be overwritten. If the file ls_cwd_content does not exist, create it.

9. **Duplicate Last Line**
    - **[9-duplicate_last_line:](9-duplicate_last_line)** Write a script that duplicates the last line of the file iacta.

10. **No More JavaScript**
    - **[10-no_more_js:](10-no_more_js)** Write a script that deletes all the regular files (not directories) with a .js extension that are present in the current directory and all its subfolders.

11. **Don't Just Count Your Directories, Make Your Directories Count**
    - **[11-directories:](11-directories)** Write a script that counts the number of directories and sub-directories in the current directory. Hidden directories should be counted, and the current and parent directories should not be taken into account.

12. **What’s New**
    - **[12-newest_files:](12-newest_files)** Create a script that displays the 10 newest files in the current directory, one file per line, sorted from newest to oldest.

13. **Being unique is better than being perfect**
    - **[13-unique:](13-unique)** Create a script that takes a list of words as input and prints only words that appear exactly once.

14. **It must be in that file**
    - **[14-findthatword:](14-findthatword)** Display lines containing the pattern "root" from the file /etc/passwd.

15. **Count that word**
    - **[15-countthatword:](15-countthatword)** Display the number of lines that contain the pattern "bin" in the file /etc/passwd.

16. **What's next?**
    - **[16-whatsnext:](16-whatsnext)** Display lines containing the pattern "root" and 3 lines after them in the file /etc/passwd.

17. **I hate bins**
    - **[17-hidethisword:](17-hidethisword)** Display all the lines in the file /etc/passwd that do not contain the pattern "bin".

18. **Letters only please**
    - **[18-letteronly:](18-letteronly)** Display all lines of the file /etc/ssh/sshd_config starting with a letter, including capital letters.

19. **A to Z**
    - **[19-AZ:](19-AZ)** Replace all characters 'A' and 'c' from input to 'Z' and 'e' respectively.

20. **Without C, you would live in hiago**
    - **[20-hiago:](20-hiago)** Create a script that removes all letters 'c' and 'C' from input.

21. **esreveR**
    - **[21-reverse:](21-reverse)** Write a script that reverses its input.

22. **DJ Cut Killer**
    - **[22-users_and_homes:](22-users_and_homes)** Write a script that displays all users and their home directories, sorted by users, based on the /etc/passwd file.

23. **Empty casks make the most noise**
    - **[100-empty_casks:](100-empty_casks)** Write a command that finds all empty files and directories in the current directory and all sub-directories. List only the names of the files and directories (not the entire path).

24. **A gif is worth ten thousand words**
    - **[101-gifs:](101-gifs)** Write a script that lists all the files with a .gif extension in the current directory and all its sub-directories. List only regular files (not directories) and sort them by byte values in a case-insensitive manner.

25. **Acrostic**
    - **[102-acrostic:](102-acrostic)** Create a script that decodes acrostics that use the first letter of each line.

26. **The biggest fan**
    - **[103-the_biggest_fan:](103-the_biggest_fan)** Write a script that parses web server logs in TSV format as input and displays the 11 hosts or IP addresses which did the most requests, ordered by the number of requests (most active host or IP at the top).

## Resources

### Read or watch:

- [Shell, I/O Redirection](http://linuxcommand.org/lc3_lts0070.php)
- [Special Characters](http://mywiki.wooledge.org/BashGuide/SpecialCharacters)

### man or help:

`echo`
`cat`
`head`
`tail`
`find`
`wc`
`sort`
`uniq`
`grep`
`tr`
`rev`
`cut`
`passwd (5)` (i.e. `man 5 passwd`)

For detailed instructions and examples, refer to the respective script files in this repository.

---

## Special Thanks for Project Guidance to 

- **Julien Barbier**

[YouTube](https://www.youtube.com/@0xJulien) | [Twitter](https://twitter.com/julienbarbier42) | [LinkedIn](https://www.linkedin.com/in/julienbarbier/)

## License

This project is licensed under the terms of the [MIT License](https://www.alxafrica.com/terms-conditions-portal/).

---

© 2023 [ALX](https://www.alxafrica.com/). All rights reserved.
