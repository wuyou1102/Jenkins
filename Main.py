# -*- encoding:UTF-8 -*-
from libs import Environment as Env
from libs import Configuration as Cfg
from Jobs import Get_Python_Job
import sys

Job = Get_Python_Job(Cfg.Jobs.get(Env.JOB_NAME))


def checkout():
    Job.checkout()


def test():
    Job.test()


def build():
    Job.build()


def deploy():
    Job.deploy


switch = {
    "checkout": Job.checkout,
    "test": Job.test,
    "build": Job.build,
    "deploy": Job.deploy,
}

if __name__ == '__main__':
    stage = sys.argv[1].lower()
    switch.get(stage)()
