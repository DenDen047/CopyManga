#!/usr/bin/python
# -*- coding: utf-8 -*-
# -*- coding: cp932 -*-

import LoadFiles
import PathCheck


class INIT(object):
    """docstring for INIT"""
    def __init__(self, setting):
        super(INIT, self).__init__()
        # value
        self.pref = None
        # get value
        self.getSetting(setting)
        self.checkDirs(self.pref)

    def getSetting(self, setting):
        self.pref = LoadFiles.LoadSetting(setting).setting

    def checkDirs(self, mixDict):
        # get dirs
        dirs = []
        for k, v in mixDict.items():
            if v[-1] == '/':
                dirs += [v]
        # check dirs
        PathCheck.CheckDirectory(dirs)
