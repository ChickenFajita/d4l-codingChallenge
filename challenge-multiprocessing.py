import time
import multiprocessing
import concurrent.futures

def main():
    start = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor(max_workers=200) as executor:
        [executor.submit(mock_send) for _ in range(10)]

        # processes = []
        # for _ in range(10):
        #     p = multiprocessing.Process(target=mock_send)
        #     p.start()
        #     processes.append(p)
        # for process in processes:
        #     process.join()
    finish = time.perf_counter()
    print(f'Finished in {round(finish-start, 2)} seconds')

def mock_send():
    print('Sending for half a second..')
    time.sleep(0.5)
    print('Sent!')

if __name__ == '__main__' :
    main()

#for 100 mails
#   Workers     Time in second(s)
#   1           50.64
#   2           25.63
#   5           10.57 
#   10          6.08
#   50          6.08
#   100         15.21

#for 50 mails
#   Workers     Time in second(s)
#   1           25.47
#   2           12.94
#   5           3.29
#   10          2.52
#   50          3.26

#for 10 mails
#   Workers     Time in second(s)
#   1           5.19
#   2           2.82
#   5           1.32
#   10          1.31
#   50          2.58
#   100         4.71
#   200         9.25