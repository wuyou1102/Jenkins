# -*- encoding:UTF-8 -*-
from libs import Environment as Env
from Config import Path
import os
import shutil


def run(*args, **kwargs):
    folder = Env.get('NeedRelease')
    src = os.path.join(Path.DAILY_DEPLOY, folder)
    dst = os.path.join(Path.WEEKLY_DEPLOY, folder)
    shutil.copytree(src=src, dst=dst)
