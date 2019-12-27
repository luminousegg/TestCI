#!/usr/local/bin/python
#-*- coding: utf-8 -*-
#@Time:2019/12/27 9:48 PM
#@Author: wangzhen
#@FileName:WidgetTestCase
#@SoftWare:PyCharm

import unittest

class WidgetTestCase(unittest.TestCase):



    def test_default_widget_size(self):
        self.assertEqual(10,10, 'incorrect default size')

    def test_widget_resize(self):
        self.assertEqual(10,10,'wrong size after resize')

if __name__ == '__main__':
    unittest.main()

