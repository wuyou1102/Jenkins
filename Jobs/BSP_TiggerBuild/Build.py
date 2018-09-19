from libs import Utility
import os
import JobFunc
import shutil
from libs import Environment as Env


def run(*args, **kwargs):
    Utility.print_info(__file__, args, kwargs)
    version_type = Env.VERSION_TYPE
    remove_out_folder()
    if version_type == "userdebug":
        build_userdebug()
    elif version_type == "user":
        build_user()
    else:
        JobFunc.RaiseException(KeyError, "Unknown version type:%s" % version_type)


def build_userdebug():
    workspace_path = Utility.get_compiler_path()
    os.chdir(workspace_path)
    envsetup_command = "source build/envsetup.sh"
    link_command = "source build/link.sh"
    lunch_command = "lunch g2-userdebug general"
    ulimit_command = "ulimit -c unlimited"
    update_command = "make update-api -j8"
    make_command = "make -j8"

    commands = [
        envsetup_command,
        link_command,
        lunch_command,
        ulimit_command,
        update_command,
        make_command
    ]
    command = " && ".join(commands)
    command_exit_code = Utility.execute_command(cmd=command)
    if command_exit_code != 0:
        JobFunc.RaiseException(IOError, "Build Error")


def build_user():
    workspace_path = Utility.get_compiler_path()
    os.chdir(workspace_path)
    envsetup_command = "source build/envsetup.sh"
    link_command = "source build/link.sh"
    lunch_command = "lunch g2-user general"
    ulimit_command = "ulimit -c unlimited"
    update_command = "make update-api -j8"
    make_command = "make -j8"

    commands = [
        envsetup_command,
        link_command,
        lunch_command,
        ulimit_command,
        update_command,
        make_command
    ]
    command = " && ".join(commands)
    command_exit_code = Utility.execute_command(cmd=command)
    if command_exit_code != 0:
        JobFunc.RaiseException(IOError, "Build Error")


def remove_out_folder():
    workspace_path = Utility.get_compiler_path()
    out_folder = os.path.join(workspace_path, "out")
    if os.path.exists(out_folder):
        shutil.rmtree(out_folder)
