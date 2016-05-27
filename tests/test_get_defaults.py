from nose.tools import *
from tests import *
from licenser import licenser


def test_get_defaults():
    '''
    reads defaults from a .licenser file
    '''

    x = licenser.get_defaults(cwd + '/assets/.licenser')
    assert x.get('name') == 'n'
    assert x.get('email') == 'e'
    assert x.get('license') == 'unlicense'


def test_get_defaults_no_file():
    '''
    ensures an empty object is returned when file doesn't exist
    '''

    x = licenser.get_defaults('this does not exist')
    assert x == {}
