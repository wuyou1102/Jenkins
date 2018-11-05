# -*- encoding:UTF-8 -*-
import os
from libs import Utility
from libs.Utility import ConsolePrint
from Config import Path
import JobFunc


def run(*args, **kwargs):
    JobFunc.SendJobStartMail()
    Utility.print_info(__file__, args, kwargs)
    workspace_path = Utility.get_compiler_path()
    Utility.create_folder(workspace_path)
    check_space_available(path=workspace_path)
    init_repo(path=workspace_path)
    sync_repo(path=workspace_path)


def check_space_available(path):
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
