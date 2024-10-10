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

s = ','

get_eid = lambda : input('Enter Employee Id : ')

split = lambda x: x.split(s)

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

def create_bill():
    pass

get_dcode = lambda : input('Enter Dish Code : ')

def add_new_dish():
    dcode = get_dcode()
    dname = input('Enter Dish Price : ')
    dprice = input('Enter Dish Price : ')

    fobj = open('all_dish.txt', 'a')
    fobj.write(dcode + s + dname + s + dprice + '\n')
    fobj.close()
    print('New Dish Added Succesfully')

def update_dish():
    dcode = get_dcode()
    updated_p = input('Enter the Price to Update : ')

    fdata = open_file_in_r('d')
    found = False 
    ind = 0
    newstr = None
    for i in fdata:
        ls = split(i)
        if ls[0] == dcode:
            found = True 
            ls[2] = updated_p + '\n'
            newstr = s.joind(ls)
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
    eid = get_eid()
    ename = input('Enter Employee Name : ')
    eaadhar = input('Enter Employee Aadhar Number : ')
    emob = input('Enter Employee Monile Number : ')
    epost = input("Enter Employee's Post : ")

    fobj = open('all_employee.txt', 'a')
    fobj.write(eid + s + ename + s + eaadhar + s + emob + s + epost + '\n')
    fobj.close()
    print('New Employee Details Added Succesfully')

def remove_emp():
    pass

def update_emp_info():
    pass

def view_emp_info():
    eid = get_eid()    

    fdata = open_file_in_r('e')
    found = False
    for i in fdata:
        ls = split(i)
        if ls[0] == eid:
            print('Employee Name :', ls[1])
            print('Employee Aadhar Number :', ls[2])
            print('Employee Mobile Number :', ls[3])
            print("Employee's Position :", ls[4])
            found = True
            break

    if found == False: print('Invalid Employee ID')

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

