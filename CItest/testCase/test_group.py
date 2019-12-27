#!/usr/local/bin/python
#-*- coding: utf-8 -*-
#@Time:2019/12/27 9:11 PM
#@Author: wangzhen
#@FileName:test_group
#@SoftWare:PyCharm
import unittest
from CItest.testCase import test_baidu
from CItest.testCase import WidgetTestCase
def suite():
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase('test_default_widget_size'))
    suite.addTest(WidgetTestCase('test_widget_resize'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())