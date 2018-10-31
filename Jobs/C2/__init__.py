# -*- encoding:UTF-8 -*-
from Checkout import run as checkout
from Build import run as build
from Test import run as test
from Deploy import run as deploy
from Cleanup import run as cleanup


class Job(object):
    checkout = checkout
    build = build
    test = test
    deploy = deploy
    cleanup = cleanup
