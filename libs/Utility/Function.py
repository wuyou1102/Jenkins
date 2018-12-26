# -*- encoding:UTF-8 -*-
import os
import subprocess
from libs import Environment as Env
import ConsolePrint
import psutil
from Worktile import Incoming
import traceback


def get_compiler_path():
    if Env.VERSION_TYPE is not None:
        version_name = "%s_%s_%s" % (Env.PROGRAM_NAME, Env.VERSION_TYPE, Env.BUILD_TIMESTAMP)
    else:
        version_name = "%s_%s" % (Env.PROGRAM_NAME, Env.BUILD_TIMESTAMP)
    return os.path.join(Env.COMPILER_FOLDER, version_name)


def get_deploy_path():
    if Env.VERSION_TYPE is not None:
        version_name = "%s_%s_%s" % (Env.PROGRAM_NAME, Env.VERSION_TYPE, Env.BUILD_TIMESTAMP)
    else:
        version_name = "%s_%s" % (Env.PROGRAM_NAME, Env.BUILD_TIMESTAMP)
    return os.path.join(Env.DEPLOY_FOLDER, version_name)


def create_folder(path):
    if not os.path.exists(path):
        ConsolePrint.info("Create New Folder: %s " % path)
        os.makedirs(path)
    return path


def close_umask():
    set_umask(mask=0000)


def set_umask(mask=022):
    os.umask(mask)


def execute_command(cmd):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE, shell=True)
    try:
        for line in iter(p.stdout.readline, b''):
            ConsolePrint.info(line.rstrip())
    except Exception:
        ConsolePrint.traceback()
    finally:
        exit_code = p.wait()
        ConsolePrint.info('Executed command:\"%s\" and exit code is : \"%s\"' % (cmd, exit_code))
        return exit_code


def get_job_file_info(_file):
    tmp = _file.split(os.path.sep)
    # tmp = os.path.split(_file)
    job = tmp[-2]
    stage = tmp[-1]
    return "%s:%s" % (job, stage)


def print_info(_file, *args, **kwargs):
    title = get_job_file_info(_file)
    print "*" * 50
    print "*" + title.ljust(48) + "*"
    print "* Args:" + repr(args).ljust(42) + "*"
    print "* Kwargs:" + repr(kwargs).ljust(40) + "*"
    print "*" * 50


__dict_commit = {
    "commit ": "Commit Id",
    "Author:": "Author",
    "Date:   ": "Data",
    "Change-Id: ": "Change Id",
    "Signed-off-by: ": "Signed Off",
    "BugID: ": "'Bug Id"
}


def get_commit_blocks(lines):
    def remove_empty_lines():
        lines_with_out_empty = list()
        for l in lines:
            l = l.strip('\r\n')
            if '    ' in l:
                l = l.replace('    ', '')
            if l:
                lines_with_out_empty.append(l)
        return lines_with_out_empty

    lines = remove_empty_lines()
    blocks = []
    block = []
    for line in lines:
        if line.startswith('commit '):
            if block:
                blocks.append(block)
                block = list()
        block.append(line)
    blocks.append(block)
    return blocks


def format_commit_msg(lines):
    blocks = get_commit_blocks(lines=lines)
    lst = list()
    for block in blocks:
        m_dict = dict()
        for line in block[:]:
            for k, v in __dict_commit.items():
                if line.startswith(k):
                    m_dict[v] = line.lstrip(k)
                    block.remove(line)
                    break
        m_dict["Info"] = "\n".join(block)
        lst.append(m_dict)
    return lst


def get_disk_usage(path):
    usage = psutil.disk_usage(path)
    gigabyte = 1024 * 1024 * 1024  # 1024Byte *1024*KB*1024MB
    free = usage.free / gigabyte
    used = usage.used / gigabyte
    total = usage.total / gigabyte
    return free, used, total


def zip_folder(path):
    if path.endswith('/'):
        path.rstrip('/')
    p, f = os.path.split(path)
    os.chdir(p)
    execute_command("zip -r %s.zip %s" % (f, f))


def get_traceback():
    tmp = traceback.format_exc()
    if tmp != 'None\n':
        return tmp
    return ""


def RaiseException(error, build_info, users=[]):
    resp = Incoming.job_error(build_info=build_info, users=users, text=get_traceback())
    raise error


if __name__ == '__main__':
    zip_folder("/home/bspserver/sda/C2_DailyBuild/C2_20180919.050000/UserDebug")
