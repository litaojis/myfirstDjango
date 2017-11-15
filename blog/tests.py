from django.test import TestCase

import numpy as np


def npSum():
    a = np.array([0,1,2,3,4])
    b = np.array([9,8,7,6,5])

    c = a ** 2 + b ** 3

    return c

print(npSum())

# Create your tests here.

def testRedis():
    from django_redis import get_redis_connection
    get_redis_connection('default').flushall()
    print('No Problem')


if __name__ == 'testRedis':
    testRedis()
