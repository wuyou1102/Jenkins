# -*- encoding:UTF-8 -*-
import os
from libs import Environment as Env
from libs import Utility
import shutil
import JobFunc
from Config import Path

BUILD_NUMBER = Env.get('BUILD_NUMBER')


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


def copy_ota_to_deploy(src_folder, ota_folder, binary_folder):
    Utility.create_folder(ota_folder)
    zipfile_ota = os.path.join(src_folder, 'g2-ota-%s.zip' % BUILD_NUMBER)
    folder_intermediates = os.path.join(src_folder, 'obj', 'PACKAGING', 'target_files_intermediates')
    zipfile_targetfile = os.path.join(folder_intermediates, 'g2-target_files-%s.zip' % BUILD_NUMBER)
    image_system = os.path.join(folder_intermediates, 'g2-target_files-%s' % BUILD_NUMBER, 'IMAGES', 'system.img')
    shutil.copyfile(src=zipfile_ota, dst=os.path.join(ota_folder, 'ota.zip'))
    shutil.copyfile(src=zipfile_targetfile, dst=os.path.join(ota_folder, 'target_files.zip'))
    shutil.copyfile(src=image_system, dst=os.path.join(binary_folder, 'system.img'))


def run(*args, **kwargs):
    Utility.print_info(__file__, *args, **kwargs)
    if not os.path.exists(Path.COMPILER_PATH):
        import sys
        sys.exit(0)
    version_type = args[2]
    if version_type == "UserDebug":
        deploy_version(_type=userdebug)
    elif version_type == "User":
        deploy_version(_type=user)
    else:
        JobFunc.RaiseException(KeyError, "Unknown version type:%s" % version_type)
    JobFunc.SendJobFinishMail()


userdebug = 'userdebug'
user = 'user'
binary = 'Binary'
debuginfo = 'DebugInfo'
ota = "OTA"


def deploy_version(_type):
    output_path = get_userdebug_path() if _type == userdebug else get_user_path()
    if output_path:
        deploy_path = Path.DAILY_DEPLOY
        binary_folder = os.path.join(deploy_path, binary, _type)
        debug_info_folder = os.path.join(deploy_path, debuginfo, _type)
        ota_folder = os.path.join(deploy_path, ota, _type)
        copy_binary_to_deploy(src_folder=output_path, dst_folder=binary_folder)
        copy_debug_info_to_deploy(src_folder=get_out_path(), dst_folder=debug_info_folder)
        copy_ota_to_deploy(src_folder=get_out_path(), ota_folder=ota_folder, binary_folder=binary_folder)
        Utility.zip_folder(os.path.join(deploy_path, binary, _type))
        Utility.zip_folder(os.path.join(deploy_path, debuginfo, _type))
    else:
        JobFunc.RaiseException(IOError, "Can not find out file.")
