# -*- encoding:UTF-8 -*-
import os
from libs import Environment as Env
from libs import Utility
import shutil
import JobFunc

src_folder = os.path.join(JobFunc.PATH_SOURCE_CODE, '9201')
output_folder = os.path.join(JobFunc.PATH_SOURCE_CODE, "9201", "output", "image")


def run(*args, **kwargs):
    Utility.print_info(__file__, args, kwargs)
    version_type = args[2]
    if version_type == "P0":
        deploy_p0()
    elif version_type == "P1":
        deploy_p1()
    else:
        JobFunc.RaiseException(KeyError, "Unknown version type:%s" % version_type)


def deploy_p0():
    copy_image("P0")


def deploy_p1():
    copy_image("P1")


def copy_image(_type):
    u_disk1 = 'artosyn-upgrade-B2%sU.' % _type
    u_disk2 = 'B2%sU.' % _type
    full = 'B2%sF.' % _type
    dst_folder = Utility.create_folder(os.path.join(JobFunc.PATH_DAILY_BUILD, Env.BUILD_TIMESTAMP))
    for f in os.listdir(output_folder):
        if f.startswith(full):
            shutil.copy(src=os.path.join(output_folder, f), dst=os.path.join(dst_folder, "B2%sF.img" % _type))
        elif f.startswith(u_disk1) or f.startswith(u_disk2):
            shutil.copy(src=os.path.join(output_folder, f), dst=os.path.join(dst_folder, "B2%sU.img" % _type))
        else:
            print "wuyou debug:->%s" % f
    create_commit_history(deploy_path=dst_folder)


def create_commit_history(deploy_path):
    commit_history = os.path.join(deploy_path, "CommitHistory.txt")
    print "wuyou debug:-> %s" % commit_history
    if not os.path.exists(commit_history):
        print "wuyou debug:-> not exists commit history"
        os.chdir(src_folder)
        output = os.popen('git log --since=1.day').read()
        print "wuyou debug:-> %s" % output
        with open(commit_history, "w") as wfile:
            wfile.write(str(output))
