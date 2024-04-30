import pandas as pd
import matplotlib.pyplot as plt
import mplcursors
import numpy as np
import matplotlib.colors as mcolors
from matplotlib.colors import TwoSlopeNorm

df = pd.read_csv('cleaned_review.csv')

df['Playtime_Score'] = df['Playtime_Score'] + np.random.normal(0, 10, size=len(df))
df['Score'] = df['Score'] + np.random.normal(0, 1, size=len(df))


colors = ["red", "yellow", "green"]


cmap = mcolors.LinearSegmentedColormap.from_list("ryg", colors)

vmin = df['Playtime_Score'].min()
vmax = df['Playtime_Score'].max()
divnorm = TwoSlopeNorm(vmin=vmin, vcenter=0, vmax=vmax)


scatter = plt.scatter(df['Playtime'], df['Playtime_Score'], c=df['Playtime_Score'], cmap=cmap, norm=divnorm)

plt.xlabel('Playtime')
plt.ylabel('Imperession')
plt.title('Scatterplot of Playtime vs Impression')


sm = plt.cm.ScalarMappable(cmap=scatter.cmap, norm=scatter.norm)
sm.set_array([])  # Set empty array to avoid data range issues


cursor = mplcursors.cursor(scatter)

@cursor.connect("add")
def on_add(sel):
  sel.annotation.set_text(df['Review'].iloc[sel.target.index])

plt.show()