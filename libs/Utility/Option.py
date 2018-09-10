# -*- encoding:UTF-8 -*-

from optparse import OptionParser


def get_parser():
    parser = OptionParser()
    parser.add_option("-s", "--stage", dest="filename",
                      help="write report to FILE", metavar="FILE")

    (options, args) = parser.parse_args()
