# # <- Do not write comments in red text!!
# plus, minus, multiplication, dividing
# use %d(decimal<- integer!!)
# Input two integers

# solve

num1 = int(input("num1: "))
num2 = int(input("num2: "))
result1 = num1 + num2
result2 = num1 - num2
result3 = num1 * num2
result4 = num1 // num2 # // -> integer dividing

print("%d + %d = %d" %(num1, num2, result1))
print("%d - %d = %d" %(num1, num2, result2))
print("%d * %d = %d" %(num1, num2, result3))
print("%d / %d = %d" %(num1, num2, result4))
