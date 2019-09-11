import json
import calendar
import random
from datetime import date, timedelta

import faker
import numpy as np
from pandas import DataFrame
from delorean import parse
import pandas as pd
import matplotlib

pd.set_option('display.mpl_style', 'default')

fake = faker.Faker()

usernames = set()
usernmaes_no = 1000

while len(usernames)< usernmaes_no:
    usernames.add(fake.user_name())
def get_random_name_and_gender():
    skew = .6
    male = random.random() >skew
    if male:
        return fake.name_male(), 'M'
    else:
        return fake.name_female(), 'F'
def get_users(usernames):
    users = []
    for username in usernames:
        name, gender = get_random_name_and_gender()
        user = {
            'username': username,
            'name': name,
            'gender': gender,
            'email': fake.email(),
            'age': fake.random_int(min=18, max=90),
            'address': fake.address(),
        }
        users.append(json.dumps(user))
    return users
users = get_users(usernames)
users[:3]

    