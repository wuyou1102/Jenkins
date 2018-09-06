# -*- encoding:UTF-8 -*-
import os
from libs import Utility
import subprocess


def Repo_Init():
    cmd = Utility.Repo.init(url='ssh://youwu@gerrit.sensethink.cn:29418/manifest', branch='C2_8.1_master')
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE)
    try:
        while True:
            print p.stdout.readline()  # block/wait

    except Exception, e:
        print e.message


def Repo_Sync():
    cmd = Utility.Repo.sync(thread_num=8)
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE)
    try:
        while True:
            print p.stdout.readline()  # block/wait
    except Exception, e:
        print e.message


workspace_path = Utility.get_compiler_path()
Utility.create_folder(workspace_path)

os.chdir(workspace_path)
Repo_Init()
Repo_Sync()
