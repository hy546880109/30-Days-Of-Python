# 1.使用列表内涵过滤器只过滤列表中的负数和零
# numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

# numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
# x = [x for x in numbers if x>0]
# print(x)

# 2.将以下列表展开成一维列表:
# list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
# list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

# l = [num for r in list_of_lists for num in r]
# s = [num for r in l for num in r]
# print(l)
# print(s)

# 3.使用列表内涵创建如下元组列表:
# [(0, 1, 0, 0, 0, 0, 0),
# (1, 1, 1, 1, 1, 1, 1),
# (2, 1, 2, 4, 8, 16, 32),
# (3, 1, 3, 9, 27, 81, 243),
# (4, 1, 4, 16, 64, 256, 1024),
# (5, 1, 5, 25, 125, 625, 3125),
# (6, 1, 6, 36, 216, 1296, 7776),
# (7, 1, 7, 49, 343, 2401, 16807),
# (8, 1, 8, 64, 512, 4096, 32768),
# (9, 1, 9, 81, 729, 6561, 59049),
# (10, 1, 10, 100, 1000, 10000, 100000)]

# s = [(i,1,i,i**2,i*i**2,i**4,i**2*i*i**2) for i in range(11)]
# print(s)

# 4.将以下列表合并为一个新列表:
# countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# output:
# ['FINLAND', 'HELSINKI', 'SWEDEN', 'STOCKHOLM', 'NORWAY', 'OSLO']

# countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

# l = []
# for i in countries:
#     # print(i)
#     for n in i:
#         # print(n)    
#         for m in n:
#             # print(m)
#             l.append(m)
# print(l)

# ls = [num for i in countries for num in i]
# print(num)
# ll = [num for i in ls for num in i]
# print(ll)

# 5.将以下列表更改为字典列表:
# countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# output:
# [{'country': 'FINLAND', 'city': 'HELSINKI'},
# {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
# {'country': 'NORWAY', 'city': 'OSLO'}]

# ll = []
# countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# country = ['country','city']
# ls = [num for i in countries for num in i]
# for i in ls:
#     x = dict(zip(country, i))
#     ll.append(x)
# print(ll)



# 6.将以下列表更改为串联字符串列表:
# names = [[('Asabeneh', 'Yetaeyeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
# output
# ['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']

names = [[('Asabeneh', 'Yetaeyeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

ls = [num for i in names for num in i]
kk = []
for num in ls:
    ss = ' '.join(num)
    kk.append(ss)
print(kk)

