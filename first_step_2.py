import hug

@hug.get(examples='name=Gonzalo&age=37')
@hug.local()

def happy_birthday(name: hug.types.text, age: hug.types.number, hug_timer=3):
    return {'message': 'Happy {0} birthday {1}!!!'.format(age,name),'took':float(hug_timer) } 
    