# -*- encoding:UTF-8 -*-
import os


def get_c2_complier_path():
    compiler = os.environ['COMPILER_FOLDER']
    timestamp = os.environ['BUILD_TIMESTAMP']
    version_name = "C2_%s" % timestamp
    return os.path.join(compiler, version_name)
