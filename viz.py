import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('review.csv')


plt.scatter(df['Playtime'], df['Score'], c=df['Score'])


plt.xlabel('Playtime')
plt.ylabel('Score')
plt.title('Scatterplot of Playtime vs Score')


plt.show()