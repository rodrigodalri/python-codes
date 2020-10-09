'''
author: Rodrigo Dal Ri
email: rodrigodalri1995@gmail.com
'''
from mongoengine import *
import datetime

connect('mongoengine_test', host='localhost', port=27017)

class Post(Document):
    title = StringField(required=True, max_length=200)
    content = StringField(required=True)
    author = StringField(required=True, max_length=50)
    published = DateTimeField(default=datetime.datetime.now)

post_1 = Post(
    title='Sample Post',
    content='Some engaging content',
    author='Scott'
)
post_1.save()       
print(post_1.title)
post_1.title = 'A Better Post Title'
post_1.save()       
print(post_1.title)