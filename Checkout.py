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
home_folder = '~/G4_Version/'
cur_folder = os.path.join(home_folder, Utility.get_timestamp())

if not os.path.exists(cur_folder):
    print "Create New Folder: %s " % cur_folder
    os.makedirs(cur_folder)
dict_env = os.environ
print dict_env["WORKSPACE"]
os.chdir(cur_folder)
