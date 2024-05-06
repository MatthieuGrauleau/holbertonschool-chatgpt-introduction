1. Debugging - Python Arguments
mandatory
Objective: Use ChatGPT to identify and correct errors in code samples.

$ cat print_arguments.py
#!/usr/bin/python3
import sys

for i in range(len(sys.argv)):
    print(sys.argv[i])

$ ./print_arguments.py 1 2 3
print_arguments.py
1
2
3
You can download the code here.

Fix the code, it should print only the arguments without the python file name.