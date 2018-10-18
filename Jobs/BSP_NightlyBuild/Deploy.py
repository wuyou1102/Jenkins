# -*- encoding:UTF-8 -*-
import os
from libs import Environment as Env
from libs import Utility
import shutil
import JobFunc

def run(*args, **kwargs):
    Utility.print_info(__file__, args, kwargs)