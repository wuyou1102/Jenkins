# -*- encoding:UTF-8 -*-
import os


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
