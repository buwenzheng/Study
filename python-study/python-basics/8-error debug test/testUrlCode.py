from urllib.request import urlopen
import unittest

class TestUrlHttpcode(unittest.TestCase):

    def setUp(self):
        urlinfo = ['http://www.baidu.com','http://www.163.com','http://www.sohu.com','http://www.cnpythoner.com', 'https://www.google.com']
        self.checkurl = urlinfo

    def test_ok(self):    
        for m in self.checkurl:
            httpcode = urlopen(m).getcode()
            self.assertEqual(httpcode, 200)

if __name__ == '__main__':
    unittest.main()            
