##import sys
##import random
##import time
### 2 second
##
##print("Dice!")
##i = 0
##while i<100:
##    value = random.randint(1, 6)
##    print("Dice value: %d" %value)
##    time.sleep(2)
##sys.exit()

#ex
#start = 1
#end : input
#number count program-> use while loop


#1-ээс оролтын утгын төгсгөл хүртэлх тоог
#while давталт ашиглан тоолох программ бүтээцгээе!
##startvalue = int(input("startvalue: "))
##endvalue = int(input("endvalue: "))
##
##while startvalue <= endvalue:
##    print("Count: %d" %startvalue)
##    startvalue += 1

#use for loop!!
##startvalue = int(input("startvalue: "))
##endvalue = int(input("endvalue: "))
##
##for startvalue in range(startvalue, endvalue+1, 1):
##    print("Count: %d" % startvalue)



#Оролтын m утгыг n оролтын утга дээр нэмээд
#тэдгээрийн нийлбэрийг хэвлэнэ.
#while loop!


#Төгсгөлийн утга нь эхлэх утгаас бага байвал алдаа гарна!
#-> Онцгой байдлын зохицуулалт
import sys
startvalue = int(input("startvalue: "))
endvalue = int(input("endvalue: "))
SUM = 0

# hint : sys.exit()
# If else ашиглан алдаагаа засна уу!

if startvalue <= endvalue:
    while startvalue <= endvalue:
        print("Count: %d" %startvalue)
        SUM += startvalue
        startvalue += 1
else:
    sys.exit()
print(SUM)



    
