# -*- encoding:UTF-8 -*-
from libs import Environment as Env
import os

__SOURCE_PATH = '/home/bspserver/sda/C2_SourceCode/'
__DAILY_PATH = '/home/bspserver/sda/C2_DailyBuild/'
__WEEKLY_PATH = '/home/bspserver/sda/C2_WeeklyBuild/'
__TRIGGER_PATH = '/home/bspserver/sda/C2_TriggerBuild/'

COMPILER_PATH = os.path.join(__SOURCE_PATH, Env.BUILD_TIMESTAMP)
DAILY_DEPLOY = os.path.join(__DAILY_PATH, Env.BUILD_TIMESTAMP)
WEEKLY_DEPLOY = os.path.join(__WEEKLY_PATH, Env.BUILD_TIMESTAMP)
TRIGGER_DEPLOY = os.path.join(__TRIGGER_PATH, Env.BUILD_TIMESTAMP)

