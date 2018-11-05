# -*- encoding:UTF-8 -*-
import os
from libs import Environment as Env
from libs import Utility
import shutil
import JobFunc
from Config import Path


def get_userdebug_path():
    out_path = get_out_path()
    for folder in os.listdir(out_path):
        if "g2-userdebug-" in folder:
            return os.path.join(out_path, folder)
    return None


def get_user_path():
    out_path = get_out_path()
    for folder in os.listdir(out_path):
        if "g2-user-" in folder:
            return os.path.join(out_path, folder)
    return None


def get_out_path():
    compiler_path = Path.COMPILER_PATH
    out_path = os.path.join(compiler_path, 'out', 'target', 'product', 'g2')
    return out_path


def copy_binary_to_deploy(src_folder, dst_folder):
    Utility.create_folder(dst_folder)
    for f in os.listdir(src_folder):
        src = os.path.join(src_folder, f)
        dst = os.path.join(dst_folder, f)
        print "Copy \"%s\" to \"%s\"" % (src, dst)
        shutil.copyfile(src=src, dst=dst)


def copy_debug_info_to_deploy(src_folder, dst_folder):
    Utility.create_folder(dst_folder)
    src_folder = os.path.join(src_folder, 'obj', 'kernel', 'msm-4.4')
    for f in ['vmlinux', 'System.map']:
        src = os.path.join(src_folder, f)
        dst = os.path.join(dst_folder, f)
        print "Copy \"%s\" to \"%s\"" % (src, dst)
        shutil.copyfile(src=src, dst=dst)


def run(*args, **kwargs):
    Utility.print_info(__file__, *args, **kwargs)
    if not os.path.exists(Path.COMPILER_PATH):
        import sys
        sys.exit(0)
    version_type = args[2]
    if version_type == "UserDebug":
        deploy_userdebug_version()
    elif version_type == "User":
        deploy_user_version()
    else:
        JobFunc.RaiseException(KeyError, "Unknown version type:%s" % version_type)
    JobFunc.SendJobFinishMail()


userdebug = 'userdebug'
user = 'user'
binary = 'Binary'
debuginfo = 'DebugInfo'


def deploy_userdebug_version():
    output_path = get_userdebug_path()
    if output_path:
        deploy_path = Path.DAILY_DEPLOY()
        copy_binary_to_deploy(src_folder=output_path, dst_folder=os.path.join(deploy_path, binary, userdebug))
        copy_debug_info_to_deploy(src_folder=get_out_path(), dst_folder=os.path.join(deploy_path, debuginfo, userdebug))
        Utility.zip_folder(os.path.join(deploy_path, binary, userdebug))
        Utility.zip_folder(os.path.join(deploy_path, debuginfo, userdebug))
    else:
        JobFunc.RaiseException(IOError, "Can not find out file.")


def deploy_user_version():
    output_path = get_user_path()
    if output_path:
        deploy_path = Path.DAILY_DEPLOY()
        copy_binary_to_deploy(src_folder=output_path, dst_folder=os.path.join(deploy_path, binary, user))
        copy_debug_info_to_deploy(src_folder=get_out_path(), dst_folder=os.path.join(deploy_path, debuginfo, user))
        Utility.zip_folder(os.path.join(deploy_path, binary, user))
        Utility.zip_folder(os.path.join(deploy_path, debuginfo, user))
    else:
        JobFunc.RaiseException(IOError, "Can not find out file.")
