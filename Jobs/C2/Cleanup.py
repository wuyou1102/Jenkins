# -*- encoding:UTF-8 -*-
from libs import Utility
import os

SOURCE_CODE_PATH = "/home/bspserver/sda/C2_SourceCode/"
DAILY_PATH = "/home/bspserver/sda/C2_DailyBuild/"


def run(*args, **kwargs):
    remove_empty_commit_history()


def remove_empty_commit_history():
    for f in os.listdir(DAILY_PATH):
        commit_history = os.path.join(DAILY_PATH, f, "ReleaseNotes.txt")
        if os.path.exists(commit_history):
            with open(commit_history) as r_file:
                print r_file.read()


def remove_oldest_version():
    while True:
        free, used, total = Utility.get_disk_usage(SOURCE_CODE_PATH)
        print "free:%s" % free
        print "used:%s" % used
        print "total:%s" % total
        if free < 500:
            print 'I will remove the ol'
        else:
            print 'Space is enough.'
