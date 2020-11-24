# test_to_run.py
# coding=utf-8
import unittest


class TestToRun(unittest.TestCase):
    def setUp(self):
        pass
        # 这里写setUp的方法，通常是打开浏览器

    @unittest.skipIf(2 > 1, '如果为真则不执行')
    def testAssertNotEqual(self):
        self.assertEqual(1, 2)
        # 这里写具体的search方法

    @unittest.expectedFailure
    def testAssertEqual(self):
        print(1)
        self.assertEqual(1, 1)
        # 这里写具体的search方法

    def tearDown(self):
        pass
        # tearDown方法，测试后的清理工具，比如对测试产生的数据进
