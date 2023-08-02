# 물건 구입 계산 프로그램
import sys

bread = 2000; milk = 1000; fruit = 2000; coffee = 3000; water = 500
payment = 0; totalamount = 0

while 1:
    print("\n<요금표>\n\t1 : 빵 (2000)\n\t2 : 우유 (1000)\n\t3 : 과일 (2000)\n\t4 : 커피 (3000)\n\t5 : 물 (500)\n\t- 3개 이상 주문시 : 전체 금액의 10% 할인\n\t- 5개 이상 주문시 : 전체 금액의 15% 할인\n")
    code = int(input("구입할 물건의 코드 입력: "))
    quantity = int(input("구입할 물건의 수량 입력: "))
    totalamount += quantity
    if code == 1:
        payment += bread * quantity
    elif code == 2:
        payment += milk * quantity
    elif code == 3:
        payment += fruit * quantity
    elif code == 4:
        payment += coffee * quantity
    elif code == 5:
        payment += water * quantity
    else:
        print("올바른 숫자를 입력해주세요.")
        continue
    num = int(input("\n계속 구입 : 1 / 계산 하기 : 0\n숫자 입력 : "))
    if num == 1:
        continue
    elif num == 0:
        break
    else:
        print("올바른 숫자를 입력해주세요.")
        print("처음부터 다시 시작합니다.")
        sys.exit()

print("<계산하기>")
if totalamount >= 5:
    totalpayment = payment * (85/100)
    print("5개 이상 구매시 15% 할인이 적용됩니다.")
    print("기존 요금 {0}원 >> 할인된 요금 {1}원".format(payment, totalpayment))
elif totalamount >=3:
    totalpayment = payment * (90/100)
    print("3개 이상 구매시 10% 할인이 적용됩니다.")
    print("기존 요금 {0}원 >> 할인된 요금 {1}원".format(payment, totalpayment))
else:
    totalpayment = payment
    
print("최종 요금: %.1f원" %totalpayment)
while 1:
    money = int(input("지불할 금액 입력: "))
    change = money - totalpayment
    if change > 0:
        print("거스름돈: %.1f원" %change)
        break
    elif change == 0:
        print("거스름돈이 없습니다.")
        break
    else:
        print("지불한 금액이 부족합니다.")
        continue
print("계산 완료.")
