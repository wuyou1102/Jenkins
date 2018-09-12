# -*- encoding:UTF-8 -*-
import os
import time

environ = os.environ
__debug = False or os.getenv('computername') == 'OEMPC'

__timestamp = "20180911.122335"


def get(attr_name):
    return environ.get(key=attr_name, failobj=None)


COMPILER_FOLDER = get('COMPILER_FOLDER')  # 编译目录
DEPLOY_FOLDER = get('DEPLOY_FOLDER')  # 发布目录
BUILD_TIMESTAMP = get('BUILD_TIMESTAMP') if not __debug else __timestamp  # JENKINS触发事件
BUILD_TIME = time.mktime(time.strptime(BUILD_TIMESTAMP, "%Y%m%d.%H%M%S"))  # float型
PROGRAM_NAME = get('PROGRAM_NAME')  # 项目名称
JOB_NAME = get('JOB_NAME')  # JENKINS JOB名称
VERSION_TYPE = get('VERSION_TYPE')  # 版本类型
CORE_QUANTITY = get('CORE_QUANTITY')  # CPU核心数
BUILD_URL = get("BUILD_URL") if not __debug else "http://192.168.90.42:8080/job/BSP_NightlyBuild_Dev/100/"
