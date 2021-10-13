# 365days
Repo consists of practise, projects and work for 1 year


# Practise problems include LeetCode(LC) problems
The following will show list of LC problems, files and if it's completed:

1. #1 (Two sum; day6.py) - *passes* with + integers so far
2. #9 (Palindrome; day7, day8) - *passes* however TypeError on LC regarding  '__init__() takes exactly 2 arguments (1 given)'
3. #7 (Reverse integer; day12) - *passes* w/ +/-ive inputs; Not tested on LC due to confusion in using classes

------

# Budget App

1st iteration:

- input for each category (dict) [completed]
- set limits for each category [completed]
- balances between categories
- transfers between categories
- connect to db


Problem: Create a Budget class that can instantiate ~~~ objects based on different budget categories ~~~ like food, clothing, and entertainment. These objects should allow for depositing and withdrawing funds from each category, as well computing category balances and transferring balance amounts between categories

IOW:

Categories: Food, Clothing, Hobby, Subscriptions, PC equip, coffee

Features: expenses,
           deposit/withdraw funds from each category,
             balances/transfer between categories

Input: Dict {} of all expenses i.e. transactions history type data
Output: expenses, balances/transfer between categories, deposit/wd funds from each catg.

Topics found during reading on Decorators (Credits: https://book.pythontips.com/en/latest/decorators.html ):
- Nested function
- function as argument for another func.
- ANSWER TO LONG-TIME QUESTION: having () in front of functions executes them (i.e. returns whatever code's inside of them) BUT w/o them, function itself is assigned to the variables

----------

This repo will be stale as of 12/10/2021.
