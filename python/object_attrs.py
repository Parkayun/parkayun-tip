from __future__ import print_function


def print_attrs(obj):
    for attr in dir(obj):
        print('>', attr, ':', getattr(obj, attr))

