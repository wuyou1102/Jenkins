# -*- encoding:UTF-8 -*-
import os
from libs import Utility
from libs.Utility import ConsolePrint
from libs import Environment as Env
from Config import Path
import JobFunc
import sys


def run(*args, **kwargs):
    JobFunc.SendJobStartMail()
    Utility.print_info(__file__, args, kwargs)
    check_space_available(path=Path.COMPILER_PATH)  # 检查硬盘空间是否充足
    init_repo(path=Path.COMPILER_PATH)  # 初始化 repo
    check_commit_history(path=Path.COMPILER_PATH)  # 检查是否有最新的提交记录
    sync_repo(path=Path.COMPILER_PATH)  # 同步 repo


def check_space_available(path):
    Utility.create_folder(path)
    free, used, total = Utility.get_disk_usage(path)
    ConsolePrint.info("free:%s" % free)
    ConsolePrint.info("used:%s" % used)
    ConsolePrint.info("total:%s" % total)
    if free < 200:
        JobFunc.RaiseException(MemoryError, "Insufficient disk space.")


def init_repo(path):
    os.chdir(path)
    repo_init_command = Utility.Repo.init(url='ssh://youwu@gerrit.sensethink.cn:29418/manifest', branch='C2_8.1_master')
    repo_init_exit_code = Utility.execute_command(repo_init_command)
    if repo_init_exit_code != 0:
        JobFunc.RaiseException(IOError, "Repo init error")


def sync_repo(path):
    os.chdir(path)
    repo_sync_command = Utility.Repo.sync()
    repo_sync_exit_code = Utility.execute_command(repo_sync_command)
    if repo_sync_exit_code != 0:
        JobFunc.RaiseException(IOError, "Repo sync error")


def cleanup_repo(path):
    import shutil
    shutil.rmtree(path)


def check_commit_history(path):
    os.chdir(path)
    since = Utility.get_timestamp(time_fmt="%Y-%m-%d %H:%M", t=Env.BUILD_TIME - 3600 * 24 * 1)
    output = os.popen(Utility.Repo.log(since=since)).read()
    if output:
        ConsolePrint.info(output)
        pass
    else:
        ConsolePrint.info("No commit submitted in the last day ")
        cleanup_repo(path=path)
        sys.exit(0)
