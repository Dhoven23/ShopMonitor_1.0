import matplotlib.pyplot as plt
from Data.day import Day
import numpy as np


def plotins():
    X = []
    Y = []
    labels = []
    t = []
    t1=[]
    t2 = []
    n = 0
    for day in Day.objects:
        n += 1
        t.append(n)

        t1.append(n-0.2)
        t2.append(n+0.2)

        X.append(day.logs)
        Y.append(day.capstone_logs)
        labels.append(day.date[5:10])
    ax = plt.subplot()

    m = 20

    t = t[-m:]
    t1 = t1[-m:]
    t2 = t2[-m:]
    X = X[-m:]
    Y = Y[-m:]
    labels = labels[-m:]
    normal = ax.bar(t1, X, width=0.4, label = 'normal',color='blue')

    capstone = ax.bar(t2, Y, width=0.4, label = 'Capstone',color='orange')

    plt.title('Daily users',fontsize=20)
    plt.xticks(t, labels, rotation=45)
    plt.legend(handles = [capstone, normal])
    plt.ylabel('Students')
    plt.show()


liszt = [1, 2, 3, 4, 5, 6, 7, 8]
n = 5
lis = liszt[-n:]
