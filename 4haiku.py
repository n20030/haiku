# -*- coding: utf-8 -*-
import time
import random


li = ['国','島','牛','魚','空','海','雲','浜辺','かもめ','鳥','蝉','蝶','蝉','猫','犬','星','月','虹']
li2 = ['の','は','も','よ','か','を','が']
li3 = ['泣く','笑う','読む','歌う','飛ぶ','羽ばたく','香る','踊る']
li4 = ['せつなさ','虚しさ','懐かしさ','はかなさ']


li_random = random.choice(li)
li_random2 = random.choice(li)
li_random3 = random.choice(li)

li2_random = random.choice(li2)
li2_random2 = random.choice(li2)
li2_random3 = random.choice(li2)

li3_random = random.choice(li3)
li3_random2 = random.choice(li3)
li3_random3 = random.choice(li3)

li4_random = random.choice(li4)
li4_random2 = random.choice(li4)
li4_random3 = random.choice(li4)

print(li_random + li2_random + li_random2)
time.sleep(1)

print(li_random3 + li2_random2 + li4_random)
time.sleep(1)

print(li4_random2 + li2_random3)