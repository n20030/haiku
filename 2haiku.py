# -*- coding: utf-8 -*-
import time

def sl1():
	time.sleep(1)
def sl2():
	time.sleep(2)


#2+1-2
def five_letters():
	import random

	#subject
	sub = ['夜', '海', '空', '昼', '石', '豆', '熊', '蝉','花','キス']
	#connected word
	cw = ['の', 'は' , 'を', 'ん','も',]
	#predicage
	pre = ['声','超え','音','中','まだ','色']

	random_sub = random.choice(sub)
	random_cw = random.choice(cw)
	random_pre = random.choice(pre)

	print(random_sub + random_cw + random_pre)

five_letters()
sl2()

#2+1+4
def seven_characters():
	import random

	sub = ['猿','人','虫','サメ','牛','雨','船','虹','風呂','街','山','歌','夏','冬','雲']
	cw = ['の', 'は' , 'を', 'ん','も','と','をも','が']
	pre = ['慌てる','とまどう','まどろむ','よろめく','かすめる','香るは','舞い散る','目覚める','隠れる']

	random_sub = random.choice(sub)
	random_cw = random.choice(cw)
	random_pre = random.choice(pre)


	print(random_sub + random_cw + random_pre)

seven_characters()
sl2()

def five_letters2():
	import random
	#endless beauty
	eb = ['花曇り','はかなさよ','ふるさとよ','旅人よ','最上川','ふじの山','恋人よ','想い人','せつなさよ','友とゆく','泡の中']
	random_eb = random.choice(eb)

	print(random_eb)

five_letters2()








#ubject_two_letters = ['夜', '海', '空', '昼', '石', '豆', '熊', '蝉']
#subject_three_letters = ['魚' , 'かもめ', '子猫', '雀'　, 'マグロ', 'つばめ']
#subject_four_letters = ['石橋'　,'なめくじ', 'うみうし' , 'かにかま', 'シマウマ', 'ウミガメ']


#predicate_one_letters = ['を', 'に', 'や', 'も', 'よ']
#predicate_two_letters = ['たち', 'の音'　, 'の目'　,]