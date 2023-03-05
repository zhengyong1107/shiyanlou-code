## 写代码要求：打印1到100之间，不是7的倍数，切不包含7的数字，每行打印一个数字

a = 0
while a < 100:
    a += 1
    if a % 7 == 0 or a % 10 == 7 or a // 10 == 7:
        continue
    else:
        print(a)


