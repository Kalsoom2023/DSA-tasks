import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('Train.csv')
names = df.columns
list1 = []
for i in range(0,len(names)):
        abc = df[names[i]].tolist()
        list1.append(abc)
        list2 = df[names[len(names)-1]].tolist()
        plt.scatter(list1, list2, s=10, c='b', marker="s", label='first')
        plt.show()
    

