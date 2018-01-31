#!/usr/bin/python
# -*- coding: utf-8 -*-
# -*- coding: cp932 -*-

import re
import os
import sys
import glob
import shutil

from init.Init import INIT


class CleanFileName(object):
    """docstring for CleanFileName"""
    def __init__(self, f):
        super(CleanFileName, self).__init__()
        filename = self.getFileName(f)
        # file name
        self.zip = self.getTitle(filename)
        # auth name
        self.auth = self.getAuth(filename)

    def getFileName(self, f):
        fn = f.split('/')[-1]
        return fn

    def getTitle(self, f):
        try:
            title = f.strip()
            title = title.replace(u'【', '[')
            title = title.replace(u'】', ']')
            r = title.split(']')
            title = r[-1] if len(r)==2 else r[-2]
            title = title.split('(')[0]
            title = title.split('|')[0]
            title = title.split(u'│')[0]
            title = title.strip()
            if title[-4:] == '.zip':
                return title
            else:
                return title + '.zip'
        except:
            print 'error: getTitle'
            return f

    def getAuth(self, f):
        auth = f.split(']')
        if len(auth) == 1:
            return 'zip'
        else:
            auth = auth[0]
        auth = auth.split('[')[-1]
        auth = auth.split('(')[0]
        auth = auth.replace('.', '_')
        auth = auth.strip()
        return auth


# === MAIN ===
def main():
    # title call
    print ""
    print "\n--------------------\n"
    print "  Clean Manga Zip"
    print "\n--------------------\n"
    print ""

    # get place of URL list file
    setPlace = 'setting.json'
    while True:
        try:
            setting = INIT(setPlace).pref
            break
        except:
            setPlace = raw_input("Where setting.json? : ")
            setPlace = os.path.expanduser(setPlace)
    print ''

    # move zip files from ~/Downloads/
    reStr = setting['Downloads_place'] + '*.zip'
    zips = glob.glob(reStr)
    for x in zips:
        shutil.move(x, setting['Zip_place'])

    reStr = setting['Zip_place'] + '*.zip'
    zips = glob.glob(reStr)
    for x in zips:
        f = CleanFileName(x)
        # get Auth Name
        authName = f.auth
        # get filename
        fileName = f.zip
        # get path
        authDir = setting['Manga_place'] + authName + '/'
        # mkdir new dir
        try:
            os.makedirs(authDir)
        except OSError as e:
            if e.errno is 17:
                pass
        # move zip file
        try:
            shutil.move(x, authDir)
            # rename
            old = os.path.expanduser(authDir + x.split('/')[-1])
            new = os.path.expanduser(authDir + fileName)
            os.renames(old, new)
            print authName
        except OSError as e:
            if e.errno is 17:
                print 'remove : ' + x
                os.remove(x)
        except:
            pass

    print '\nClean Directorys...\n'
    dirs = glob.glob(setting['Manga_place'] + '*/')
    for i in dirs:
        if len(glob.glob(i + '*')) == 0:
            try:
                os.removedirs(i)
                print i
            except:
                pass
    print i

    print '\nFINISH!!\n'


if __name__ == "__main__":
    main()
    sys.exit()
