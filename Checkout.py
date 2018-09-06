# -*- encoding:UTF-8 -*-
import os
from libs import Utility
import subprocess


def PrintOutput(cmd):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE, shell=True)
    try:
        for line in iter(p.stdout.readline, b''):
            print line.rstrip()
    except Exception, e:
        print e.message


workspace_path = Utility.get_compiler_path()
Utility.create_folder(workspace_path)

os.chdir(workspace_path)
PrintOutput(Utility.Repo.init(url='ssh://youwu@gerrit.sensethink.cn:29418/manifest', branch='C2_8.1_master'))
PrintOutput(Utility.Repo.sync(thread_num=8))
