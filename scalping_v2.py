import matplotlib.pyplot as plt
import  random


var = [1, -1]
course_count = 1500
x = list(range(course_count))
y = []
CANDLES_COUNT = 10
y_y = 50
for i in range(course_count):
    y_y = y_y + random.choice(var)
    y.append(y_y)


bots= {
    'v1':{'current':50,'direction':1,'balance':0,'may':1},
    'v2':{'current':'','direction':'','balance':0,'may':0}
}


for i in y:
    if bots.get('v1').get('direction') == '' and bots.get('v1').get('may') == 1 :
        bots.get('v1').update({'direction':random.choice([1,-1])})

    if bots.get('v1').get('current') + bots.get('v1').get('direction') != i:
        bots.get('v1').update({'balance':bots.get('v1').get('balance') - 1,'may':0,'current':i})

        bots.get('v2').update({'current':i,'direction':1 if bots.get('v1').get('direction') == -1 else -1,'may':1})
    elif bots.get('v1').get('current') + bots.get('v1').get('direction') == i:
        bots.get('v1').update({'balance': bots.get('v1').get('balance') + 1,'current':i})


    if bots.get('v2').get('may') == 1:
        if bots.get('v2').get('current') + bots.get('v2').get('direction') != i:
            bots.get('v2').update({'balance': bots.get('v2').get('balance') - 1,'current':i})
        elif bots.get('v2').get('current') + bots.get('v2').get('direction') == i:
            bots.get('v2').update({'balance': bots.get('v2').get('balance') + 1,'current':i})


        if bots.get('v1').get('current') + bots.get('v1').get('direction') != i:
            bots.get('v1').update({'balance': bots.get('v1').get('balance') - 1,'current':i})

        elif bots.get('v1').get('current') + bots.get('v1').get('direction') == i:
            bots.get('v1').update({'balance': bots.get('v1').get('balance') + 1, 'current': i})

print(bots)








