# -*- encoding:UTF-8 -*-
from libs import Environment as Env
import JobFunc
import os
import shutil


def run(*args, **kwargs):
    version_type = Env.get('VersionType')
    need_release = Env.get('NeedRelease')
    if not version_type:
        raise IOError(u"版本类型配置不正确")
    daily_path, weekly_path = __get_path(version_type)
    src_folder = get_src_folder(daily_path, need_release)
    src = os.path.join(daily_path, src_folder)
    dst = os.path.join(weekly_path, src_folder)
    shutil.copytree(src=src, dst=dst)


def get_src_folder(path, except_version):
    for folder in os.listdir(path):
        file_path = os.path.join(path, folder, "VersionNumber.txt")
        if os.path.exists(file_path):
            with open(file_path) as f:
                if except_version in f.readline():
                    return folder


def __get_path(_type):
    if _type == "9A":
        return JobFunc.PATH_DAILY_9A, JobFunc.PATH_WEEKLY_9A
    elif _type == "9B":
        return JobFunc.PATH_DAILY_9B, JobFunc.PATH_WEEKLY_9B
    else:
        return None, None
