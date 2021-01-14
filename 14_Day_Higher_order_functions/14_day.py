# 闭包：一个函数封装并返回它内部的另一个函数
# def ten_add():
#     ten = 10
#     def add(num):
#         ten = 3
#         return num + ten
#     return add

# print(ten_add()(3))

# 装饰器
# 装饰器的原型：
# def big_message(func):
#     def warpper():
#         f = func()
#         t = f.title()
#         return t
#     return warpper

# def get_message():
#     return 'hello,world!'

# print(big_message(get_message)())

# 装饰器@的进阶
# import time
# def big_message(func):
#     def warpper():
#         f = func()
#         t = f.title()
#         print(t)
#         return t
#     return warpper

# def len_message(func):
#     def warpper():
#         f = func()
#         t = len(f)
#         print(t)
#         return t
#     return warpper

# def time_message(func):
#     def warpper():
#         t = time.time()
#         f = func()
#         t1 = time.time()
#         run_time = t1 - t
#         # print(run_time)
#         return run_time
#     return warpper

# @time_message
# @len_message
# @big_message
# def get_message():
#     print('hello,world!')
#     return 'hello,world!'

# print(get_message())

# Map函数:对可迭代器或者序列中的每个元素进行相同的操作（例如每个元素+1等等），并返回迭代器或者列表
# 示例1
# num = [x for x in range(6)]
# # def square(x):
# #     return x**2
# # num_square = map(square, num)
# # print(list(num_square))
# #示例2
# # nums = map(lambda x:x**2,num)
# # print(list(nums))
# #示例3
# number = map(str,num)
# print(list(number))
# #示例4
# lang = ['python','java','javascript']
# li = map(lambda x: x.title(), lang)
# print(list(li))

# Filter函数：对可迭代对象中的元素按照特定的条件进行筛选（例如筛选列表中所有的偶数等等）

# num = [x for x in range(6)]
# # def is_even(n):
# #     if n % 2 == 0:
# #         return True
# #     return False

# # even_num = filter(is_even,num)
# # print(list(even_num))

# ll = filter(lambda x : x % 2 == 0, num)
# print(list(ll))

# Reduce函数：Reduce ()函数是在 functools 模块中定义的，我们应该从这个模块导入它。像 map 和 filter 一样，它需要两个参数，一个函数和一个迭代。
# 但是，它不返回另一个可迭代的值，而是返回单个值。
# from functools import reduce
# num = [1,2,3,4,5]
# def add(x,y):
#     return x + y

# total = reduce(add, num)
# print(total)

# t = reduce(lambda x,y : x + y, num)
# print(t)

# 练习
import json
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 1、解释 map、 filter 和 reduce 之间的区别？
# 答：
# 1、map函数对可迭代的数组通过一个函数遍历执行数组中的每个元素生成新的生成器
# 2、filter函数对可迭代的数组通过一个判断条件对每个元素进行判断筛选出新的生成器
# 3、reduce函数对可迭代的数组中的每两个元素执行一个函数方法最后返回出单个值

# 2、解释高阶函数、闭包和装饰器之间的区别？
# 答：
# 1、高阶函数是函数传递的参数是函数，也可把函数做为返回值
# 2、闭包实际是高阶函数，但是它存在多个函数的嵌套关系，内部函数引用外部函数的变量，外部函数返回内部函数的函数名称
# 3、装饰器等于高阶函数+闭包，它是在不修改原函数的基础上添加新的功能。

# 3、使用 map 创建新列表，方法是将每个国家在 countries 列表中更改为大写
# country = map(lambda name:name.upper(), countries)
# print(list(country))

# 4、使用 map 创建一个新列表，方法是将每个数字更改为数字列表中它的平方
# number = map(lambda x:x**2,numbers)
# print(list(number))

# 5、使用过滤器过滤掉包含“land”的国家。

# country = filter(lambda name: 'land' not in name, countries)
# print(list(country))

# 6、使用过滤器过滤出正好有六个字符的国家。
# country = filter(lambda name: len(name) == 6, countries)
# print(list(country))

# 7、使用 filter 过滤掉国家列表中包含六个或更多字母的国家。
# country = filter(lambda name: len(name) >= 6, countries)
# print(list(country))

# 8、使用过滤器过滤掉以 E 开头的国家
# country = filter(lambda name: name.startswith('E'), countries)
# print(list(country))

# 9、使用 reduce 对数字列表中的所有数字求和。
# from functools import reduce
# num = reduce(lambda x, y: x + y, numbers)
# print(num)

# 10、使用 reduce 连接所有国家并生成以下句子:
# Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
# from functools import reduce
# person = reduce(lambda x,y : str(x) + ',' + str(y), countries)
# print(person+', and Iceland are north European countries')

# 11、创建一个返回字典的函数，其中 keys 表示国家的起始字母，而 value 表示以该字母开始的国家名称的数量。


def country_dict():
    pass


# 12、使用 countries _ data.py ( https://github.com/asabeneh/30-days-of-python/blob/master/data/countries-data.py )文件并执行以下任务:
# 按国名、资本、人口对国家进行排序
# 根据地理位置选出十种最常被使用的语言
# 选出人口最多的十个国家
f = open(r'C:\Users\Administrator\Desktop\learn\30-Days-Of-Python\data\countries-data.py',
         'r', encoding='utf8')
file = f.read()
js = json.loads(file)
l = []
for i in range(len(js)):
    # print(js[i]['name'])
    # l.append(js[i]['name'])
    l.append(js[i]['population'])
l.sort()
print(l)

f.close()
