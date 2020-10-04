import subprocess as sp
import pymysql.cursors
import config
import sys

sys.path.append('.')
from src.queries import *


def insert():
    tmp = getReportOfSpeciesOfNationalPark().generateReport()
    print(tmp)



