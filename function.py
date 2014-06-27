def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b
a = add(30,40);
s = subtract(40,30);
m = multiply(7,8);
d = divide(18,9);

print "Add: %d, Subtract: %d, multiply: %d, divide: %d" %(a,s,m,d)