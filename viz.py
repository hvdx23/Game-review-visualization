import pandas as pd
import matplotlib.pyplot as plt
import mplcursors
import numpy as np
import matplotlib.colors as mcolors

df = pd.read_csv('cleaned_review.csv')

df['Playtime_Score'] = df['Playtime_Score'] + np.random.normal(0, 10, size=len(df))
df['Score'] = df['Score'] + np.random.normal(0, 1, size=len(df))

colors = ["blue", "gray", "red"]

cmap = mcolors.LinearSegmentedColormap.from_list("bgr", colors)

scatter = plt.scatter(df['Playtime'], df['Playtime_Score'], c=df['Playtime_Score'], cmap=cmap)


plt.xlabel('Playtime')
plt.ylabel('Playtime * Score')
plt.title('Scatterplot of Playtime vs Playtime * Score')

sm = plt.cm.ScalarMappable(cmap=scatter.cmap, norm=scatter.norm)
sm.set_array([])

cursor = mplcursors.cursor(scatter)

@cursor.connect("add")
def on_add(sel):
  sel.annotation.set_text(df['Review'].iloc[sel.target.index])


plt.show()