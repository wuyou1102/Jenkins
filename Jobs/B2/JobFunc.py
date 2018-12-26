# -*- encoding:UTF-8 -*-
import os
from libs import Utility
from libs import Environment as Env
import shutil

PATH_SOURCE_CODE = "/home/bspserver/sda/B2/SourceCode"
PATH_CONFIG_9A = "/home/bspserver/sda/VersionConfig/B2/9A.txt"
PATH_CONFIG_9B = "/home/bspserver/sda/VersionConfig/B2/9B.txt"
PATH_DAILY_9A = "/home/bspserver/sda/B2/DailyBuild/9A"
PATH_DAILY_9B = "/home/bspserver/sda/B2/DailyBuild/9B"
PATH_WEEKLY_9A = "/home/bspserver/sda/B2/WeeklyBuild/9A"
PATH_WEEKLY_9B = "/home/bspserver/sda/B2/WeeklyBuild/9B"


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


def get_version_number(path):
    with open(os.path.join(path, 'VersionNumber.txt'), 'r') as f:
        ver = f.read()
    return ver


def get_deploy_path(_type):
    if _type == "P0":
        return os.path.join(PATH_DAILY_9A, Env.BUILD_TIMESTAMP)
    return os.path.join(PATH_DAILY_9B, Env.BUILD_TIMESTAMP)


def get_config_path(_type):
    if _type == "P0":
        return PATH_CONFIG_9A
    return PATH_CONFIG_9B
