#!/usr/local/bin/python
#-*- coding: utf-8 -*-
#@Time:2019/12/27 9:52 PM
#@Author: wangzhen
#@FileName:suite
#@SoftWare:PyCharm
import unittest

from CItest.testCase import WidgetTestCase


def suite():
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase.WidgetTestCase('test_default_widget_size'))
    suite.addTest(WidgetTestCase.WidgetTestCase('test_widget_resize'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())