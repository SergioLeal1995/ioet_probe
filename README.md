# Overview

This code was develop in Python whit an input, process, output arquitecture. Also in order to rehuse code a module was implemented whose is incharged to do the validation about how much  per day the company will pay to the employee, and finally each value per day is save in a collect variable allowing to know during the working days the salary of the employee. To finish, the output is show in console whit each employee and their respective salary.
README file has the problem in order to put in context the reader, the explanation of the arquitecture giving an overview about how the problem was on board, approach and metodology which is in charge to explain details of the solving process and finally how to run the code.

# Problem
The company ACME offers their employees the flexibility to work the hours they want. They will pay for the hours worked based on the day of the week and time of day, according to the following table:

| **Day of the week** | **value** |
|:-------------------:|:---------:|
| Monday - Friday     |           |
| 00:01-09:00         | 25 USD    |
| 09:01-18:00         | 15 USD    |
| 18:01-00:00         | 20 USD    |
| Saturday and sunday |           |
| 00:01-09:00         | 30 USD    |
| 09:01-18:00         | 20 USD    |
| 18:01-00:00         | 25 USD    |

### Input: 
the name of an employee and the schedule they worked, indicating the time and hours. This should be a .txt file with at least five sets of data.

#### Example:
RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00

### Output
indicate how much the employee has to be paid

#### Example
The amount to pay RENE is: 215 USD

# Explanation arquitecture

The code arquitecture is based on input, process, output; In this case the input of the program is the file whose contain the data-set with each employee and their respective hours during the week. The process is about all required actions to extract, clean, and interact whit the data in order to solve the problem. Finally the output whose is the aswer about how much the company should pay to each employee.
During the develop process is neccesary to set a descomposition of the problem, in order to be easier the way to solve it. The items taking into account were, data reading, data descomposition, conditions validation and print results. Also a module was created because that code section is used twice. In addition to be the code more efficient.

# Approach and metodology

For this case the approach of the problem is to split the data-set in a properly way, in order to know how much the company should pay to the employee, first of all is neccesary to read the data-set and save the data in a list because then it will be read in a for statement due to the quantity of employees. For each employee the process is to split in a specific points in order to obtain segmented data-sets and to have the posibility to operate each of them. In this case, obtain the name, day and the working hours for the employee, once we have the data in that way is neccesary to do a check about the day of the week and taking into account the hours to assign the salary of the employee in those days. To allow the preview idea was neccesary to create a module in which a validation is made about the hours intervals and taking into account the payment per days of the week.

# How to run
### Windows 
Inside the folder of the project open a power shell window, if you want to see the output of the script on screen type the following command.

```bash
python main.py
```
Otherwise if you want to redirect the output of the script and see it in a txt file run the following command
```bash
python main.py > output.txt
```
### Linux
After clone the project, open a terminal inside the folder and type de following command
```bash
python3 main.py 
```

All of those previous methods to execute the code will show in the console the next output
```bash
The amount to pay RENE is: 215 USD
The amount to pay ASTRID is: 85 USD
The amount to pay SERGIO is: 790 USD
The amount to pay SILVIA is: 275 USD
The amount to pay TOM is: 90 USD
```
