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
import datetime
import random

def get_date():
    get = datetime.date.today()
    day = get.day
    month = get.month
    year = get.year

    full_date = str(day) + '/' + str(month) + '/' + str(year)
    return full_date

s = ','

get_eid = lambda : input('Enter Employee Id : ')

split_by = lambda x: x.split(s)

# Function to open files in 'read-mode'
def open_file_in_r(x):
    if x == 'd':
        fobj = open('all_dish.txt', 'r')
        fdata = fobj.readlines()
        fobj.close()

        return fdata
    elif x == 'e':
        fobj = open('all_employees.txt', 'r')
        fdata = fobj.readlines()
        fobj.close()

        return fdata
    elif x == 'b':
        fobj = open('all_bills.txt', 'r')
        fdata = fobj.readlines()
        fobj.close()

        return fdata

def get_dish_price(code):
    fdata = open_file_in_r('d')
    found = False
    for i in fdata:
        ls = split_by(i)
        if ls[0] == str(code):
            found = True
            return ls[1], int(ls[2][0:len(ls[2]) - 1])

    if found == False: 
        print('   Invalid Dish Code')
        return None, -1
 
def create_bill():
    fdata = open_file_in_r('b')
    bill_code = str(len(fdata) + 1)
    print('What would like to have')
    final_bill_amt = 0

    while True:
        d_code = int(input('Enter dish code or 0 : '))

        if d_code != 0:
            name, pr = get_dish_price(d_code)
            if pr == -1: 
                continue
            elif pr != -1:
                qnt = int(input('Quantity of ' + name + ' : '))
                tot = pr * qnt
                final_bill_amt = final_bill_amt + tot
        elif d_code == 0:
            if final_bill_amt > 0:
                bill_date = get_date()
                fobj = open('all_bills.txt', 'a')
                fobj.write(bill_code + s + str(final_bill_amt) + s + bill_date + '\n')
                print('Bill Created Succefully')
                break
            else: 
                print('Bill is Not Created!')
                break


def add_new_dish():
    fdata = open_file_in_r('d')
    dcode = str(len(fdata) + 1)
    dname = input('Enter Dish Name : ')
    dprice = input('Enter Dish Price : ')

    fobj = open('all_dish.txt', 'a')
    fobj.write(dcode + s + dname + s + dprice + '\n')
    fobj.close()
    print('New Dish Added Succesfully')

newstr = None

def update_dish():
    dcode = input('Enter Dish Code : ')
    fdata = open_file_in_r('d')
    found = False 
    ind = 0
    for i in fdata:
        ls = split_by(i)
        if ls[0] == dcode:
            found = True 
            updated_p = input('Enter the Price to Update : ')
            ls[2] = updated_p + '\n'
            newstr = s.join(ls)
            fdata[ind] = newstr
            break
        else: ind += 1

    if found == False: print('Invalid Dish Code')
    if found == True:
        dobj = open('all_dish.txt', 'w')
        dobj.writelines(fdata)
        dobj.close()
        print('Price Updated Succesfully')


def add_new_emp():
    fdata = open_file_in_r('e')
    eid = str(len(fdata) + 1)
    ename = input('Enter Employee Name : ')
    eaadhar = input('Enter Employee Aadhar Number : ')
    emob = input('Enter Employee Monile Number : ')
    epost = input("Enter Employee's Post : ")

    fobj = open('all_employees.txt', 'a')
    fobj.write(eid + s + ename + s + eaadhar + s + emob + s + epost + '\n')
    fobj.close()
    print('New Employee Details Added Succesfully')

def remove_emp():
    eid = get_eid()

    fdata = open_file_in_r('e')
    found = False
    ind = 0
    for i in fdata:
        ls = split_by(i)
        if ls[0] == eid:
            found = True
            break
        else: ind += 1
    
    if found == False: print('Invalid Employee ID')
    if found == True: 
        fdata.pop(ind)
        fobj = open('all_employees.txt', 'w')
        fobj.writelines(fdata)
        fobj.close()
        print('Data Removed Succefully')

def update_emp_info():
    eid = get_eid()
    updated_post = input("Enter Employee's Updated Position : ")

    fdata = open_file_in_r('e')
    found = False
    ind = 0
    for i in fdata:
        ls = split_by(i)
        if ls[0] == eid:
            ls[4] = updated_post + '\n'
            found = True 
            newstr = s.join(ls)
            fdata[ind] = newstr
            break
        else: ind += 1

    if found == False: print('Invalid Employee Id')
    elif found == True:
        fobj = open('all_employees.txt', 'w')
        fobj.writelines(fdata)
        fobj.close()
        print('Employee Details Updated')
            

def view_emp_info():
    eid = get_eid()    

    fdata = open_file_in_r('e')
    found = False
    for i in fdata:
        ls = split_by(i)
        if ls[0] == eid:
            print('Employee Name :', ls[1])
            print('Employee Aadhar Number :', ls[2])
            print('Employee Mobile Number :', ls[3])
            print("Employee's Position :", ls[4], end='')
            found = True
            break

    if found == False: print('Invalid Employee ID')

def today_earn(): 
    fdata = open_file_in_r('b')
    date = get_date()
    add = 0
    
    for i in fdata:
        ls = split_by(i)
        if ls[2] == date + '\n':
            add += int(ls[1])
        else: add = add
        
    print(" Today's Total Earning :", add)

def date_earn():
    date = input('Enter Date to View Earning : ')
    fdata = open_file_in_r('b')
    add = 0

    for i in fdata:
        ls = split_by(i)
        if ls[2] == date + '\n':
            add += int(ls[1])

    print('', date, 'Total Earning :', add)


def between_date():
    first_date = input(' Enter Start Date : ')
    end_date = input(' Enter End Date : ')
    fdata = open_file_in_r('b')
    add = 0

    for i in fdata:
        ls = split_by(i)
        sp = ls[2].split('/')
        fd = first_date.split('/')
        ed = end_date.split('/')

        if (int(sp[0]) >= int(fd[0]) and int(sp[0]) <= int(ed[0])) and (int(sp[1]) >= int(fd[1]) and int(sp[1]) <= int(ed[1])):
            add += int(ls[1])

    print(' Earning between', first_date, 'and', end_date, ':', add)

def view_earnings():
    print(" 1 - View Today's Earning")
    print(" 2 - View Earning of Specific Date")
    print(" 3 - View Earning between Specific Dates")
    ch = int(input(' Enter your choice : '))

    if ch == 1: today_earn() 
    elif ch == 2: date_earn()
    elif ch == 3: between_date()

    
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
    print('0 - Exit')


def check_op():
    if ch == 1: create_bill() 
    elif ch == 2: add_new_dish()
    elif ch == 3: update_dish()
    elif ch == 4: add_new_emp()
    elif ch == 5: remove_emp()
    elif ch == 6: update_emp_info()
    elif ch == 7: view_emp_info()
    elif ch == 8: view_earnings()
    elif ch == 0: exit(0)


open('all_dish.txt', 'a')
open('all_employees.txt', 'a')
open('all_bills.txt', 'a')

while True:
    operations()
    ch = int(input('Enter Your Choice : '))
    check_op()

