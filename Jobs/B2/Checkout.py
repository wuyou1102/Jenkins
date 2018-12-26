# -*- encoding:UTF-8 -*-
import os
from libs import Utility
from libs.Utility import ConsolePrint
import JobFunc
from libs import Environment


def run(*args, **kwargs):
    try:
        Utility.job_started()
        version_type = args[2]
        JobFunc.remove_folder()
        src_path = JobFunc.git_clone()
        check_commit_history(path=src_path, _type=version_type)
    except Exception:
        Utility.Incoming.job_exception()
        raise Exception


def check_commit_history(path, _type):
    os.chdir(path)
    output = os.popen('git log --since=1.day').read()
    ConsolePrint.info("wuyou debug:-> %s" % output)
    if output:
        create_deploy_folder(path=JobFunc.get_deploy_path(_type), commit_msg=output, _type=_type)
    else:
        ConsolePrint.info("No commit submitted in the last day ")


def create_deploy_folder(path, commit_msg, _type):
    Utility.create_folder(path=path)
    write_commit_history(path=path, commit_msg=commit_msg)
    return generate_version_number(path=path, _type=_type)


def write_commit_history(path, commit_msg):
    with open(os.path.join(path, "CommitHistory.txt"), "w") as wfile:
        wfile.write(commit_msg)
    return True


def parse_version_config(config_path):
    with open(config_path) as old:
        config = dict()
        for line in old.readlines():
            tmp = line.strip('\r\n').split(JobFunc.sep)
            config[tmp[0]] = tmp[1]
    config['Edition'] = '{0:02d}'.format(int(config['Edition']))
    config['Release'] = '{0:02d}'.format(int(config['Release']))
    config['Internal'] = '{0:03d}'.format(int(config['Internal']) + 1)
    version_name = "{p}-{h}{m}-{r}".format(p=config['Project'], h=config['HW'], m=config['Market'],
                                           r=config['Reserved'])
    version_number = '{e}.{r}.{i}'.format(e=config['Edition'], r=config['Release'], i=config['Internal'])
    version = '{name}-{number}'.format(name=version_name, number=version_number)
    with open(config_path, 'w') as new:
        for attr_name in ['Project', 'HW', 'Market', 'Reserved', 'Edition', 'Release', 'Internal']:
            new.write('{name}{sep}{value}\n'.format(name=attr_name, sep=JobFunc.sep, value=config[attr_name]))
    print version
    return version


def generate_version_number(path, _type):
    version_number = parse_version_config(config_path=JobFunc.get_config_path(_type=_type))
    with open(os.path.join(path, "VersionNumber.txt"), "w") as wfile:
        wfile.write(version_number)
    return version_number
