# !/usr/bin/env python
# -*- coding: utf-8 -*-

# Python的hashlib提供了常见的摘要算法，如MD5，SHA1等等。

# 什么是摘要算法呢？摘要算法又称哈希算法、散列算法。它通过一个函数，把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）。

# 举个例子，你写了一篇文章，内容是一个字符串'how to use python hashlib - by Michael'，并附上这篇文章的摘要是'2d73d4f15c0db7f5ecb321b6a65e5d6d'。如果有人篡改了你的文章，并发表为'how to use python hashlib - by Bob'，你可以一下子指出Bob篡改了你的文章，因为根据'how to use python hashlib - by Bob'计算出的摘要不同于原始文章的摘要。

# 可见，摘要算法就是通过摘要函数f()对任意长度的数据data计算出固定长度的摘要digest，目的是为了发现原始数据是否被人篡改过。

# 摘要算法之所以能指出数据是否被篡改过，就是因为摘要函数是一个单向函数，计算f(data)很容易，但通过digest反推data却非常困难。而且，对原始数据做一个bit的修改，都会导致计算出的摘要完全不同。

# 我们以常见的摘要算法M;D5为例，计算出一个字符串的MD5值

import hashlib

md5 = hashlib.md5()
md5.update('hello world'.encode('utf-8'))
md5.update('hello buwenzheng'.encode('utf-8'))
print(md5.hexdigest())

sha1 = hashlib.sha1()
sha1.update('how to use sha1 in'.encode('utf-8'))
print(sha1.hexdigest())


# 根据用户输入的口令，计算出存储在数据库中的MD5口令:
def calc_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()


# 设计一个验证用户登录的函数，根据用户输入的口令是否正确，返回True或False：
db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}
def login(user, password):
    pwdMd5 = calc_md5(password)
    if db[user] and pwdMd5 == db[user]:
        return True
    else:
        return False
# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')


# 采用MD5存储口令是否就一定安全呢？也不一定。假设你是一个黑客，已经拿到了存储MD5口令的数据库，如何通过MD5反推用户的明文口令呢？暴力破解费事费力，真正的黑客不会这么干。

# 考虑这么个情况，很多用户喜欢用123456，888888，password这些简单的口令，于是，黑客可以事先计算出这些常用口令的MD5值，得到一个反推表：

# 'e10adc3949ba59abbe56e057f20f883e': '123456'
# '21218cca77804d2ba1922c33e0151105': '888888'
# '5f4dcc3b5aa765d61d8327deb882cf99': 'password'
# 这样，无需破解，只需要对比数据库的MD5，黑客就获得了使用常用口令的用户账号。

# 对于用户来讲，当然不要使用过于简单的口令。但是，我们能否在程序设计上对简单口令加强保护呢？

# 由于常用口令的MD5值很容易被计算出来，所以，要确保存储的用户口令不是那些已经被计算出来的常用口令的MD5，这一方法通过对原始口令加一个复杂字符串来实现，俗称“加盐”：

# def calc_md5(password):
#     return get_md5(password + 'the-Salt')
# 经过Salt处理的MD5口令，只要Salt不被黑客知道，即使用户输入简单口令，也很难通过MD5反推明文口令。

# 但是如果有两个用户都使用了相同的简单口令比如123456，在数据库中，将存储两条相同的MD5值，这说明这两个用户的口令是一样的。有没有办法让使用相同口令的用户存储不同的MD5呢？

# 如果假定用户无法修改登录名，就可以通过把登录名作为Salt的一部分来计算MD5，从而实现相同口令的用户也存储不同的MD5。

# 练习2 Look hashlib-practice1.py 