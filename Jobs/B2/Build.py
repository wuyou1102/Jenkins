# -*- encoding:UTF-8 -*-
from libs import Utility
import os
import JobFunc
import shutil


def run(*args, **kwargs):
    Utility.print_info(__file__, args, kwargs)
    version_type = args[2]
    if version_type == "P0":
        build_p0()
    elif version_type == "P1":
        build_p1()
    else:
        JobFunc.RaiseException(KeyError, "Unknown version type:%s" % version_type)


def build_p0():
    remove_folder()
    git_clone()
    make('mkimg_demo.sh')


def build_p1():
    remove_folder()
    git_clone()
    make('mkimg_g4.sh')





def git_clone():
    os.chdir(JobFunc.PATH_SOURCE_CODE)
    command_exit_code = Utility.execute_command(cmd="git clone ssh://youwu@gerrit.sensethink.cn:29418/9201")
    if command_exit_code != 0:
        raise IOError
    os.chdir(os.path.join(JobFunc.PATH_SOURCE_CODE, '9201'))
    command_exit_code = Utility.execute_command(cmd="git checkout -b encrypt origin/encrypt")
    if command_exit_code != 0:
        raise IOError


def make(script):
    src_folder = os.path.join(JobFunc.PATH_SOURCE_CODE, '9201')
    script_path = os.path.join(src_folder, script)
    if os.path.exists(script_path):
        change_permission(script_path)
        os.chdir(src_folder)
        execute_script(script=script)
    else:
        raise IOError


def change_permission(path):
    command_exit_code = Utility.execute_command(cmd="chmod u+x %s" % path)
    if command_exit_code != 0:
        raise IOError


def execute_script(script):
    command_exit_code = Utility.execute_command(cmd="./%s" % script)
    if command_exit_code != 0:
        raise IOError
