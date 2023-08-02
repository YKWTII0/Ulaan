#Annotation(MacOS) : Ctrl + 3, Ctrl + 4
#Annotation(Windows) : Alt + 3, Alt + 4

#[list+]
#00.Intro
#00.Танилцуулга

##scores = [90, 80, 70, 60, 50]
##print(scores)
##average = sum(scores) / 5
##print(average)

#01.range 함수로 리스트 만들기
#01.range Функц бүхий жагсаалт үүсгэх

##a = list(range(1, 11, 1))
##print(a)
##b = list(range(5, 50, 5))
##print(b)
##print("list length : %d" %len(b))

#02.리스트 항목 추가하기
#02.Жагсаалтын зүйлсийг нэмж байна

#02-1.append 함수
#02-1.append функц

##the_list = [10, 20, 30]
##print(the_list)
##the_list.append(40)
##print(the_list)

#02-2.insert 함수
#02-2.insert Функц

##a = [1, 2, 3, 4, 5]
##print(a)
##a.insert(1, 10)
##print(a)
##a.insert(0, 100)
##print(a)

#02-3.extend 함수
#02-3.extend Функц

##a = [1,2,3]
##b = [4,5,6]
##a.extend(b)
##print(a)
##print(b)
##a += [7, 8, 9]
##print(a)

#03.리스트와 반복문
#03.жагсаалт ба гогцоо

##a = [1, 2, 3, 4, 5]
##i = 0
##while i <= 4:
##    print(a[i])
##    i += 1
##print("\n")
##for n in a:
##    print(n)

#04.리스트에 입력하기
#04.
жагсаалтад оруулах

##scores = []
##sum = 0
##for i in range(5):
##    scores.append(int(input("score input %d: " %(i+1))))
##    sum += scores[i]
##print(scores)    
##print("sum: ", sum)
##print("average: ", sum/5)


#05.count 함수
#05.count Функц

##a = [10, 20, 10, 20, 10]
##print(a.count(10))
##print(a.count(20))
##print(a.count(15))


#06.remove 함수
#06.remove Функц

##a = [10, 20, 30, 40, 50]
##print(a)
##a.remove(30)
##print(a)

#07.index 함수
#07.index Функц

##a = [1, 2, 3, 4, 5]
##print(a.index(3))

#08.sort 함수 : 크기 순으로 정렬
#08.sort Функц : хэмжээгээр ангилах

##a = [10, 20, 30, 40, 50]
##a.insert(2, 100)
##print(a)
##a.sort()
##print(a)

#09.pop 함수
#09.pop Функц

##a = [10, 20, 30, 40, 50]
##print(a.pop())
##print(a.pop())
##print(a.pop())

#10.리스트와 튜플
#10.жагсаалт ба tuple

##mylist = [10, 20, 30, 40, 50]
##mytuple = (10, 20, 30, 40, 50)
##print(mylist)
##print(mytuple)
##print(30 in mytuple)
##print(mytuple[0])
##for x in mytuple:
##    print(x)

