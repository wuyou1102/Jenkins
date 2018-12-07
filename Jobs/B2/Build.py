# -*- encoding:UTF-8 -*-
from libs import Utility
import os
import JobFunc


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
    if os.path.exists(JobFunc.DAILY_DEPLOY):
        JobFunc.remove_folder()
        JobFunc.git_clone()
        change_version_number()
        make('mkimg_demo.sh')


def build_p1():
    if os.path.exists(JobFunc.DAILY_DEPLOY):
        JobFunc.remove_folder()
        JobFunc.git_clone()
        change_version_number()
        make('mkimg_g4.sh')


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


def get_version_number():
    with open(JobFunc.DAILY_DEPLOY, 'VersionNumber') as f:
        ver = f.read()
    return ver


def change_version_number():
    version_number = get_version_number()
    src_folder = os.path.join(JobFunc.PATH_SOURCE_CODE, '9201')
    version = os.path.join(src_folder, 'versions', 'version.txt')
    with open(version, 'w') as f:
        f.write(version_number)
