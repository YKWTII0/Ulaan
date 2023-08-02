# 파일에 내용 쓰기
'''
fp = open("c:\\Python_C\\hello.txt", "w")
fp.write("Hello World\n")
fp.write("My name is BeomGyu\n")
fp.close()
print("파일을 열어보세요.")
'''

# 파일에 내용 추가
'''
fp = open("c:\\Python_C\\hello.txt", "a")
fp.write("Nice to meet you\n")
fp.close()
print("파일에 내용이 추가되었습니다.")
'''

# 구구단 출력하기
'''
fp = open("c:\\Python_C\\구구단 5단.txt", "w")
for t in range(1, 10, 1):
    fp.write("5 X {0} = {1}\n".format(t, 5*t))
fp.close()
print("구구단 5단이 파일에 출력되었습니다.")
'''

# 이중 for문 활용**
'''
fp = open("c:\\Python_C\\구구단.txt", "w")
for n in range(2, 10, 1):
    fp.write("\n구구단 %d단 출력\n" %n)
    fp.write("-----------------\n")
    for t in range(1, 10, 1):
        fp.write("%3d X %3d = %3d\n" %(n, t, n*t))
print("구구단 전체가 파일에 출력되었습니다.")
fp.close()
'''

# 파일 읽기
'''
fp = open("c:\\Python_C\\read_text.txt", "r")
while 1:
    line = fp.readline()
    if len(line) == 0:
        break
    print(line, end = "")
fp.close()
'''
'''
fp = open("c:\\Python_C\\read_text.txt", "r")
for line in fp.readlines():
    print(line, end = "")
fp.close()
'''

# 예외상황 처리
'''
try:
    text = input("출생연도 입력: ")
    year = int(text)
    age = 2022 - year + 1
    print("당신은 {0}살입니다.".format(age))
except:
    print("예상치 못한 상황으로 종료합니다.")
finally:
    print("이용해 주셔서 감사합니다.")
'''

# 예외상황 파악하기
# 다중 except 처리
'''
try:
    t = input("정수 입력: ")
    n = int(t)
    m = 100 / n
    print("100을 %d로 나눈 몫: %d" %(n, m))
    print("입력한 두번째 숫자: %c" %t[1])
except ValueError:
    print("예외상황: 값 변환 오류")      # 3.14 입력
except ZeroDivisionError:
    print("예외상황: 0으로 나눈 오류")        # 0 입력
except IndexError:
    print("예외상황: 인덱스 범위 오류")        # 6번 라인 발생
'''
