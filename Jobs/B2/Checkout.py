# -*- encoding:UTF-8 -*-
import os
from libs import Utility
import JobFunc


def run(*args, **kwargs):
    JobFunc.SendJobStartMail()
    Utility.print_info(__file__, args, kwargs)
    workspace_path = Utility.get_compiler_path()
    Utility.create_folder(workspace_path)
    free, used, total = Utility.get_disk_usage(workspace_path)
    print "free:%s" % free
    print "used:%s" % used
    print "total:%s" % total
    if free < 200:
        JobFunc.RaiseException(MemoryError, "Insufficient disk space.")

    os.chdir(workspace_path)
    repo_init_command = Utility.Repo.init(url='ssh://youwu@gerrit.sensethink.cn:29418/manifest', branch='C2_8.1_master')
    repo_init_exit_code = Utility.execute_command(repo_init_command)
    if repo_init_exit_code != 0:
        JobFunc.RaiseException(IOError, "Repo init error")

    repo_sync_command = Utility.Repo.sync()
    repo_sync_exit_code = Utility.execute_command(repo_sync_command)
    if repo_sync_exit_code != 0:
        JobFunc.RaiseException(IOError, "Repo sync error")
