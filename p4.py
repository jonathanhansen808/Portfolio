#project: p4
#submitter: jmhansen7
#partner: none

import pandas as pd

def predict1(glucose, bmi, age):
    if glucose <= 127.5:
        return False
    else:
        return True
    pass
    
def predict2(glucose, bmi, age):
    if glucose <= 127.5:
        return False
    else: 
        if bmi <= 29.95:
            return False
        else:
            return True
    pass
        
from math import *

def column_avg(column_name):
    x = column_sum(column_name)
    y = row_count()
    return x / y
    pass

 
dataset = pd.read_csv("diabetes.csv")


def column_sum(column_name):
    return dataset[column_name].sum()


def row_count():
    return len(dataset)


def predict3(glucose=None, bmi=None, age=None):
    if glucose == None: glucose = column_avg("glucose")
    if bmi == None: bmi = column_avg("bmi")
    if age == None: age = column_avg("age")
    if glucose <= 127.5:
         if age <= 28.5:
                if bmi <= 45.4:
                    return False
                else:
                    return True
         else:
            return False
    elif bmi <= 29.95:
        if glucose <= 145.5:
            return False
        else:
            return True
    return True
    pass

        