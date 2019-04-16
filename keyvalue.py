from sqlitedict import SqliteDict
import time
storage = SqliteDict('./database.sqlite', autocommit=True)
storage['time'] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
# for key, value in storage.iteritems():
#     print(key, value)
print(len(storage))
storage.close()