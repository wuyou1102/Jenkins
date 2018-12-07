# -*- encoding:UTF-8 -*-
import os
from libs.Utility import ConsolePrint
from libs import Utility
from libs import Environment as Env
import shutil

PATH_SOURCE_CODE = "/home/bspserver/sda/B2_SourceCode"
PATH_DAILY_BUILD = "/home/bspserver/sda/B2_DailyBuild"
PATH_CONFIG_PATH = "/home/bspserver/sda/VersionConfig/B2.txt"
DAILY_DEPLOY = os.path.join(PATH_DAILY_BUILD, Env.BUILD_TIMESTAMP)
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


def get_version_number():
    with open(os.path.join(DAILY_DEPLOY, 'VersionNumber.txt'), 'r') as f:
        ver = f.read()
    return ver
