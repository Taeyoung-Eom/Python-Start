# 함수
from random import *

lotto = []
while len(lotto) != 6:
    num = randint(1, 45)
    if num not in lotto:
        lotto.append(num)

lotto.sort()
print("안녕하십니까 주인님")
print("이번주 로또 당첨 번호는 {0} 입니다." .format(lotto))
