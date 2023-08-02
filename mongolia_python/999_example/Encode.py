import time

letter = "Hello Python"
encodeletter = ""

for ch in letter:
      num = ord(ch)
      encodeletter += chr(num-1)

print("원문: ", letter)
print("암호: ", encodeletter)

time.sleep(1)

decodeletter = ""

for ch in encodeletter:
      num = ord(ch)
      decodeletter += chr(num-1)

print("암호 해제: ", decodeletter)
