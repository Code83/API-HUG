import hug

@hug.cli
@hug.get(examples='name=Gonzalo&age=37')
@hug.local()

def happy_birthday(name:hug.types.text, age:hug.types.number, hug_timer=3):
    return {'message': 'Feliz {0} cumple {1}!'.format(age, name),'took': float(hug_timer)}

if __name__=='__main__':
    happy_birthday.interface.cli    