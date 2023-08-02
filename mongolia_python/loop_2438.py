#loop_2438
#사용자로부터 N을 입력 받고, 입력 받은 N만큼
#1씩 증가하는 별을 찍으면 되는 문제
#Хэрэглэгчээс N хүлээн авч, N оролттой харьцуулахад
#1-ээр өсөх од харвах асуудал
































#sol1
inp = int(input())
for i in range(1, (inp+1)):
    for j in range(1, (i+1)):
        print("*",end="")
    print()

#sol2
inp = int(input())
for i in range(1,(inp+1)):
    print("*" * i)
 
