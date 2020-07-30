import time
import concurrent.futures

start = time.perf_counter()

def mock_send(i):
    print(f'Thread {i}: sending for half a second..')
    time.sleep(0.5)
    print(f'Thread {i}: sent!')

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = [executor.submit(mock_send,i) for i in range(10)]

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