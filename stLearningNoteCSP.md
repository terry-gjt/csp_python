# list
```python
names=['Lihua','Rain','Jack','Xiuxiu','Peiqi','Black']
names2=['gfdg','fgd']
print(names[1:-2])          #使用方括号的形式截取字符
names.insert(5, 'Blue')     #指定位置插入，位置从0开始
names.append('Google')      ## 使用 append() 添加元素
del names[2]                #del 语句来删除列表的元素
len(names)       #列表元素个数
max(names)       #返回列表元素最大值
min(names)       #返回列表元素最小值
names.count('Rain')  #统计某个元素在列表中出现的次数
names.extend(names2) #在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
names.index('Rain')  #从列表中找出某个值第一个匹配项的索引位置
names.pop(2) #移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
names.remove('Rain')#移除列表中某个值的第一个匹配项
names.reverse()#反向列表中元素
#对原列表进行排序,reverse为True时为降序# 获取列表的第二个元素，cmp -- 可选参数,一般不需要
names.sort(cmp=None, key=None, reverse=False)
def takeSecond(elem):
    return elem[1]
random = [(2, 2), (3, 4), (4, 1), (1, 3)]
# 指定第二个元素排序
random.sort(key=takeSecond)
```
# dict
```python
# d = {key1 : value1, key2 : value2 } 
# 值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。
dict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
dict.clear()    #删除字典内所有元素
dict.copy()     #返回一个字典的浅复制
dict.get(key, default=None)     #返回指定键的值，如果值不在字典中返回default值
dict.has_key(key)       #如果键在字典dict里返回true，否则返回false
dict.items()            #以列表返回可遍历的(键, 值) 元组数组
dict.keys()             #以列表返回一个字典所有的键
dict.setdefault(key, default=None)      #和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
dict.update(dict2)                       #把字典dict2的键/值对更新到dict里
dict.values()                            #以列表返回字典中的所有值
dict.pop(key[,default])                  #删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
dict.popitem()                           #返回并删除字典中的最后一对键和值。
#遍历所有的键-值对
for k,v in dict.items(): pass
#遍历dict，以下两种方法一样
for k in dict.keys():pass
for k in dict:pass
#遍历dict的值
for v in dict.values():pass
```
# 可能用到的语法
## 1 for-else
```python
for i in list[1,2,34,5]:
    pass
else:pass #正常结束循环不会执行，提前break才会执行
```
## 2输入一行整数，存为list
```python
nums=list(map(int,input().split()))
nums1 = list(set(nums))#去重复值
```
## 3 数的n次方
```python
i = pow(2, 4)#2的4次方
i2=2**4     #也是2的4次方
print(i,'----',i2)
```
## 4匿名函数排序
```python
lis=[{'name':'Taobao','age':100},{'name':'Runoob','age':7},{'name':'Google','age':100},{'name':'Wiki','age':200}]
l1 = sorted(lis,key=lambda x:x['age'])
```




