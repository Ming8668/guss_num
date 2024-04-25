# 產生一個隨機整數1~100 (不要印出來)
# 讓使用者重複輸入數字去猜
# 猜對的話 印出"猜對了!!"
# 猜錯的話 要印出 比答案大/小

import random
r = random.randint(0,100)
# print(r)

while True:
	num = input("請輸入數字:")
	num = int(num)

	if num == r:
		print("猜對了!!")
		break
	elif num > r:
		print("比答案大")
	elif num < r:
		print("比答案小")
	