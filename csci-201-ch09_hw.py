
import pickle

###################################################################################

class Student:
    def __init__(self,first,last,gpa):
        self.first=first
        self.last=last
        self.gpa=gpa

###################################################################################

def validate_gpa(low,high,prompt):
    valid=False
    while not valid:
        try:
            number=float(input(prompt))
            if number < low or number > high:
                raise ValueError
            else:
                valid=True
        except ValueError:
            print("Invalid entry. Please enter a numeric value between",low,"and",high)
    return number


def validate_choice(low,high,prompt):
    valid=False
    while not valid:
        try:
            number=int(input(prompt))
            if number < low or number > high:
                raise ValueError
            else:
                valid=True
        except ValueError:
            print("Invalid selection. Please enter a numeric value between",low,"and",high)
    return number


def validate_name(prompt):
    valid=False
    while not valid:
        try:
            name=input(prompt)
            test=name.isalpha()
            if test == False:
                raise ValueError
            else:
                valid=True
        except ValueError:
            print("Invalid entry. Please enter letters only")
    return name

###################################################################################

def new_student():
    first=validate_name('enter the first name: ')
    last=validate_name('enter the last name: ')
    gpa=validate_gpa(1.0,4.0,'enter the gpa: ')

    new_student=Student(first=first,last=last,gpa=gpa)
    
    students.append(new_student)


def display_average_gpa():
    count=0
    total=0
    for student in students:
        count+=1
        gpa=student.gpa
        total+=float(gpa)
    print(total)
    total=total/count
    total=round(total,2)
    print(count)
        
    print('The average GPA is:',total)
    #print(count)


def save_students():
    with open(file_name,'wb') as out_file:
        pickle.dump(students,out_file)


def load_students2():
    global students2
    with open(file_name,'rb') as input_file:
        students2=pickle.load(input_file)


def load_students():
    global students
    with open(file_name,'rb') as input_file:
        students=pickle.load(input_file)


def display_students():
    load_students2()
    for student in students2:
        first=student.first
        last=student.last
        gpa=student.gpa
        print(first,last,gpa)


###################################################################################
###################################################################################
###################################################################################


'''Students Program'''

file_name='students.pickle'


try:
    load_students()
    print('\nStudents file found... the previous data has been loaded into the program\n')
except:
    print('\nStudents file not found... creating new file\n')
    students=[]
    students2=[]


create=validate_choice(1,6,"How many studnets do you have to enter? [up to 6] ")


count=0
while count < create:
    count+=1
    print("\nNew Student",count,"data:")
    print('-----------------------')
    new_student()


print('')
display_average_gpa()
print('')
save_students()

print('Dumping the student data into a pickle file\n')

print('Loading pickle file to new list and outputting the results')
print('----------------------------------------------------------')

display_students()


###################################################################################
###################################################################################
###################################################################################


'''Employees Program'''

print('\n\n')
employees={'cashier':9.25,'supervisor':13.55,'manager':21.25}

print('Dictionary contents: ',employees)

print('''
1) cashier
2) supervisor
3) manager
''')

choice=validate_choice(1,3,'Choose your position: ')


if choice==1:
    print('Your pay is $',employees['cashier'])
elif choice==2:
    print('Your pay is $ ',employees['supervisor'])
elif choice==3:
    print('Your pay is $ ',employees['manager'])




    
