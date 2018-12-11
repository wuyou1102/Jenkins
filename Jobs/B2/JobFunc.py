# -*- encoding:UTF-8 -*-
import os
from libs.Utility import ConsolePrint
from libs import Utility
from libs import Environment as Env
import shutil

PATH_SOURCE_CODE = "/home/bspserver/sda/B2/B2_SourceCode"
PATH_9A_CONFIG = "/home/bspserver/sda/VersionConfig/B2_9A.txt"
PATH_9A_DAILY = "/home/bspserver/sda/B2/B2_9A_DailyBuild"
PATH_9B_CONFIG = "/home/bspserver/sda/VersionConfig/B2_9B.txt"
PATH_9B_DAILY = "/home/bspserver/sda/B2/B2_9B_DailyBuild"

sep = " *|* "


def git_clone():
    os.chdir(PATH_SOURCE_CODE)
    command_exit_code = Utility.execute_command(cmd="git clone ssh://youwu@gerrit.sensethink.cn:29418/9201")
    if command_exit_code != 0:
        raise IOError
    os.chdir(os.path.join(PATH_SOURCE_CODE, '9201'))
    command_exit_code = Utility.execute_command(cmd="git checkout -b encrypt origin/encrypt")
    if command_exit_code != 0:
        raise IOError
    return os.path.join(PATH_SOURCE_CODE, '9201')


def remove_folder():
    src_folder = os.path.join(PATH_SOURCE_CODE, "9201")
    if os.path.exists(src_folder):
        shutil.rmtree(src_folder)


def get_version_number(_type):
    with open(os.path.join(_type, 'VersionNumber.txt'), 'r') as f:
        ver = f.read()
    return ver


def get_deploy_path(_type):
    if _type == "P0":
        return os.path.join(PATH_9A_DAILY, Env.BUILD_TIMESTAMP)
    return os.path.join(PATH_9B_DAILY, Env.BUILD_TIMESTAMP)
