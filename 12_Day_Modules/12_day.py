#1.写入一个生成六位数字/字符 random _ user _ id 的函数
# import random,string

# def random_user_id(num):
#     spells = string.ascii_letters
#     numbers = string.digits
#     r = ''
#     for i in range(num):
#         ran = random.choice(spells + numbers)
#         r += ran
#     return r



#2.声明一个名为 user _ id _ gen _ by _ user 的函数。它不接受任何参数，但是使用 input ()接受两个输入。
# 其中一个输入是字符数，第二个输入是假定要生成的 id 数
# import random,string

# def user_id_gen_by_user():
#     num = input('输入生成的个数:')
#     spe = input('输入字符个数:')
#     spells = string.ascii_letters   #声明一个变量为字符abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
#     numbers = string.digits         #声明一个变量为0123456789
#     r = ''
#     for n in range(int(num)):
#         for i in range(int(spe)):
#             ran = random.choice(spells + numbers)
#             r += ran
#         r += '\t' 
#     return r
# print(user_id_gen_by_user())



#3.编写一个名为rgb color gen的函数，它将生成rgb颜色(3个值，每个值从0到255)。
# import random

# def rgb_color_gen():
#     rgb = random.sample(range(0, 255), 3)
#     r = 'rgb'+ str(tuple(rgb))
#     return r

# print(rgb_color_gen())



#4.写一个函数list_of _ hexa _ colors，它返回数组中任意数量的十六进制颜色(在 # 后面写六个十六进制数字)。
# 十六进制数字系统由16个符号、0-9和字母表的前6个字母 a-f 组成。检查任务6的输出示例)
# import random,string

# def list_of_hexa_colors():
#     spells = string.ascii_letters
#     numbers = string.digits
#     ran = random.sample((spells + numbers),6)
#     r = '#' + ''.join(ran)
#     return r

# print(list_of_hexa_colors())


#5.编写一个函数，它返回0-9范围内的7个随机数的数组。所有的数字必须是唯一的

import random

def func():
    su = random.sample(range(10),7)
    return su

print(func())