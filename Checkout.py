# -*- encoding:UTF-8 -*-
import os
from libs import Utility


# git
# url: 'ssh://jenkins@192.168.90.181:29418/9201_1'
#
#
# def changeBranch =
#
#
# "change-${GERRIT_CHANGE_NUMBER}-${GERRIT_PATCHSET_NUMBER}"
# sh
# "git fetch origin ${GERRIT_REFSPEC}:${changeBranch}"
# sh
# "git checkout ${changeBranch}"


workspace_path = Utility.get_compiler_path()


if not os.path.exists(workspace_path):
    print "Create New Folder: %s " % workspace_path
    os.makedirs(workspace_path)
os.chdir(workspace_path)
stdin, stdout, stderr = os.popen3(
    Utility.Repo.init(url='ssh://weicheng@gerrit.sensethink.cn:29418/manifest', branch='C2_8.1_master'))
print repr(stdout.read())
print repr(stderr.read())
stdin, stdout, stderr = os.popen3(Utility.Repo.sync(thread_num=8))
print repr(stdout.read())
print repr(stderr.read())
