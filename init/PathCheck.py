#!/usr/bin/python
# -*- coding: utf-8 -*-
# -*- coding: cp932 -*-

import os


class CheckDirectory(object):
    """docstring for CheckDirectory"""
    def __init__(self, checklist):
        super(CheckDirectory, self).__init__()
        self.check(checklist)

    def check(self, checklist):
        for x in checklist:
            self.exit_creat(x)

    # === Check Directories of saveing data ===
    def exit_creat(self, dir_name):
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
            print dir_name + " created."
        else:
            print dir_name + " is exit."
