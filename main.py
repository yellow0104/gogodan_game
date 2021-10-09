# 정우제작
import random
import time
print("구구단을 외자~")
time.sleep(1.2)
print("구구단을 외자~")
one_number = random.randint(12345, 99999999999)
two_number = random.randint(12345, 99999999999)
print(f"{one_number} x {two_number} 는?")
answer = one_number * two_number
answer = str(answer)
inp = input("정답은>")
if inp == answer:
    print("정답입니다")
else:
    print("오답입니다")
