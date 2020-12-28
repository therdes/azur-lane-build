# -*- coding: utf-8 -*-
import numpy as np

event_name = ""
special_rates = np.array([2.0, 2.0, 2.5, 2.5]) / 100
total_times = 2000
total_try = 10000

accumulate_special = np.append([0.0], np.cumsum(special_rates))
finish_at = np.array([])

for try_time in range(0, total_try, 1):
    counts_special = np.zeros_like(special_rates)
    i = 0
    for i in range(0, total_times, 1):
        tmp_value = np.random.random(1)
        for j in range(0, len(special_rates), 1):
            if accumulate_special[j] < tmp_value < accumulate_special[j + 1]:
                counts_special[j] = counts_special[j] + 1
        if 0 in counts_special:
            continue
        else:
            break
    finish_at = np.append(finish_at, [i + 1])

print("平均所需建造次数：%d" % (np.mean(finish_at)))
print("毕业所需建造次数(16%%/50%%/84%%)：%d - %d - %d" %
      (np.percentile(finish_at, 16), np.percentile(finish_at, 50), np.percentile(finish_at, 84)))
