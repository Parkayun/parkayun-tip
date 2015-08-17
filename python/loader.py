# -*- coding:utf-8 -*-
import sys
import time


def load():
    """Inspired by https://github.com/sindresorhus/elegant-spinner"""
    while True:
        for x in ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']:
            sys.stdout.write(''.join(('\r', x)))
            sys.stdout.flush()
            time.sleep(0.1)

load()
