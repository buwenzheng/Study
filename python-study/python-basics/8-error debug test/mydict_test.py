import unittest

from mydict import Dict

class TestDict(unittest.TestCase):
    # 测试初始化
    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)  #断言d.a 的值
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict)) # 测试d是否为dict类型(isinstance()返回的是否为True)

    # 测试key的设置
    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    # 测试属性的设置
    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d) # 检测'key'属性有没有设置上
        self.assertEqual(d['key'], 'value')

    # 没有该属性抛异常
    def test_keyerror(self):         
        d = Dict()
        with self.assertRaises(KeyError): # 通过d['empty']访问不存在的key时,希望抛出KeyError异常
            value = d['empty']

    # 没有该属性值抛异常
    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError): # 通过d.empty访问不存在的key时,希望抛出AttributeError异常
            value = d.empty        

    # 每段测试函数执行前执行的函数 
    def setUp(self):
        print('setUp')

    # 每段测试函数执行后执行的函数
    def tearDown(self):
        print('tearDown')    

# 开启测试
if __name__ == '__main__':           
    unittest.main()