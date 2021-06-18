""" Python Script to convert the infix expression into postfix form. """

# Write your code from here

##Infix notation is characterized by the placement of operator between the operands like 2 + 2.
##Postfix notation is characterized by the placement of operator after the operands like 2 2 +.
##Prefix notation is characterized by the placement of operator before the operands like + 2 2.


operator_set = set(['+', '-', '*', '/', '(', ')', '^'])
priority  = {'+':1, '-':1, '*':2, '/':2, '^':3}

def infix_to_postfix(expression):
    stack = []
    output = '' 
    for character in expression:
        if character not in operator_set:
            output+= character
        elif character=='(':
            stack.append('(')
        elif character==')':
            while stack and stack[-1]!= '(':
                output+=stack.pop()
                stack.pop()
        else:
            while stack and stack[-1]!='(' and priority[character]<=priority[stack[-1]]:
                output+=stack.pop()
            stack.append(character)
    while stack:
        output+=stack.pop()
    return output

expression = input('Enter infix expression: ')
print('Given infix expression: ',expression)
print('Postfix expression: ',infix_to_postfix(expression))

##Output

##Enter infix expression: x^y/(5*x)+2
##Given infix expression:  x^y/(5*x)+2
##Traceback (most recent call last):
##  File "C:\Suraj\GITAM\Data Structures\data_structures_using_python_lab_assignment-SurajAravind\09_infix_postfix.py", line 35, in <module>
##    print('Postfix expression: ',infix_to_postfix(expression))
##  File "C:\Suraj\GITAM\Data Structures\data_structures_using_python_lab_assignment-SurajAravind\09_infix_postfix.py", line 24, in infix_to_postfix
##    stack.pop()
##IndexError: pop from empty list


