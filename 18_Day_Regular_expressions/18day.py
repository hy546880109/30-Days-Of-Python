#练习
# 1.下一段中最常用的词是什么？
#  paragraph = 'I love teaching. If you do not love teaching what else can you love. 
#  I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.


paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
ll = paragraph.replace('.','')  #删除为.得字符
l = ll.split(' ')   #通过空格进行分割也就是将空格换成,号
# print(list(l))
new_dict = {}
for i in list(l):
    new_dict[i] = list(l).count(i)  #创建字典里得键值对
print(sorted(new_dict.items(), key = lambda kv:(kv[1], kv[0]), reverse=True))   #按照value进行降序排序

# 2. 某些粒子在水平 x 轴 -12,-4,-3和-1上的位置为负方向，0在原点，4和8在正方向。从整篇文章中提取这些数字，找出最远的两个粒子之间的距离
# text = The position of some particles on the horizontal x-axis -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. 
# Extract these numbers from this whole text and find the distance between the two furthest particles.





