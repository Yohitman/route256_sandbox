import datetime

t = int(input())
for data_sets in range(t):
    data_set = dict()
    all_times = []
    n = int(input())
    flag = True
    for period in range(n):
        before, after = input().split('-')
        try:
            period_start = datetime.datetime.strptime(before, "%H:%M:%S")
            period_end = datetime.datetime.strptime(after, "%H:%M:%S")
            if period_end < period_start:
                flag = False
                for i in range(period + 1, n):
                    input()
                break
            period_start = period_start.hour*3600+period_start.minute*60+period_start.second
            all_times.append(period_start)
            period_end = period_end.hour*3600+period_end.minute*60+period_end.second
            all_times.append(period_end)
            if period_start not in data_set:
                data_set[period_start] = period_end
            else:
                flag = False
                for i in range(period + 1, n):
                    input()
                break
        except ValueError as e:
            flag = False
            for i in range(period + 1, n):
                input()
            break
    if flag:
        all_times.sort()
        item_value = 0
        for i in range(n):
            item = all_times[i*2]
            if item in data_set.keys():
                if item_value > item:
                    flag = False
                    break
                item_value = data_set[item]
                data_set.pop(item)
                if item_value in data_set.values() or item_value in data_set.keys():
                    flag = False
                    break
                continue
            else:
                flag = False
                break
    if flag:
        print('YES')
    else:
        print('NO')
