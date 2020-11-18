# -*- coding: utf-8 -*-

import random
import time

def sl1():
	time.sleep(1)
def sl2():
	time.sleep(2)

#List of season words
five_letters = ['大空に''oozorani', 'oiyukuka', 'akisameno', 'sayonarato', 'seminoyou', 'ninnnikune', 'hadukasii', 'tanosiiyo', 'kiminokoto', 'koikogare', 'natukesii']
seven_characters = ['otirunamidani' ,'sakananoyouni', 'hanabitotomoni' , 'kurusimagireno' , 'hosihuruyoruno', 'tukimohohoemu' ]

choice_five1 = random.choice(five_letters)
choice_five2 = random.choice(five_letters)
choice_seven = random.choice(seven_characters)


#print(choice_five)
#print(choice_seven)
sl1()
print(choice_five1)
sl1()
print(choice_seven)
sl1()
print(choice_five2)