PI = 3.141592653589793

def add(x, y):
    return x + y

def diff(x, y):
    return (x - y) if x > y  else (y - x)

def area_of_circle(radius):
    return PI * radius * radius

def area_of_rectangle(width , length):
    return width * length