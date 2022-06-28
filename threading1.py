import time
import threading
import concurrent.futures
execution_start_time = time.perf_counter()

def my_function(seconds):
    print(f"Sleep for {seconds} second(s)")
    time.sleep(seconds)
    return f"Done sleeping...{seconds}"

# print(my_function(5))
# print(my_function(3))

# t1 = threading.Thread(target=my_function, args=[5])
# t2 = threading.Thread(target=my_function, args=[3])
# t1.start()
# t2.start()
# t1.join()
# t2.join()


# threads = []

# for _ in range(10):
#     t = threading.Thread(target=my_function, args=[3])
#     t.start()
#     threads.append(t)

# for thread in threads:
#     thread.join()

with concurrent.futures.ThreadPoolExecutor() as executor:
    seconds = [2,4,1,6,3]
    results = executor.map(my_function, seconds)

    for result in results:
        print(result)


execution_end_time = time.perf_counter()
print(f'Finished in {round(execution_end_time-execution_start_time, 2)} second(s)')
