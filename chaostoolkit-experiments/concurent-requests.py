import sys
import requests
import threading
from threading import Thread
from queue import Queue

CONCURRENT_REQUESTS = 9000

def make_a_request():
    # print(f'Running work with thread id: {threading.get_ident()}')
    while True:
        url = q.get()
        ret = requests.get(url)
        parse_result(ret, url)
        q.task_done()

def parse_result(result, url):
    print(result, url, result.text)

q = Queue(CONCURRENT_REQUESTS * 2)
for i in range(CONCURRENT_REQUESTS):
    t = Thread(target=make_a_request)
    t.daemon = True
    t.start()
try:
    URL = 'http://check.alive/books'
    q.put(URL.strip())
    q.join()
except KeyboardInterrupt:
    sys.exit(1)
sys.exit(0)


# import sys

# def printFunc(myArgument=1000):
#     print(f"My argument is: {myArgument}")
#     # Print to stderr
#     #print('blabla', file=sys.stderr)
#     return myArgument           

# printFunc()
# sys.exit(0)
