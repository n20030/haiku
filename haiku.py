# -*- coding: utf-8 -*-

import random
import time

def sl1():
	time.sleep(1)
def sl2():
	time.sleep(2)


subject_two_letters = ['夜', '海', '空', '昼', '石', '豆', '熊', '蝉']
subject_three_letters = ['魚' , 'かもめ', '子猫', '雀'　, 'マグロ', 'つばめ']
subject_four_letters = ['石橋'　,'なめくじ', 'うみうし' , 'かにかま', 'シマウマ', 'ウミガメ']


predicate_one_letters = ['を', 'に', 'や', 'も', 'よ']
predicate_two_letters = ['たち', 'の音'　, 'の目'　,]


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