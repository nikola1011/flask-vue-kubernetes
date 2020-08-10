import sys
import requests
import threading
from threading import Thread
from queue import Queue

concurrent = 10

def doWork():
    print(f'Running work with thread id: {threading.get_ident()}')
    while True:
        url = q.get()
        ret = requests.get(url)
        doSomethingWithResult(ret, url)
        q.task_done()

# def getStatus(ourl):
#     try:
#     except:
#         return "error", ourl

def doSomethingWithResult(result, url):
    print(result, url)
    print(result.text)

q = Queue(concurrent * 2)
for i in range(concurrent):
    t = Thread(target=doWork)
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
