a = float(input("First Number: "))
b = float(input("Second Number: "))
c = float(input("Third Number: "))

s = (a+b + c) / 2
area = (s* (s-a)* (s-b) * (s-c)) ** 0.5

print('the area is : %0.2f' % area)