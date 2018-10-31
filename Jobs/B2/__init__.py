# -*- encoding:UTF-8 -*-
from Deploy import run as deploy
from Build import run as build
from Checkout import run as checkout
from Test import run as test


class Job(object):
    checkout = checkout
    build = build
    test = test
    deploy = deploy
