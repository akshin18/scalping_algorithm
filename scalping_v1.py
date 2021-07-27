import matplotlib.pyplot as plt
import  random


OVERALL_RESULT = []

for i in range(20):
    var = [1, -1]
    course_count = 1500
    x = list(range(course_count))
    y = []
    CANDLES_COUNT = 10
    y_y = 50
    for i in range(course_count):

        y_y = y_y + random.choice(var)
        y.append(y_y)

    b = []
    for i in range(len(y)//CANDLES_COUNT):
        print(y[i:i+CANDLES_COUNT])
        summ = []
        for zi in y[i:i+CANDLES_COUNT-1]:
            summ.append(y[i:i + CANDLES_COUNT][-1] - zi)
        b.append([sum(summ),y[i:i + CANDLES_COUNT][-1]])

    count_true = 0

    for i in range(len(b)-1):
        if (b[i][1]-b[i+1][1] < 0 and b[i][0] < 0) or (b[i][1]-b[i+1][1] > 0 and b[i][0] > 0):
            count_true +=1
            print(b[i],b[i][1]-b[i+1][1],True)
        # else:print(b[i],b[i][1]-b[i+1][1],False)
    print('len b='+str(len(b)),'count_true='+str(count_true))
    OVERALL_RESULT.append(count_true)
print(OVERALL_RESULT,str(sum(OVERALL_RESULT)/len(OVERALL_RESULT)/len(b))[:4])
plt.plot(x,y)
plt.show()


