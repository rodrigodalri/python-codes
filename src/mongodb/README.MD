# mongodb

Code for playing with mongodb.

Features:
- pymongo
- mongoengine

Checking funcionality
```
$ python3 mongo.py 
One post: 5f80eb24cdb00ad722f86e75
Multiple posts: [ObjectId('5f80eb24cdb00ad722f86e76'), ObjectId('5f80eb24cdb00ad722f86e77'), ObjectId('5f80eb24cdb00ad722f86e78')]
{'_id': ObjectId('5f80ea96eae22b9f685803f9'), 'title': 'Learning Python', 'content': 'Learn Python, it is easy', 'author': 'Bill'}
<pymongo.cursor.Cursor object at 0x7f0572e8a430>

$ python3 engine.py 
Sample Post
A Better Post Title
```