'''
@describe:猜数游戏,提示大小
@author:xmulsm
@date:2019-12-3
'''
import random

ran = random.randint(0, 100)  # 计算机生成一个0-100的随机数
maxNum = 6  # 最大猜数次数
count = 0  # 猜数计数
while True:
    if count >= maxNum:
        print('您的次数已经用完了，挑战失败！')
        break
    else:
        your_num = int(input('请输入一个0-100的整数：'))
        count += 1
        if your_num == ran:
            print('恭喜你，猜对了！您共猜了{}次'.format(count))
            break
        elif your_num > ran:
            print('您猜的数大了，您还剩{}次，请重新输入。'.format(maxNum - count))
            continue
        elif your_num < ran:
            print('您猜的数小了，您还剩{}次，请重新输入。'.format(maxNum - count))
            continue
