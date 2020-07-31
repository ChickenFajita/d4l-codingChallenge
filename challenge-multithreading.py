import time
import concurrent.futures


def main():
    start = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor(max_workers=500) as executor:
        [executor.submit(mock_send) for _ in range(10)]
        # the manual way showing whats behind the scenes
        # threads = []
        # for _ in range(10):
        #     t = threading.Thread(target=mock_send)
        #     t.start()
        #     threads.append(t)
        # for thread in threads:
        #     thread.join()
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
#   1           50.32
#   2           25.21
#   5           10.09   
#   10          5.05
#   50          1.06
#   100         0.57
#   200         0.53
#   500         0.74

#for 50 mails
#   Workers     Time in second(s)
#   1           25.17
#   2           12.59
#   5           5.05
#   10          2.52
#   50          0.61
#   100         0.53
#   200         0.52
#   500         0.63

#for 10 mails
#   Workers     Time in second(s)
#   1           5.04
#   2           2.52
#   5           1.01
#   10          0.51
#   50          0.51
#   100         0.53
#   200         0.51
#   500         0.51
