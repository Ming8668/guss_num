# 產生一個隨機整數1~100 (不要印出來)
# 讓使用者重複輸入數字去猜
# 猜對的話 印出"猜對了!!"
# 猜錯的話 要印出 比答案大/小
# 延伸:猜數了第幾次

import random
r = random.randint(0,100)
# print(r)
count = 0

while True:
	num = input("請輸入數字:")
	num = int(num)
	count += 1

	if num == r:
		print("猜對了!!")
		print("這是您猜了第", count, "次")
		break
	elif num > r:
		print("比答案大")
	elif num < r:
		print("比答案小")
	print("ps.您已猜了", count, "次")
