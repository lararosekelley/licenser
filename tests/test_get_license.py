# -*- coding: utf-8 -*-

from licenser import licenser


def test_get_licenses():
    '''
    calls get_license to test matching functionality
    '''

    expected_matches = [
        ('mit', 'mit'),
        ('mti', 'mit'),
        ('MIT', 'mit'),
        ('bit', 'mit'),
        ('nit', 'mit'),
        ('ics', 'isc'),
        ('isc', 'isc'),
        ('allrightsreserved', 'all-rights-reserved'),
        ('gpl2', 'gpl-2.0'),
        ('gpl-2', 'gpl-2.0'),
        ('apache', 'apache-2.0'),
        ('apache-2', 'apache-2.0'),
        ('mpl-2', 'mpl-2.0'),
        ('bsd2clause', 'bsd-2-clause'),
        ('agpl3', 'agpl-3.0'),
        ('agpl', 'agpl-3.0')
    ]

    for pair in expected_matches:
        match = licenser.get_license(pair[0])
        assert match == pair[1], '{a} != {b}, test: {pair}'.format(a=match, b=pair[1], pair=pair)
