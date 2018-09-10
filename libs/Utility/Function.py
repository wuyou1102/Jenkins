# -*- encoding:UTF-8 -*-
import os
import subprocess
from libs import Environment as Env


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
