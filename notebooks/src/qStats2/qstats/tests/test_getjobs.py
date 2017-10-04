#!/usr/bin/env python

from qstats import utils
from os.path import dirname, join

cwd = dirname(__file__)

def test_getjobs():
    theJobs = utils.getJobs([join(cwd,'data/events.Sun_Oct_25_2015')])
    assert len(theJobs) == 2123
