import sys

sys.path.append('.')
import src.Employee


def insert():
    tmp = src.Employee.Employee()
    print(tmp.hire())


insert()
