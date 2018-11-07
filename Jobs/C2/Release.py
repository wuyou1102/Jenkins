# -*- encoding:UTF-8 -*-
from libs import Environment as Env
from Config import Path
import os
import shutil


def run(*args, **kwargs):
    folder = Env.get('NeedRelease')
    src = os.path.join(Path.__DAILY_PATH, folder)
    dst = os.path.join(Path.__WEEKLY_PATH, folder)
    shutil.copytree(src=src, dst=dst)
