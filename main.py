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
    result = {}

    # get author's name
    files = os.listdir(directory)
    authors = [f for f in files if os.path.isdir(os.path.join(directory, f))]

    # get author's book
    for author in authors:
        path = os.path.join(directory, author)
        files = os.listdir(path)
        result[author] = [f for f in files if os.path.isdir(os.path.join(path, f))]

    print(result)



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
