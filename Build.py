from libs import Utility
import os

workspace_path = '/home/bspserver/sda/C2_SourceCode/c2_userdebug_20180906.180549/'
os.chdir(workspace_path)

envsetup_command = "/bin/bash build/envsetup.sh && build/link.sh && lunch g2-userdebug general && ulimit -c unlimited && make update-api -j8 && make -j8"
link_command = ""
lunch_command = "/bin/bash lunch g2-userdebug general"
ulimit_command = "/bin/bash ulimit -c unlimited"
update_command = "/bin/bash make update-api -j8"
make_command = "/bin/bash make -j8"

commands = [
    envsetup_command,
    # link_command,
    # lunch_command,
    # ulimit_command,
    # update_command,
    # make_command
]

for command in commands:
    command_exit_code = Utility.execute_command(cmd=command)
    if command_exit_code != 0:
        raise IOError
