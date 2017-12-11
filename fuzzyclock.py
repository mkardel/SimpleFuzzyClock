"""
Copyright Matthias Kardel 2017-12-10
"""

import time


class FuzzyClock(object):
    def __init__(self, t=time.localtime()):
        self.h = 0
        self.m = 0
        self.update(t)
        self.hours = ['twölf', 'een', 'twee', 'dree', 'veer', 'fief', 'söß', 'söben',
                      'acht', 'negen', 'tein', 'ölben', 'twölf']

    def get_time(self):
        return self._get_prefix() + " " + self._get_suffix()

    def _get_prefix(self):
        if self.m < 4:
            return ""
        elif self.m < 8:
            return "kort no"
        elif self.m < 13:
            return "tein no"
        elif self.m < 18:
            return "viddel no"
        elif self.m < 23:
            return "twintig no"

        self.h += 1
        if self.m < 28:
            return "kort vör halv"
        elif self.m < 32:
            return "halv"
        elif self.m < 37:
            return "kort no halv"
        elif self.m < 42:
            return "twintig vör"
        elif self.m < 47:
            return "viddel vör"
        elif self.m < 52:
            return "tein vör"
        elif self.m < 57:
            return "kort vör"

        return ""

    def _get_suffix(self):
        return self.hours[self.h]

    def update(self, t=None):
        if t is None:
            t = time.localtime()

        self.h = t.tm_hour % 12
        self.m = t.tm_min
