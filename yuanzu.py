
'''
#直接赋值与浅拷贝 深拷贝

dict1={'name':('jack','mike'),'age':(12,23),'from':('china','african')}
dict2=dict1
dict3=dict1.copy()
print(dict1)
print(dict2)
print(dict3)
dict1['name']='fan'
print(dict1)#原来的jack mike被新给的'fan'覆盖了
print(dict2)#直接赋值的dict2的值也被改变了
print(dict3)#浅拷贝的值还是原来的值 没有改变
'''
'''
import copy
a=[1,2,3]
b=a#直接赋值
c=a.copy()
d=copy.deepcopy(a)

a.append(4)
print(a)
print(b)#直接赋值和原始列表变了
print(c)
print(d)#浅拷贝 和深拷贝都木有变
'''
'''
import copy#用深拷贝需要使用copy模块
a=[1,2,3,['a','b']]
b=a#直接赋值
c=a.copy()#浅拷贝
d=copy.deepcopy(a)#深拷贝

a[3].append('c')
a.remove(2)
print(a)
print(b)#直接赋值和原函数一起同步改变
print(c)#浅拷贝的子对象''['a','b']''改变了
print(d)#深拷贝不受影响和原来的a一样
'''


'''
a=[1,3,4,[1,2,3,4],'c']

#如何向子对象中加入元素？？？


#list中可以添加元素的函数

a.append(5)
#append用于在列表末尾 只接受一个参数 参数可以是任何数据类型，被追加的元素在List中保持着原结构类型。
print(a)

a.insert(3,5)
#insert相比较append可以指定位置插入元素在列表中
print(a)

b=['a','b']
a.extend(b)#将一个列表中每个元素分别添加到另一个列表中，只接受一个参数。
print(a)
'''

a=[1,3,4,[1,2,3,4],'c']
#可以删除List中元素的函数
#pop 和del 除格式有啥不同
'''
a.remove([1,2,3,4])
#remove函数是可以指定删除存在list中的元素 没有指定元素会报错
print(a)

del a[3]
print(a)
#del 是靠位置删除元素的  与remove指定不同

a.pop()
print(a)
#pop()默认弹走最后一个数，和del一样靠索引弹元素

'''