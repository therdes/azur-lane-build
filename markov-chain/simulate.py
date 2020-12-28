import numpy as np

event_name = ""
special_rates = np.array([2.0, 2.0, 2.5, 2.5]) / 100
total_times = 1000

num_new_ships = len(special_rates)
p_rates = np.append(special_rates, 1 - np.sum(special_rates))
p_accu_rates = np.zeros((total_times + 1, 2 ** num_new_ships))
p_accu_rates[0][0] = 1

count = 0
