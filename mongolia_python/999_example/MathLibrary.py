# math 라이브러리의 수학 함수
# 올림, 내림, 버림, 반올림
'''
import math
n = 1.3579
print(math.ceil(n))
print(math.floor(n))
print(math.trunc(n))
print(round(3.1415))
print(round(3.1415, 2))
'''

# 절댓값, 거듭제곱, 팩토리얼, 최대공약수, 제곱근
'''
import math
print(math.fabs(-5))
print(math.pow(2, 10))
print(math.factorial(5))
print(math.gcd(10, 15))
print(math.sqrt(5))
'''

# 삼각함수
'''
import math
print(math.radians(180))
print(math.degrees(math.pi))
print(math.sin(math.radians(30)))
print(math.cos(math.radians(30)))
print(math.tan(math.radians(30)))
print(math.asin(0.5))
print(math.atan(0.5))
'''

# 로그함수
'''
import math
print(math.log(1000))
print(math.log2(1024))
print(math.log10(1000))
print(math.log(10, 10))
'''

# 건물의 높이 구하기
'''
import math
distance = float(input("거리: "))
angle = float(input("각도: "))
height = math.tan(math.radians(angle)) * distance
print("높이는 %d" %height)
'''

# 각도에 따른 sin 함수 값의 변화 확인
'''
import math as m
for i in range(0, 181, 15):
        value = m.sin(m.radians(i))
        print("각도: %3d, 사인값: %.2f" %(i, value))
'''

