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

if not os.path.exists(home_folder):
    os.makedirs(cur_folder)
