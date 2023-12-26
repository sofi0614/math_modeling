import time

timer = time.time()
for i in range(10):
    print(i)
    time.sleep(1)

print(f'{time.time(1) - timer}, seconds')