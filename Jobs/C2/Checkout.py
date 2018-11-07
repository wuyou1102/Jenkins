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
    sync_repo(path=Path.COMPILER_PATH)  # 同步 repo
    check_commit_history(path=Path.COMPILER_PATH)  # 检查是否有最新的提交记录


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
    since = Utility.get_timestamp(time_fmt="%Y-%m-%d %H:%M", t=Env.BUILD_TIME - 3600 * 24 * 20)
    output = os.popen(Utility.Repo.log(since=since)).read()
    ConsolePrint.info(output)
    if output:
        version_number = create_deploy_folder(path=Path.DAILY_DEPLOY, commit_msg=output)
        modify_src_version_number(path=path, version=version_number)
    else:
        ConsolePrint.info("No commit submitted in the last day ")
        cleanup_repo(path=path)


def create_deploy_folder(path, commit_msg):
    Utility.create_folder(path=path)
    write_commit_history(path=path, commit_msg=commit_msg)
    return generate_version_number(path=path)


def write_commit_history(path, commit_msg):
    with open(os.path.join(path, "CommitHistory.txt"), "w") as wfile:
        wfile.write(commit_msg)
    return True


def generate_version_number(path):
    version_number = JobFunc.parse_version_config()
    with open(os.path.join(path, "VersionNumber.txt"), "w") as wfile:
        wfile.write(version_number)
    return version_number


def modify_src_version_number(path, version):
    version_file = os.path.join(path, 'build', 'make', 'core', 'build_id.mk')
    with open(version_file) as old:
        s = old.read()
    with open(version_file, 'w') as new:
        s = s.replace('export BUILD_ID=OPM1.171019.026',
                      'export BUILD_ID=%s' % version)
        new.write(s)


if __name__ == '__main__':
    modify_src_version_number('ss', 'dddd')
