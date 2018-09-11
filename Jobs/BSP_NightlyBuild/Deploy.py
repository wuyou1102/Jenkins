# -*- encoding:UTF-8 -*-
import os
from libs import Utility
import shutil


def get_output_path():
    compiler_path = Utility.get_compiler_path()
    output_path = os.path.join(compiler_path, 'out', 'target', 'product', 'g2')
    for folder in os.listdir(output_path):
        if "g2-userdebug-" in folder:
            return os.path.join(output_path, folder)
    return None


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


def create_release_notes(path):
    pass


def run(*args, **kwargs):
    Utility.print_info(__file__, *args, **kwargs)
    output_path = get_output_path()
    if output_path:
        deploy_path = Utility.get_deploy_path()
        copy_binary_to_deploy(src_folder=output_path, dst_folder=os.path.join(deploy_path, 'Binary'))
        copy_debug_info_to_deploy(src_folder=output_path, dst_folder=os.path.join(deploy_path, 'DebugInfo'))
    else:
        print "Can not find out file."
        raise IOError


if __name__ == '__main__':
    run()
