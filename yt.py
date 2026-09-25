
print('********************************')
print('SIMPLE STUDENT ASSISTANT PROJECT')
print('********************************')
print('')
print('Bonjour! I am your Ai Assistant. So, I can help you in doing your small projects and tasks.')
print('')
print('How can I help you??')

#CHALLANGE 1
name = input('What is your name?')
print('Hello! ' + name)
programming_language = input('Which is your favourite programming language?')
print('Nice to meet you ' + name + ' you like ' + programming_language)

#CHALLENGE 2
age = int(input("How old are you?"))
print(age)
school = str(input('Your School name?'))
print(school)
course = input("What is your Course in " + school)
print(course)

#CHALLENGE 3
choice = input('What do you want? ' \
'1. Grades  ' \
'2. Motivation  ' \
'3. Study Advice  ' \
'4. Problem Solution  ')

if choice == '1':
    print('Let us check your grades')
    grade = float(input("What are your grades out of 20 "))
    if grade >= 16:
        print('EXCELLENT HARDWORK, ITS VERY GOOD')
    elif grade >= 14 and grade <= 15.99:
        print("GOOD! You did well. Keep it up")
    elif grade >= 10 and grade <= 13.99:
        print("GOOD! You did well. Keep it up")
    elif grade <= 9.99:
        print('You Failed')
    else:
        print('Incorrect number')

    grade1 = float(input("Enter you First Semester's grade: ")) 
    grade2 = float(input("Enter your Second Semester's grade: ")) 
    grade3 = float(input("Enter your Third Semester's grade: "))
    average = (grade1 + grade2 + grade3) / 3 
    print("Your average grade is: ", average) 

elif choice == '2':
    print('Beleive in yourself. You can do anything')
    a = input('Type "more" for more motivation: ')
    print(a)
    if a == 'more':
        print ('Practice makes the man perfect')
        b = input('Type "more" for more motivation: ')
        if b == 'more':
            print('Journey of thousand miles starts with a single step')
            c = input('Type "more" for more motivation: ')
            if c == 'more':
                print('Failures are stepping stones to success')
            else:
                print('First act upon this and then you will get more motivation')
        else:
            print('First act upon this and then you will get more motivation')
    else:
        print('First act upon this and then you will get more motivation')

elif choice == '3':
    print('Never gave up. Understand every topic and ask questions until not all clear')
elif choice == '4':
    print('Drop your problem here. I can help you in solving this')
else:
    print('I dont know that option yet')
    

print('===================')
print(' PROGRAM ENDS HERE')
print("===================")

