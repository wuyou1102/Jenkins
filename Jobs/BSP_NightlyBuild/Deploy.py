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


def run(*args, **kwargs):
    Utility.print_info(__file__, *args, **kwargs)
    output_path = get_output_path()
    if output_path:
        deploy_path = Utility.get_deploy_path()
        Utility.create_folder(deploy_path)
        for f in os.listdir(output_path):
            src = os.path.join(output_path, f)
            dst = os.path.join(deploy_path, f)
            print "Copy \"%s\" to \"%s\"" % (src, dst)
            shutil.copyfile(src=src, dst=dst)
    else:
        print "Can not find out file."
        raise IOError


if __name__ == '__main__':
    run()
