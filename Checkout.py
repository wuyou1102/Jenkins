import os

from libs import Utility

environment = os.environ
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

HOME = '/home/bspserver'
G4 = 'G4_Version'
WORKSPACE = os.path.join(HOME, G4, Utility.get_timestamp())

if not os.path.exists(WORKSPACE):
    print "Create New Folder: %s " % WORKSPACE
    os.makedirs(WORKSPACE)

environment["WORKSPACE"] = WORKSPACE
os.chdir(WORKSPACE)
