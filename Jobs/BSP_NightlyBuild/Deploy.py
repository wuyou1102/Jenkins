# -*- encoding:UTF-8 -*-
import os
from libs import Environment as Env
from libs import Utility
import shutil


def get_output_path():
    out_path = get_out_path()
    for folder in os.listdir(out_path):
        if "g2-userdebug-" in folder:
            return os.path.join(out_path, folder)
    return None


def get_out_path():
    compiler_path = Utility.get_compiler_path()
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


def create_release_notes():
    compiler_path = Utility.get_compiler_path()
    deploy_path = Utility.get_deploy_path()
    os.chdir(compiler_path)
    since = Utility.get_timestamp(time_fmt="%Y-%m-%d %H:%M", t=Env.BUILD_TIME - 3600 * 24 * 3)
    lines = os.popen(Utility.Repo.log(since=since)).readlines()
    with open(os.path.join(deploy_path, "ReleaseNotes.txt"), "w") as wfile:
        for line in lines:
            print line
            wfile.write(line + '\n')


def run(*args, **kwargs):
    Utility.print_info(__file__, *args, **kwargs)
    output_path = get_output_path()
    if output_path:
        deploy_path = Utility.get_deploy_path()
        copy_binary_to_deploy(src_folder=output_path, dst_folder=os.path.join(deploy_path, 'Binary'))
        copy_debug_info_to_deploy(src_folder=get_out_path(), dst_folder=os.path.join(deploy_path, 'DebugInfo'))
        create_release_notes()
    else:
        print "Can not find out file."
        raise IOError


if __name__ == '__main__':
    run()
