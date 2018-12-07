# -*- encoding:UTF-8 -*-
import os
from libs import Utility
import JobFunc


def run(*args, **kwargs):
    src_path = JobFunc.git_clone()
    JobFunc.check_commit_history(path=src_path)
