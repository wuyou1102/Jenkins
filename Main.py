# -*- encoding:UTF-8 -*-
from libs import Environment as Env
from libs import Configuration as Cfg
from Jobs import Get_Python_Job
import sys

if __name__ == '__main__':
    Job = Get_Python_Job(Env.JOB_NAME)
    stage = getattr(Job, sys.argv[1].lower())
    stage(*sys.argv)
