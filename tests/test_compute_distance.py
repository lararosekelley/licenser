from nose.tools import *
from tests import *
from licenser import licenser


def test_compute_distance_empty_str():
    '''
    tests compute_distance using one empty string
    '''

    a = ''
    b = 'hello'

    d = licenser.compute_distance(a, b)
    assert d is len(b)


def test_compute_distance():
    '''
    tests compute_distance using two non-empty strings
    '''

    a = 'palm tree'
    b = 'oak tree'

    d = licenser.compute_distance(a, b)
    assert d == 3
