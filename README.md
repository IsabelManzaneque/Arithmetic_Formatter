# Arithmetic_Formatter
Function that receives a list of strings that are arithmetic problems and returns the problems arranged vertically and side-by-side.
## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
## General info
Students in primary school often arrange arithmetic problems vertically to make them easier to solve. For example, "235 + 52" becomes:
```
  235
+  52
-----
```
this function receives a list of strings that are arithmetic problems and returns the problems arranged vertically and side-by-side. The function takes a second argument: when the second argument is set to `True`, the answers is displayed.
The function will return the correct conversion if the supplied problems are properly formatted, otherwise, it will return a string that describes an error.

* Situations that will return an error:
  * If there are **too many problems** supplied to the function. The limit is **five**, anything more will return:
    `Error: Too many problems.`
  * The appropriate operators the function will accept are **addition**, **subtraction**, **divisionn** and **multiplication**. Anything else will return an error:
    `Error: Operator must be '+', '/', '*' or '-'.`
  * Each operand should only contain digits. Otherwise, the function will return:
    `Error: Numbers must only contain digits.`
  * Each operand has a max of six digits in width. Otherwise, the error string returned will be:
    `Error: Numbers cannot be more than six digits.`
## Technologies
Project is created with:
* Python 3.9.6
* PyCharm Community Edition 2021.1.2 x64
## Setup
To run this project in PyCharm:
```
Download .zip
Execute main file
``
