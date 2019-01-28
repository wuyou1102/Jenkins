# -*- encoding:UTF-8 -*-
from libs import Utility
import os
import JobFunc
import shutil
from libs import Environment

src_folder = os.path.join(JobFunc.PATH_SOURCE_CODE, '9201')
output_folder = os.path.join(JobFunc.PATH_SOURCE_CODE, "9201", "output", "image")


def run(*args, **kwargs):
    try:
        Utility.print_info(__file__, args, kwargs)
        version_type = args[2]
        if version_type == "P0":
            build_p0()
        elif version_type == "P1":
            build_p1()
        Utility.job_finished()
    except Exception:
        Utility.job_exception()
        raise Exception


def build_p0():
    version_type = "P0"
    if os.path.exists(JobFunc.get_deploy_path(_type=version_type)):
        change_version_number(version_type)
        make('mkimg_demo.sh')
        dst_folder = copy_image(_type="P0")
        Utility.zip_folder(dst_folder)


def build_p1():
    version_type = "P1"
    if os.path.exists(JobFunc.get_deploy_path(_type=version_type)):
        change_version_number(version_type)
        make('mkimg_g4.sh')
        dst_folder = copy_image(_type="P1")
        Utility.zip_folder(dst_folder)
        make('mkimg_odm.sh')
        dst_folder = copy_odm_image(_type="P1")
        Utility.zip_folder(dst_folder)


def make(script):
    script_path = os.path.join(src_folder, script)
    if os.path.exists(script_path):
        change_permission(script_path)
        os.chdir(src_folder)
        execute_script(script=script)
    else:
        raise IOError


def change_permission(path):
    command_exit_code = Utility.execute_command(cmd="chmod u+x %s" % path)
    if command_exit_code != 0:
        raise IOError


def execute_script(script):
    command_exit_code = Utility.execute_command(cmd="./%s" % script)
    if command_exit_code != 0:
        raise IOError


def change_version_number(_type):
    version_number = JobFunc.get_version_number(JobFunc.get_deploy_path(_type=_type))
    version = os.path.join(src_folder, 'versions', 'version.txt')
    with open(version, 'w') as f:
        f.write(version_number)


def copy_image(_type):
    u_disk1 = 'artosyn-upgrade-B2%sU.' % _type
    u_disk2 = 'B2%sU.' % _type
    full = 'B2%sF.' % _type
    # dst_folder = Utility.create_folder(os.path.join(JobFunc.get_deploy_path(_type), _type))
    deploy_path = JobFunc.get_deploy_path(_type)
    long_version = JobFunc.get_version_number(deploy_path)
    short_version = long_version.split('.')[-1]
    dst_folder = Utility.create_folder(path=os.path.join(deploy_path, long_version))
    for f in os.listdir(output_folder):
        if f.startswith(full):
            shutil.copy(src=os.path.join(output_folder, f),
                        dst=os.path.join(dst_folder, "B2%sF_%s.img" % (_type, short_version)))
        elif f.startswith(u_disk1) or f.startswith(u_disk2):
            shutil.copy(src=os.path.join(output_folder, f),
                        dst=os.path.join(dst_folder, "B2%sU_%s.img" % (_type, short_version)))
        else:
            print "wuyou debug:->%s" % f
    return dst_folder


def copy_odm_image(_type):
    u_disk1 = 'artosyn-upgrade-B2%sU.' % _type
    u_disk2 = 'B2%sU.' % _type
    full = 'B2%sF.' % _type
    # dst_folder = Utility.create_folder(os.path.join(JobFunc.get_deploy_path(_type), _type))
    deploy_path = JobFunc.get_deploy_path(_type)
    long_version = JobFunc.get_version_number(deploy_path)
    long_version = long_version.replace("9B01", "9B02")
    short_version = long_version.split('.')[-1]
    dst_folder = Utility.create_folder(path=os.path.join(deploy_path, long_version))
    for f in os.listdir(output_folder):
        if f.startswith(full):
            shutil.copy(src=os.path.join(output_folder, f),
                        dst=os.path.join(dst_folder, "B2%sF_%s.img" % (_type, short_version)))
        elif f.startswith(u_disk1) or f.startswith(u_disk2):
            shutil.copy(src=os.path.join(output_folder, f),
                        dst=os.path.join(dst_folder, "B2%sU_%s.img" % (_type, short_version)))
        else:
            print "wuyou debug:->%s" % f
    return dst_folder
