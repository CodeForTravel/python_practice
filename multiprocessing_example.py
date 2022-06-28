
import concurrent.futures
import multiprocessing
import time

start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

# p1 = multiprocessing.Process(target=do_something, args=[3])
# p2 = multiprocessing.Process(target=do_something, args=[2])

# p1.start()
# p2.start()
 
# p1.join()
# p2.join()

# processes = []
# for i in range(1,11):
#     p = multiprocessing.Process(target=do_something, args=[i])
#     p.start()
#     processes.append(p)

# for process_ in processes:
#     process_.join()

with concurrent.futures.ProcessPoolExecutor() as process_executor:
    sec_list = [5,4,3,2,1]
    # results = [process_executor.submit(do_something, sec) for sec in sec_list]
    # for f in concurrent.futures.as_completed(results):
    #     print(f.result())

    results = process_executor.map(do_something, sec_list)
    for f in results:
        print(f)


finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')