# 序列化
# 在程序运行的过程中，所有的变量都是在内存中，比如，定义一个dict：
# d = dict(name='Bob', age=20, score=88)
# 可以随时修改变量，比如把name改成'Bill'，但是一旦程序结束，变量所占用的内存就被操作系统全部回收。如果没有把修改后的'Bill'存储到磁盘上，下次重新运行程序，变量又被初始化为'Bob'。
# 我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思。
# 序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。
# 反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。
# Python提供了pickle模块来实现序列化。

# 首先，我们尝试把一个对象序列化并写入文件：
import pickle

d = dict(name='bod', age=20, score=20)
s = pickle.dumps(d)
# print(s)
# 输出序列化之后的dict
# b'\x80\x03}q\x00(X\x03\x00\x00\x00ageq\x01K\x14X\x05\x00\x00\x00scoreq\x02KXX\x04\x00\x00\x00nameq\x03X\x03\x00\x00\x00Bobq\x04u.'

# pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。或者用另一个方法pickle.dump()直接把对象序列化之后写入一个file-like Object:

f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()
# 看看写入的dump.txt文件，一堆乱七八糟的内容，这些都是Python保存的对象内部信息。

# 当我们要把对象从磁盘读到内存时，可以先把内容读到一个bytes，然后用pickle.loads()方法反序列化出对象，也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象。我们打开另一个Python命令行来反序列化刚才保存的对象：

f1 = open('dump.txt', 'rb')
d = pickle.load(f1)
f.close()
# print(d)

# JSON
# python对象转json
import json
d1 = dict(name='bwz', age=23)
d2 = json.dumps(d1)

# json反序列化为Python对象
js_str = '{"name": "bwz", "sex": "male"}'
js_dict = json.loads(js_str)
# print(js_dict)


# JSON进阶
# Python的dict对象可以直接序列化为JSON的{}，不过，很多时候，我们更喜欢用class表示对象，比如定义Student类，然后序列化

class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 将Student类转换成dict 
def studentDict(std):
    return {
        'name': std.name,
        'age': std.age
    }
s = Student('buwenzheng', 22)        

# s1 = json.dumps(s, default=studentDict)
# 或者
s1 = json.dumps(s, default=lambda obj: obj.__dict__)
print('s1', type(s.__dict__))

# json.dumps()的ensure_ascii参数，是否将中文转换成ascii码
obj = dict(name='你好', age=12)
s = json.dumps(obj, ensure_ascii=True)
print(s)

# 小结
# Python语言特定的序列化模块是pickle，但如果要把序列化搞得更通用、更符合Web标准，就可以使用json模块。

# json模块的dumps()和loads()函数是定义得非常好的接口的典范。当我们使用时，只需要传入一个必须的参数。但是，当默认的序列化或反序列机制不满足我们的要求时，我们又可以传入更多的参数来定制序列化或反序列化的规则，既做到了接口简单易用，又做到了充分的扩展性和灵活性