import os
import sys
import shutil
import unittest
from testbook import testbook
from gradescope_utils.autograder_utils.json_test_runner import JSONTestRunner
from gradescope_utils.autograder_utils.decorators import weight, number


class TestNotebook(unittest.TestCase):
# class TestNotebook(testbook):

    def setUp(self):
        pass

    @weight(1)
    @number("1.1")
    def test_task_1_1(self):
        with testbook('/autograder/source/notebook.ipynb', execute=True) as tb:
            task_1_1 = tb.ref("task_1_1")
            print("*********** Hello ***************")
            assert task_1_1() == 0
    
    # def test_eval_add(self):
    #     """Evaluate 1 + 1"""
    #     val = self.calc.eval("1 + 1")
    #     self.assertEqual(val, 2)

    # @weight(1)
    # @number("1.2")
    # def test_eval_sub(self):
    #     """Evaluate 2 - 1"""
    #     val = self.calc.eval("2 - 1")
    #     self.assertEqual(val, 1)

    # @weight(1)
    # @number("1.3")
    # def test_eval_mul(self):
    #     """Evaluate 4 * 8"""
    #     val = self.calc.eval("4 * 8")
    #     self.assertEqual(val, 32)

    # @weight(1)
    # @number("1.4")
    # def test_eval_div(self):
    #     """Evaluate 8/4"""
    #     val = self.calc.eval("8 / 4")
    #     self.assertEqual(val, 2)

    # @weight(2)
    # @number("1.5")
    # def test_eval_whitespace(self):
    #     """Evaluate 1+1 (no whitespace)"""
    #     val = self.calc.eval("1+1")
    #     self.assertEqual(val, 2)
