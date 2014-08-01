import random
import sys

def math():
    print 'Lets start with some math'
    num1 = random.randint(10, 100)
    num2 = random.randint(10, 100)
    print 'How much is %d + %d' % (num1, num2)
    while True:
        answer = raw_input('Enter your answer please:')
        try:
            answer = int(answer)
            break
        except ValueError:
            print "Numbers only. Try again."

    if int(answer) == num1 + num2:
        print 'Correct!!! Well done'
    else:
        print 'Wrong answer.'

def spell():
    print 'Logic test'
    age = raw_input('How old are you? ')
    print 'If you are a pilot of a plane and the plane flys 1000 miles per hour what is the age of the pilot'
    answer = raw_input('Guess the age of the pilot:')
    if int(answer) == int(age):
        print 'Correct!'
    else:
        print 'Read very carefully the question'

def welcome():
    print 'Hello, what is your name?'
    name = raw_input('')
    print 'It is good to meet you ' + name.capitalize()
    return spell()

welcome()
