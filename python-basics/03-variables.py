"""
This is a comment
written in
more than just one line
"""
# Single line comment

# Below a and name are varibles which have values defined
a=10
name='Dasari'

print(a)
print(name)

# Type casting
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

print("x = ",x,"\ny = ",y,"\nz = ",z)

x = "I am a global variable"

def someFunction():
    print("Inside function:: ",x)
    
someFunction()
print("Outside function:: ",x)

def anotherFunction():
    b="I am a local variable"
    print("Inside function:: ",b)
anotherFunction()



def declareGlobal():
    global a
    a=100
    print("Inside Function:: ",a)

declareGlobal()
print("Outside Function:: ",a)

#print("Outside function:: ",b)

c="I am local value"
def outerFunction():
    c = "I am local value"
    def innerFunction():
        nonlocal c
        c = "I am non-local value"
        print("Inner function value of c:: ",c)
    innerFunction()
    print("Outer function value of c:: ",c)
    
    outerFunction()