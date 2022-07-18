t = { 'lesson': [1594663200, 1594666800],'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],'tutor': [1594663290, 1594663430, 1594663443, 1594666473] }
lst_time = []
for k in t:
    ev = t[k]
    for i in range(len(ev)):
        lst_time.append((ev[i], 1 - 2*(i%2)))
lst_time.sort()
value = 0
start = -1
value_time = 0
for e in lst_time:
    value += e[1]
    if value == 3:
        start = e[0]
    if value == 2 and start > 0:
        value_time += e[0] - start
        start = -1
print(value_time)


t = {'lesson': [1594692000, 1594695600], 'pupil': [1594692033, 1594696347], 'tutor': [1594692017, 1594692066, 1594692068, 1594696341]}
lst_time_1 = []
for k in t:
    ev = t[k]
    for i in range(len(ev)):
        lst_time_1.append((ev[i], 1 - 2*(i%2)))
lst_time_1.sort()
cnt = 0
start = -1
value_time_1 = 0
for e in lst_time_1:
    cnt += e[1]
    if cnt == 3:
        start = e[0]
    if cnt == 2 and start > 0:
        value_time_1 += e[0] - start
        start = -1
print(value_time_1)


