from itertools import groupby
from operator import itemgetter

worker_count = int(input())
for worker in range(worker_count):
    number_of_days = int(input())
    tasks = set()
    flag = True
    days = list(map(int, input().split()))
    grouped_tasks = [(k, sum(1 for i in g)) for k,g in groupby(days)]
    if len(set(map(itemgetter(0), grouped_tasks))) != len(list(map(itemgetter(0), grouped_tasks))):
        print('NO')
    else:
        print('YES')