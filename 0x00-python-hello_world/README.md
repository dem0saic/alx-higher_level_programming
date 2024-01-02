

Code
Issues
Pull requests
Breadcrumbsalx-higher_level_programming/0x00-python-hello_world
/README.md
Latest commit
deezyfg
deezyfg
8 hours ago
History
100 lines (80 loc) · 4.28 KB
File metadata and controls

Preview

Code

Blame
0x00-python-hello_world
This project introduces fundamental concepts of Python programming. Below are the tasks for this project:

Mandatory Tasks
0. Run Python file
Write a Shell script that runs a Python script.

The Python file name will be saved in the environment variable $PYFILE.
1. Run inline
Write a Shell script that runs Python code.

The Python code will be saved in the environment variable $PYCODE.
2. Hello, print
Write a Python script that prints exactly "Programming is like building a multilingual puzzle", followed by a new line.

Use the function print.
3. Print integer
Complete this source code to print the integer stored in the variable number, followed by 'Battery street', followed by a new line.

The output should be:
the number, followed by 'Battery street',
followed by a new line.
Your code must be 3 lines long.
You have to use f-strings.
4. Print float
Complete the source code to print the float stored in the variable number with a precision of 2 digits.

The output should be:
'Float:', followed by the float with only 2 digits,
followed by a new line.
You are not allowed to cast 'number' to string
You have to use f-strings.
5. Print string
Complete this source code to print 3 times a string stored in the variable str, followed by its first 9 characters.

The output should be:
3 times the value of str,
followed by a new line,
followed by the 9 first characters of str,
followed by a new line.
You are not allowed to use any loops or conditional statements
Your program should be maximum 5 lines long.
6. Play with strings
Complete this source code to print 'Welcome to Holberton School!'

You are not allowed to use any loops or conditional statements.
You have to use the variables 'str1' and 'str2' in your new line of code
Your program should be exactly 5 lines long.
7. Copy - Cut - Paste
Complete this source code to manipulate strings.

You are not allowed to use any loops or conditional statements.
Your program should be exactly 8 lines long.
word_first_3 should contain the first 3 letters of the variable word.
word_last_2 should contain the last 2 letters of the variable word.
middle_word should contain the value of the variable word without the first and last letters.
8. Create a new sentence
Complete this source code to print 'object-oriented programming with Python', followed by a new line.

You are not allowed to use any loops or conditional statements.
Your program should be exactly 5 lines long.
You are not allowed to create new variables.
You are not allowed to use string literals.
9. Easter Egg
Write a Python script that prints “The Zen of Python”, by Tim Peters, followed by a new line.

Your script should be maximum 98 characters long. (please check with 'wc -m 9-easter_egg.py')
10. Linked list cycle
Technical interview preparation:

You are not allowed to google anything
Whiteboard first
This task and all future technical interview prep tasks will include checks for the efficiency of your solution, i.e. is your solution’s runtime fast enough, does your solution require extra memory usage / mallocs, etc.
Write a function in C that checks if a singly linked list has a cycle in it.

Prototype: int check_cycle(listint_t *list).
Return: '0' if there is no cycle, '1' if there is a cycle.
Requirements:
Only these functions are allowed: 'write', 'printf', 'putchar', 'puts', 'malloc', 'free'.
Advanced Tasks
11. Hello, write
Write a Python script that prints exactly 'and that piece of art is useful - Dora Korpar, 2015-10-19', followed by a new line.

Use the function write from the sys module.
You are not allowed to use 'print'.
Your script should print to 'stderr'.
Your script should exit with the status code '1'.
12. Compile
Write a script that compiles a Python script file.

The Python file name will be stored in the environment variable $PYFILE.
The output filename has to be $PYFILEc (ex: 'export PYFILE=my_main.py' => output filename: 'my_main.pyc').
13. ByteCode -> Python #1
Write the Python function def magic_calculation(a, b): that does exactly the same as the provided Python bytecode.

Tip: Python bytecode
