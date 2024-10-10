'''
Files required:
1.  all_dish.txt ---> This file contains:
	 dish_code, dish_name, dish_price

2.  all_employees.txt ---> This file contains:
	empid, empname, empaadhar, empmob, emppost

3.  all_bills.txt ---> This file contains
	bill_num, bill_total, bill_date
	(bill number should be automatically generated.)

Features of the application:-
1. Create Bill
2. Add New Dish (in menu)
3. Update Dish (in menu)
4. Add New Employee
5. Remove Employee
6. Update Employee Information
7. View Employee Information
8. View Earnings:
	a. View Today's earning
	b. View Earning of Specific Date
	c. View Earning between specific Dates
'''

###################################################################

def create_bill():
    pass

def add_new_dish():
    pass

def update_dish():
    pass

def add_new_emp():
    pass

def remove_emp():
    pass

def update_emp_info():
    pass

def view_emp_info():
    pass

def view_earnings():
    pass


def operations():
    input()
    print('Select Operation:')
    print('1 - Create Bill')
    print('2 - Add New Dish')
    print('3 - Update Dish')
    print('4 - Add New Employee')
    print('5 - Remove Employee')
    print('6 - Update Employee Information')
    print('7 - View Employee Information')
    print('8 - View Earnings')


def check_op():
    if ch == 1: create_bill() 
    elif ch == 2: add_new_dish()
    elif ch == 3: update_dish()
    elif ch == 4: add_new_emp()
    elif ch == 5: remove_emp()
    elif ch == 6: update_emp_info()
    elif ch == 7: view_emp_info()
    elif ch == 8: view_earnings()


while True:
    operations()
    ch = input('Enter Your Choice : ')
    check_op()

