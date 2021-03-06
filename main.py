#!/usr/bin/python
# -*- coding: utf-8 -*-
# -*- coding: cp932 -*-

import re
import os
import sys
import glob
import shutil

from init.Init import INIT


def find_author_book(directory):
    result = {}

    # get author's name
    files = os.listdir(directory)
    authors = [f for f in files if os.path.isdir(os.path.join(directory, f))]

    # get author's book
    for author in authors:
        path = os.path.join(directory, author)
        files = os.listdir(path)
        result[author] = [f for f in files if os.path.isdir(os.path.join(path, f))]

    return result


def find_copied_dist(src_dirs, dist_dirs):
    result = {}
    for author in dist_dirs.keys():
        if author in src_dirs:
            src_set = set(src_dirs[author])
            dist_set = set(dist_dirs[author])
            nand_list = list(src_set - (src_set & dist_set))
            result[author] = nand_list
    return result



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
    copy_dest = find_author_book(setting['destination_place'])

    # get list of directories of copy source
    copy_src = find_author_book(setting['source_place'])

    # get list of directories to be copied
    result = find_copied_dist(copy_src, copy_dest)
    print(result)

    # copy

    print '\nFINISH!!\n'


if __name__ == "__main__":
    main()
    sys.exit()
