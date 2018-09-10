# -*- encoding:UTF-8 -*-
import os
import Configuration as cfg

environ = os.environ


def get(attr_name):
    return environ.get(key=attr_name, failobj=None)


COMPILER_FOLDER = get('COMPILER_FOLDER')  # 编译目录
DEPLOY_FOLDER = get('DEPLOY_FOLDER')  # 发布目录
BUILD_TIMESTAMP = get('BUILD_TIMESTAMP')  # JENKINS触发事件
PROGRAM_NAME = get('PROGRAM_NAME')  # 项目名称
JOB_NAME = get('JOB_NAME')  # JENKINS JOB名称
VERSION_TYPE = get('VERSION_TYPE')  # 版本类型
CORE_QUANTITY = get('CORE_QUANTITY')  # CPU核心数
