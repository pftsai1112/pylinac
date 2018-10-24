"""Test the entire package; an underscore precedes this file name
so it does not include itself in the test discovery."""
import os.path as osp
from test_basic import run_tests

import matplotlib


matplotlib.use('Agg')

test_dir = osp.join(osp.dirname(__file__), 'tests_complete')
run_tests(test_dir, pattern='_test_all*.py')