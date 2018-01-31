#!/usr/bin/python
# -*- coding: utf-8 -*-
# -*- coding: cp932 -*-

import os
import sys
import json


# load setting.json
class LoadSetting(object):
    """docstring for LoadSetting"""
    def __init__(self, jsonFile):
        super(LoadSetting, self).__init__()
        self.setting = self.load(jsonFile)

    def load(self, jsonFile):
        # fix path
        jsonFile = os.path.expanduser(jsonFile)
        # open json file
        try:
            with open(jsonFile, 'r') as f:
                x = json.load(f)
        except:
            print u"設定ファイルが開けません"
            sys.exit()
        # fix paths
        for k, v in x.items():
            x[k] = os.path.expanduser(v)
        return x
