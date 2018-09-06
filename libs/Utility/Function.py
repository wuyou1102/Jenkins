# -*- encoding:UTF-8 -*-
import os
import subprocess


def get_compiler_path():
    path = os.environ['COMPILER_FOLDER']
    timestamp = os.environ['BUILD_TIMESTAMP']
    program_name = os.environ['PROGRAM_NAME']
    version_type = os.environ['VERSION_TYPE']
    version_name = "%s_%s_%s" % (program_name, version_type, timestamp)
    return os.path.join(path, version_name)


def get_deploy_path():
    path = os.environ['DEPLOY_FOLDER']
    timestamp = os.environ['BUILD_TIMESTAMP']
    program_name = os.environ['PROGRAM_NAME']
    version_type = os.environ['VERSION_TYPE']
    version_name = "%s_%s_%s" % (program_name, version_type, timestamp)
    return os.path.join(path, version_name)


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
        return p.wait()
