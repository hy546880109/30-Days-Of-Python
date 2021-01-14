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

# Map函数

# num = [x for x in range(6)]
# def square(x):
#     return x**2
# num_square = map(square, num)
# print(list(num_square))

# nums = map(lambda x:x**2,num)
# print(list(nums))
        

#