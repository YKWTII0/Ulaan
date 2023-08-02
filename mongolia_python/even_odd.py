# Бүхэл тоо оруулах, тэгш сондгой тоог нөхцөлт
# хэллэгээр ялгах програм бичье.
# (Зөвлөгөө: Үлдсэн оператор %)

# 하나의 정수를 입력하고, 조건문으로
# 짝수와 홀수를 구별하는 프로그램을 작성해봅시다.
# (힌트: 나머지 연산자 %)
# 10 % 2 == 0
# 5 % 2 == 1

# solve
import sys

inputNum = int(input("input integer : "))

if inputNum <= 0:
    print("This is Negative Num.")
    print("Program exit.")
    sys.exit() # system exit
else: # ex) inputNum > 0
    if inputNum % 2 == 0:
        print("Even Num")
    else:
        print("Odd Num")
# press F5!

