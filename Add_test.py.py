a=1
b=2
c= a+b
print(c)
print('a*b=', a*b)

# pattern program
''' I did a pattern program here
Just provide the shape to be printed. '''

def pattern_program(size: object, width: object) -> object:
    for i in range(size):
        for j in range(width):
            print("*",end='  ')
        print('')



size = int(input('enter the size:'))
width = int(input('enter the width:'))

pattern_program(size, width)

''' just  doing some testing comments to reflect in the git hub. 
will check this one there.
'''
