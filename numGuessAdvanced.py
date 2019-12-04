'''
@describe:猜数游戏
n位数，位置与数字都正确为A，数字正确，位置不正确记为B
@author:xmulsm
@date:2019-12-3
'''

import random


def generateNum(bits=4):
    '''
    生成数字互不相同的n位数，n由传入参数bits确定
    首位数从1-9，其它位数从0-9
    @params:num_list  n位数结果，类型list
    '''
    num_list = []
    num_set = set()
    firstbit = random.randint(1, 9)  # 首位数不能为0
    num_list.append(firstbit)
    num_set.add(firstbit)
    while True:
        other = random.randint(0, 9)  # 其它位数0-9
        num_set.add(other)
        if len(num_list) >= bits:
            break
        else:
            if len(num_set) == len(num_list):  # num_set与num_list长度一样，表示新生成的数与原来的重复
                continue
            else:
                num_list.append(other)
    return num_list


def judgeNum(cp_num, user_num):
    '''
    判断用户输入正确数字个数
    @params:cp_num 计算机生成的4位随机整数,转换成list类型
    @params:user_num 用户输入的4位整数
    @params:count_A,count_B  返回结果
    '''
    cp_num = list(cp_num)
    user_num = list(user_num)
    count_A = 0  # 位置、数字全部正确的个数
    count_B = 0  # 数字正确、位置不正确的个数
    for i in range(len(cp_num)):
        if cp_num[i] == int(user_num[i]):
            count_A += 1
        else:
            if int(user_num[i]) in cp_num:
                count_B += 1
    return count_A, count_B


if __name__ == '__main__':
    res = generateNum(bits=4)  # 计算机生成一个4位不同的整数
    # print(res)
    num_len = len(res)  # 生成随机整数的位数
    count = 0  # 猜数次数
    while True:
        your_num = input("请输入一个{}位不同整数：".format(num_len))
        if len(set(list(your_num))) != num_len:
            print('您输入的4位数字非法，请重新输入！')
            continue
        count += 1
        count_a, count_b = judgeNum(cp_num=res, user_num=your_num)
        print('你共猜了{}次，结果{}A{}B'.format(count, count_a, count_b))
        if count_a == num_len:
            print('恭喜您，全部猜对！您共猜了{}次'.format(count))
            break
