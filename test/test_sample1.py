import sys
sys.path.append('.')

import src.national_park

def insert():
    tmp = src.national_park.NationalPark()
    print(tmp.add())


insert()
