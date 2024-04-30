import pandas as pd
import matplotlib.pyplot as plt
import mplcursors

df = pd.read_csv('review.csv')

scatter = plt.scatter(df['Playtime'], df['Score'], c=df['Score'])

plt.xlabel('Playtime')
plt.ylabel('Score')
plt.title('Scatterplot of Playtime vs Score')

# Use mplcursors to add interactivity
cursor = mplcursors.cursor(scatter)

@cursor.connect("add")
def on_add(sel):
    sel.annotation.set_text(df['Review'].iloc[sel.target.index])

plt.show()