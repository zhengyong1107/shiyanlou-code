## 打印1-100的数字，不能是7的倍数，且不包含7的数字，每行打印一个数字
for a in range(1,101):
    if a % 7 == 0:        ## 判断是否7的倍数
        continue
    elif a % 10 == 7:     ## 判断个位数是否7
        continue
    elif a // 10 == 7:    ## 判断十位数是否7
        continue
    else:
        print(a)



