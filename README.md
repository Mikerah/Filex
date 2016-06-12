#Filex

## Overview
Filex is a really simply file explorer for Windows built using python and PyQt5. Users can copy files and directories, navigate the firectory structure, create new files and directories and rename files and directories. I left out a lot of things since I was getting bored of this project.

## What I've learned
I've increased my understanding of the Python programming language. I've learned how to declare static methods in Python and about circular dependencies (of which this project contains lots of). I've also learned more about the os and shutil modules, thus increasing my understanding of how to control the operating system through python. I've also learned a ton more about the PyQt5 Framework. I've created my own custom widgets for directories and files and implemented my own custom slots and signals. This project wasn't that difficult but it did stretch my current skills and was a good challenge.

## Improvements
There are a lot of improvements that can be made to Filex. Exceptions are not handled at all. Also, navigating the file structure is buggy and doesnt't work as it should but it'll do for now. Comments and documentation needs to be added for future reference. I would also do more refactoring to the code to eliminate circular dependencies and have the Directory and File widgets inherit from another custom widget to eliminate reimplementing a lot of the same functionality for both.
