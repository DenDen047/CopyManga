#!/usr/bin/python
# -*- coding: utf-8 -*-
# -*- coding: cp932 -*-

import re
import os
import sys
import glob
import shutil

from init.Init import INIT


def find_all_files(directory):
    # for root, dirs, files in os.walk(directory):
    #     yield root
    #     for file in files:
    #         yield os.path.join(root, file)
    for root, dirs, files in os.walk(directory):
        print(root, dirs, files)


# === MAIN ===
def main():
    # title call
    print("")
    print("\n--------------------\n")
    print("  Copy Manga")
    print("\n--------------------\n")
    print("")

    # get place of manga
    setPlace = 'setting.json'
    while True:
        try:
            setting = INIT(setPlace).pref
            break
        except:
            setPlace = raw_input("Where setting.json? : ")
            setPlace = os.path.expanduser(setPlace)
    print('')

    # get list of directories of copy destination
    find_all_files(setting['destination_place'])

    # get list of directories of copy source

    # get list of directories to be copied

    # copy

    print '\nFINISH!!\n'


if __name__ == "__main__":
    main()
    sys.exit()
