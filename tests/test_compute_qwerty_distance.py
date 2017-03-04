# -*- coding: utf-8 -*-

from licenser import licenser


def test_compute_qwerty_distance():
    '''
    calls compute_qwerty_distance to find the distance between characters on a
    keyboard
    '''

    expected_scores = [
        ('a', 'b', 26**0.5),
        ('x', 'x', 0),
        ('t', 'u', 2),
        ('1', '8', 7),
        ('r', 'k', 17**0.5)
    ]

    for item in expected_scores:
        c1 = item[0]
        c2 = item[1]
        expected = item[2]
        actual = licenser.compute_qwerty_distance(c1, c2)

        assert actual == expected, '{a} != {b}, test: {item}'.format(a=actual, b=expected, item=(c1, c2))
