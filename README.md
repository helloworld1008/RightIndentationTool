# RightIndentationTool

RightIndentationTool is a python-based script that right indents a block of code using a tab by specifying the start and end line number in the source code file. With this tool, there is no need to use vi editor and manually add tab at each line in the file

To illustrate with an example, below are a few lines from the original file

```sh
$ cat testfile
Line 1

This is line 2

Line 3

Line 4

This is line 5
This is line 6

This line 7

```

## How to use
Clone this file from the repo, give it executable permissions and run it. 
You need to enter the absolute path of the file and specify the line numbers that you want to indent

```sh
$ ./right_indentation_tool.py 

Enter absolute path of file: /root/testfile

Original file saved to /root/testfile_23_01_2022_12_27_21.orig

1 Line 1
2 
3 This is line 2
4 
5 Line 3
6 
7 Line 4
8 
9 This is line 5
10 This is line 6
11 
12 This line 7

Enter start line number: 5

Enter end line number: 9

File /root/testfile modified

$
$ cat /root/testfile
Line 1

This is line 2

        Line 3

        Line 4

        This is line 5
This is line 6

This line 7
$

```


