**Making Gradescope autograder assignments work with Jupyter Notebooks **

Here's what I have to far, you can take the zip (which *should* be a zip of the current version of the code) and upload it to Gradescope in the Configure Autograder screen. 

Take the notebook separately and submit it.

This works with the testbook library, the main code that makes this work is in the actual test file:

```python
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
        with testbook('/autograder/source/notebook.ipynb', execute=False) as tb:
            task_1_1 = tb.ref("task_1_1")
            print("*********** Hello ***************")
            assert task_1_1() == 1
```

Note, we're not using the testbook decorator, we're using the `with` statement. The decorator seems to interfere with the Gradescope decorators.

LIMITATIONS:

- Currently, to load the functions to be tested, testbook runs the entire notebook
- This means anything outside of function defintitions will be run and the output will go to the Gradescope progress screen
- This is largely untested, I've just gotten one simple function to work