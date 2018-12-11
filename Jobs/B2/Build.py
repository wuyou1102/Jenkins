# -*- encoding:UTF-8 -*-
from libs import Utility
import os
import JobFunc
import shutil

src_folder = os.path.join(JobFunc.PATH_SOURCE_CODE, '9201')
output_folder = os.path.join(JobFunc.PATH_SOURCE_CODE, "9201", "output", "image")


def run(*args, **kwargs):
    Utility.print_info(__file__, args, kwargs)
    version_type = args[2]
    if version_type == "P0":
        build_p0()
    elif version_type == "P1":
        build_p1()
    else:
        JobFunc.RaiseException(KeyError, "Unknown version type:%s" % version_type)


def build_p0():
    version_type = "P0"
    if os.path.exists(JobFunc.get_deploy_path(_type=version_type)):
        change_version_number(version_type)
        make('mkimg_demo.sh')
        copy_image(_type="P0")


def build_p1():
    version_type = "P1"
    if os.path.exists(JobFunc.get_deploy_path(_type=version_type)):
        change_version_number(version_type)
        make('mkimg_g4.sh')
        copy_image(_type="P1")


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
    dst_folder = JobFunc.get_deploy_path(_type)
    version = JobFunc.get_version_number(JobFunc.get_deploy_path(_type=_type)).split('.')[-1]
    for f in os.listdir(output_folder):
        if f.startswith(full):
            shutil.copy(src=os.path.join(output_folder, f),
                        dst=os.path.join(dst_folder, "B2%sF_%s.img" % (_type, version)))
        elif f.startswith(u_disk1) or f.startswith(u_disk2):
            shutil.copy(src=os.path.join(output_folder, f),
                        dst=os.path.join(dst_folder, "B2%sU_%s.img" % (_type, version)))
        else:
            print "wuyou debug:->%s" % f
