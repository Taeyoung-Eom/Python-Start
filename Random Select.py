from random import *

users = ["김명석", "한완희", "이재혁", "박대호", "이주호", "엄태영", "마주남",
         "주지호", "이정훈", "이정원", "이한웅", "배현", "강현구", "유우식", "문병헌"]

users = list(users)
shuffle(users)

winners = sample(users, 4)

print("-- 당첨자 발표 --")
print("설거지 당첨자 : {0}" .format(winners[0]))
print("방청소 당첨자 : {0}" .format(winners[1:]))
print("-- 축하합니다 --")
