#list+

#alt + 3, alt + 4

##scores = [90, 80, 70, 60, 50]
##print(scores)
##average = sum(scores)/5

#range function -> make list

##a = list(range(1, 11, 1))
##print(a)
##b = list(range(5, 50, 5))
##print(b)

#append function
##new_list = [10, 20, 30]
##print(new_list)
##new_list.append(40)
##print(new_list)

#insert function(index)
##a = [1, 2, 3, 4, 5]
##print(a)
##a.insert(1, 10)
##print(a)
##a.insert(2, "hello")
##print(a)

#extend function
##a = [1, 2, 3]
##b = [4, 5, 6]
##a.extend(b)
##print(a)
##print(b)

#ex
##a += [7,8,9] # a = a + [7, 8, 9]
##b -= [7,8,9] # b = b - [7, 8, 9]
##c *= [7,8,9] # c = c * [7, 8, 9]

#list and loop
##a = [1,2,3,4,5]
##i = 0
##while i<=4:
##    print(a[i])
##    i += 1 # i = i + 1
##
##print("\n")
##for n in a:
##    print(n)

#list input
##scores = []
##SUM = 0
##for i in range(5): # i = 0, i = 1, i = 2, i = 3, i = 4
##    scores.append(int(input("score input %d: " %(i+1))))
##    SUM += scores[i]
##print(scores)
##print("sum: ", SUM)
##print("average: ", SUM/5)

#count function
##a = [10, 20, 20, 40, 50]
##print(a.count(10)) # 1
##print(a.count(20)) # 2

#remove function
##a = [10, 20, 30, 40, 50]
##print(a)
##a.remove(10)
##print(a)

#index function
##a = [10, 20, 30, 40, 50]
##print(a.index(30))

#sort function
##a = [20, 40, 10, 90, 80]
##a.sort()
##print(a)

#pop function
a = [10, 20, 30, 40, 50]
print(a.pop())
print(a.pop())
print(a.pop(0))
#press F5!!


