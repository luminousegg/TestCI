#!/usr/local/bin/python
#-*- coding: utf-8 -*-
#@Time:2019/12/27 9:05 PM
#@Author: wangzhen
#@FileName:test_Case002
#@SoftWare:PyCharm
import unittest

class BaiduTest(unittest.TestCase):
    def setUp(self):
        self.number = 10
        self.number = int(self.number)

    def test_case1(self):
        #print(self.number)
        self.assertEqual(self.number, 10, msg='Your input is not 10')

    def test_case2(self):
        #print(self.number)

        self.assertEqual(self.number, 10, msg='Your input is not 20')

    def tearDown(self):
        print('Test over')

if __name__=='__main__':
    unittest.main()