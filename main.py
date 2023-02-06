import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('movie_info.csv')

#All Brands
x = df['Title']
y = df['Ratings']


plt.title('Best horror movies')
plt.ylabel('Ratings', fontsize=18)
plt.xlabel('Title', fontsize=16)
plt.bar(x,y)
plt.show()