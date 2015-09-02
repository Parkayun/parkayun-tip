from __future__ import print_function


def run_attr(obj):
    for attr in dir(obj):
        print('>', attr, ':', end=" ")
        obj_attr = getattr(obj, attr)
        if hasattr(obj_attr, '__call__'):
            print('method')
        else:
            print(obj_attr)

