"""Firs API con HUG"""
import hug

@hug.local()
def happy_birthday(name: hug.types.text, age: hug.types.number, hug_timer=3):
    return {'message': 'Happy {0} Birthday {1}!!!'.format(name,age),'took': float(hug_timer)}
