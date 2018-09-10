# -*- encoding:UTF-8 -*-
import os
from libs import Utility


def run():
    workspace_path = Utility.get_compiler_path()
    Utility.create_folder(workspace_path)
    os.chdir(workspace_path)

    repo_init_command = Utility.Repo.init(url='ssh://youwu@gerrit.sensethink.cn:29418/manifest', branch='C2_8.1_master')
    repo_init_exit_code = Utility.execute_command(repo_init_command)
    if repo_init_exit_code != 0:
        raise IOError

    repo_sync_command = Utility.Repo.sync()
    repo_sync_exit_code = Utility.execute_command(repo_sync_command)
    if repo_sync_exit_code != 0:
        raise IOError
