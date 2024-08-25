import time
start_time = time.time()
delta_time = 0.000001

for i in range(576):
    print(0)
delta_time = time.time() - start_time
print(delta_time)

start_time = time.time()
delta_time2 = 0.000001

for i in range(24):
    for j in range(24):
        print(0)
delta_time2 = time.time() - start_time
print(delta_time)
print(delta_time2)