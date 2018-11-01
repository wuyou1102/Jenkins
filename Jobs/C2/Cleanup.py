# -*- encoding:UTF-8 -*-
from libs import Utility
import os

SOURCE_CODE_PATH = "/home/bspserver/sda/C2_SourceCode/"
DAILY_PATH = "/home/bspserver/sda/C2_DailyBuild/"


def run(*args, **kwargs):
    remove_empty_commit_history()
    remove_oldest_version()


def remove_empty_commit_history():
    for f in os.listdir(DAILY_PATH):
        commit_history = os.path.join(DAILY_PATH, f, "CommitHistory.txt")
        if os.path.exists(commit_history):
            with open(commit_history) as r_file:
                commit = r_file.read()
                if not commit:
                    remove_src_folder(f)


def remove_src_folder(folder_name):
    folder_path = os.path.join(SOURCE_CODE_PATH, folder_name)
    if os.path.exists(folder_path):
        print folder_path


def remove_oldest_version():
    while True:
        free, used, total = Utility.get_disk_usage(SOURCE_CODE_PATH)
        print "free:%s" % free
        print "used:%s" % used
        print "total:%s" % total
        if free < 500:
            f_list = os.listdir(SOURCE_CODE_PATH)
            f_list.sort()
            print f_list
        else:
            print 'Space is enough.'
