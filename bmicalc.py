import random
from time import sleep  #importing time for sleep 
from os import system, name  #importing only system from os
from font import bmicalc,by,ashim,weight_font,height_font,thankyou  #importing all the fonts generated in ascii

#defining a screen clearing function:
def clear():
    if name == 'nt': 
        _ = system('cls')
    #for windows
    
    else:
        _ = system('clear') #for mac and linux
        
# function to get correct input for correct conversion
def get_choice(n):
    '''
    n means how many  choices are to be given to the user
    '''
    while True:
        print('~'*50)
        choice=input('\nPlease input your choice: \n')
        try:
            choice=int(choice)
            if choice not in range(1,n+1):
                print("\n'{}' was an invalid choice".format(choice))
            else: 
                break
        except ValueError:
            print("\n '{}' is not a valid choice.".format(choice))
    print('~'*50)
    global main_choice
    main_choice=choice
    
    
def get_correct_input(to_measure):
    global data
    '''
    to measure==what to be displayed to measure
    '''
    while True:
        print('~'*50)
        print("\nPlease input your {} : \n".format(to_measure))
        data=input()
        try:
            data=float(data)
            if data<=0:
                print("\n{a} cannot be '{b}' \n".format(a=to_measure, b=data))
            else:
                break
        except ValueError:
            print("\n'{}' is not a valid input.\n".format(data))
    print('~'*50)
    
    
    
    
#function to check bmi

def check_bmi(bmi):
    if bmi<18.5:
        print('You are under weight')
        print("Take more protein and carbs")
    elif 18.5<=bmi<=24.9:
        print('You are normal')
        print("Do exercises regularly to maintain your health")
    elif 25<=bmi<=29.9:
        print("You seem to be over-weight")
        print("You must limit carbs. intake and do exercises")
    elif bmi>=30:
        print("You are obesed")
        print("You must do exercises daily.")
        print("You must develop a healthy eating habit.")
        print("You must be seriously concerned to your health now.")



def loading_dialogue():   #for some interesting effect
    print("~"*50)
    print("\t\tLoading Your BMI....... ")
    print("~"*50)
    sleep(0.89)
    print()
    print()
    print("\t\tL")
    sleep(0.09)
    print("\t\tLO")
    sleep(0.09)
    print("\t\tLOA")
    sleep(0.09)
    print("\t\tLOAD")
    sleep(0.09)
    print("\t\tLOADI")
    sleep(0.09)
    print("\t\tLOADIN")
    sleep(0.09)
    print("\t\tLOADING")
    sleep(0.09)
    print("\t\tLOADING.....")
    sleep(1)
    clear()




#MY MAIN PROGRAM STARTS FROM HERE:
#INTRO
sleep(0.9)
bmicalc()
sleep(0.3)
by()
sleep(0.3)
ashim()
sleep(2.3)
clear()

program_active=True  #Declaring a variable saying program is active
while program_active:
    #the program for mass part
    print()
    print('*'*50)
    weight_font()
    print('*'*50)
    print("\nChoose the unit to input your weight")
    print('''
        1. Kilogram
        2. Pound
        ''')
    print()
    mass=0
    data=0
    main_choice=0
    get_choice(2)
    sleep(0.75)
    clear()
    if main_choice==1:
        get_correct_input('weight (kg)')
        mass=data
        sleep(.75)
        clear()
        pass
    elif main_choice==2:
        get_correct_input('weight (pound)')
        mass=data
        mass*=0.453592
        sleep(.75)
        clear()
        
        
    #program for height part
    print()
    print("*"*50)
    height_font()
    print("*"*50)
    print("Choose the unit to input your height")
    print('''
    1. Meter
    2. Centimeters
    3. Feet
    4. Inches
    ''')
    data=0
    main_choice=0
    height=0
    get_choice(4)

    sleep(.75)
    clear()
    if main_choice==1:
        get_correct_input('height (m)')
        height=data
        sleep(.75)
        clear()
    elif main_choice==2:
        get_correct_input('height (cm)')
        height=data
        height*=0.01
        sleep(.75)
        clear()
    elif main_choice==3:
        get_correct_input('height (feet)')
        height=data
        height*=0.3048
        sleep(.75)
        clear()
    elif main_choice==4:
        get_correct_input('height (inches)')
        height=data
        height*=0.0254
        sleep(.75)
        
    loading_dialogue()
    
    bmi=mass/(height**2)

    clear()
    print("~"*50)
    print()
    print("Your BMI is : %1.2f "%(bmi))
    print()
    sleep(0.79)
    check_bmi(bmi)
    print("~"*50)
    sleep(2)
    print()
    
    
    #asking for replay?
    print()
    print("\t\t\t\t",'~'*50)
    print("\t\t\t\t    Do you want to run the program again ? (y/n)")
    print("\t\t\t\t",'~'*50)
    ask1=input()
    response1=ask1[0].upper()
    while response1!='Y' and response1!="N":
        print('\t\t\t\t ',"Sorrry! '{}' was an invalid input. Say (y/n)".format(ask1))
        ask1=input()
        response1=ask1[0].upper()
    if response1=='N':
        program_active= False
        print()
        print()
        print()
        thankyou()
        print()
        print()
        sleep(2)
        clear()
    else:
        clear()
#MAIN PROGRAM ENDS HERE

print("Press any key to exit")
input()