#!/bin/bash
echo "Which C file do you want to run? Be sure to include the .c file extension." #asks user for .c file to run
read filename
echo "File Name Read"
objname="${filename%?}"
objname="${objname%?}"
echo "Object File Name Created: "$objectname""
gcc "$filename" -o ""$objname".o"
echo "C File Compiled"
gcc -static ""$objname".o" -lm
echo "Object File Linked"
./"$objname".out
echo "C File Run"
