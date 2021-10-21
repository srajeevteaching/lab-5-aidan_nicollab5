 Lab 5


Problem
Your friends just bought a new five room house and need your help to know how much it will cost to re-do the floors. Write a program that, given the dimensions of each of the five rooms and the desired type of flooring, outputs the cost of each room as well as the total cost. Hardwood costs $1.39/sqft, carpet costs $3.99/sqft, and tile costs $4.99/sqft.

Input Validation: Your program must work regardless of the case the floor option is typed in and any blank spaces surrounding it; If an invalid option is given, inform the user it was invalid and that you will be skipping that room (treat the cost as zero).

Round: Use the round function to round your output to two decimal places.

Instructions
Create a new Python file and place intro comments using the template below.
Use comments to write the algorithm your program will follow, including functions. Use the function decomposition described in the section below.
Create an Excel file with at least one test case for each control path in your algorithm. Use one row per test case with one column for the case's label, one column for each input, and one column for each corresponding output.
Write the Python code corresponding to each of your algorithm's steps.
Note: This lab does not require a flowchart.

Test your program using your test cases. If the output doesn't match, correct your program.

Commit and push changes and check your repository on github.com to confirm your updates before leaving lab (even if not finished).

Intro comments template
# Programmers: [your names]
# Course: CS151, Dr. Rajeev 
# Date:
# Lab Number:
# Program Inputs: [What information do you request from the user?]
# Program Outputs: [What information do you display for the user?]
Function decomposition
Your program should have a function for each of the following tasks:

Given a string representing a floor type, determine if it is a valid option.
Given a string representing a valid floor type, return the cost per square foot of that floor type.
Given a valid length and width in feet and a valid floor type, determine the cost of a single room of those dimensions for the given floor type.
Process a single room, including asking the user to input values for room dimensions and floor type. After gathering the inputs form the user, this function should call one of the other functions to compute the values.
A main function to drive the program.
Submission
One submission per team including all member names.

GitHub: Completed .py file (including comments).
Moodle: An Excel file with test cases (no flowchart required for this lab)
