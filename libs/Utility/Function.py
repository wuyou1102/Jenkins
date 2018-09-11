# -*- encoding:UTF-8 -*-
import os
import subprocess
from libs import Environment as Env
import re


def get_compiler_path():
    version_name = "%s_%s_%s" % (Env.PROGRAM_NAME, Env.VERSION_TYPE, Env.BUILD_TIMESTAMP)
    return os.path.join(Env.COMPILER_FOLDER, version_name)


def get_deploy_path():
    version_name = "%s_%s_%s" % (Env.PROGRAM_NAME, Env.VERSION_TYPE, Env.BUILD_TIMESTAMP)
    return os.path.join(Env.DEPLOY_FOLDER, version_name)


def create_folder(path):
    if not os.path.exists(path):
        print "Create New Folder: %s " % path
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
            print line.rstrip()
    except Exception, e:
        print e.message
    finally:
        exit_code = p.wait()
        print 'Executed command:\"%s\" and exit code is : \"%s\"' % (cmd, exit_code)
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
