#coding=utf-8

import unittest
from HTMLTestRunner import HTMLTestRunner
import time

if __name__ == '__main__':
    suite = unittest.defaultTestLoader.discover('./test', pattern='test*.py')
    now_time = time.strftime("%Y_%m_%d_%H_%M_%S")
    filename = './report/' + now_time + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp)
    runner.run(suite)
    fp.close()
