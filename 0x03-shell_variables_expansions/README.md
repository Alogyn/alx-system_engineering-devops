# 0x03. Shell, init files, variables, and expansions - DevOps Project

This project is part of the DevOps curriculum and focuses on enhancing your shell scripting skills. You'll work with shell initialization files, environment variables, alias creation, arithmetic operations, and more. The tasks are designed to help you become proficient in shell scripting, which is crucial for DevOps engineers.

## Learning Objectives

By completing this project, you are expected to achieve the following learning objectives:

- Understand the role of shell initialization files.
- Distinguish between local and global variables.
- Master the usage of expansions in shell scripting.
- Create and manage aliases effectively.
- Perform arithmetic operations within shell scripts.
- Implement text encoding and decoding using rot13 encryption.
- Work with different number bases in shell scripts.

## Project Structure

The project is organized into a series of tasks, each focusing on a specific aspect of shell scripting:

0. **<o>**
    - **[0-alias:](0-alias)** Create a script that sets up an alias for the `ls` command, allowing you to remove all files in the current directory with a single command.

1. **Hello you**
    - **[1-hello_you:](1-hello_you)** Create a script that greets the current Linux user by printing "hello user."

2. **The path to success is to take massive, determined action**
    - **[2-path:](2-path)** Expand your system's PATH variable by adding `/action` as the last directory to be searched for programs.

3. **If the path be beautiful, let us not ask where it leads**
    - **[3-paths:](3-paths)** Write a script to count the number of directories in the PATH variable.

4. **Global variables**
    - **[4-global_variables:](4-global_variables)** Create a script that lists all environment variables on your system.

5. **Local variables**
    - **[5-local_variables:](5-local_variables)** Write a script that lists both local and environment variables, including functions.

6. **Local variable**
    - **[6-create_local_variable:](6-create_local_variable)** Develop a script that creates a new local variable named BEST with the value "School."

7. **Global variable**
    - **[7-create_global_variable:](7-create_global_variable)** Create a script that establishes a new global variable named BEST with the value "School."

8. **Every addition to true knowledge is an addition to human power**
    - **[8-true_knowledge:](8-true_knowledge)** Write a script that performs an arithmetic operation by adding 128 to the value stored in the TRUEKNOWLEDGE environment variable.

9. **Divide and rule**
    - **[9-divide_and_rule:](9-divide_and_rule)** Create a script that calculates the result of dividing POWER by DIVIDE, where POWER and DIVIDE are environment variables.

10. **Love is anterior to life, posterior to death, initial of creation, and the exponent of breath**
    - **[10-love_exponent_breath:](10-love_exponent_breath)** Build a script that calculates and displays the result of raising BREATH to the power of LOVE, where BREATH and LOVE are environment variables.

11. **There are 10 types of people in the world -- Those who understand binary, and those who don't**
    - **[11-binary_to_decimal:](11-binary_to_decimal)** Write a script to convert a binary number stored in the BINARY environment variable to its decimal equivalent.

12. **Combination**
    - **[12-combinations:](12-combinations)** Generate all possible combinations of two lowercase letters (excluding "oo") and print them alphabetically.

13. **Floats**
    - **[13-print_float:](13-print_float)** Create a script that prints a number stored in the NUM environment variable with exactly two decimal places.

14. **Decimal to Hexadecimal (Advanced)**
    - **[100-decimal_to_hexadecimal:](100-decimal_to_hexadecimal)** Convert a decimal number stored in the DECIMAL environment variable to its hexadecimal representation.

15. **Everyone is a proponent of strong encryption (Advanced)**
    - **[101-rot13:](101-rot13)** Develop a script that encodes and decodes text using the rot13 encryption method.

16. **The eggs of the brood need to be an odd number (Advanced)**
    - **[102-odd:](102-odd)** Write a script that prints every other line from the input, starting with the first line.

17. **I'm an instant star. Just add water and stir. (Advanced)**
    - **[103-water_and_stir:](103-water_and_stir)** Create a script that performs base conversion using environment variables WATER and STIR, storing the result in the base BESTCHOL.

## Resources

### Read or watch:

- [Expansions](http://linuxcommand.org/lc3_lts0080.php)
- [Shell Arithmetic](https://www.gnu.org/software/bash/manual/html_node/Shell-Arithmetic.html)
- [Variables](https://tldp.org/LDP/Bash-Beginners-Guide/html/sect_03_02.html)
- [Shell initialization files](https://tldp.org/LDP/Bash-Beginners-Guide/html/sect_03_01.html)
- [The alias Command](https://www.linfo.org/alias.html)
- [Technical Writing](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/misc/2021/6/9112669886fd446a2aa3113c31319d1f468dc160.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230922%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230922T154710Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=76aa23cae692bbd0b21f78bb800c492bafd46a2893a93a7f0682710ea373e3ed)

### man or help:

`printenv`
`set`
`unset`
`export`
`alias`
`unalias`
`.`
`source`
`printf`

For detailed instructions and examples, refer to the respective script files in this repository.

---

## Special Thanks for Project Guidance to 

- **Julien Barbier**

[YouTube](https://www.youtube.com/@0xJulien) | [Twitter](https://twitter.com/julienbarbier42) | [LinkedIn](https://www.linkedin.com/in/julienbarbier/)

## License

This project is licensed under the terms of the [MIT License](https://www.alxafrica.com/terms-conditions-portal/).

---

© 2023 [ALX](https://www.alxafrica.com/). All rights reserved.
