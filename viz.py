import pandas as pd
import matplotlib.pyplot as plt
import mplcursors
import numpy as np
import matplotlib.colors as mcolors

# Load the data
df = pd.read_csv('cleaned_review.csv')

# Add random noise to 'Playtime_Score' and 'Score'
df['Playtime_Score'] = df['Playtime_Score'] + np.random.normal(0, 10, size=len(df))
df['Score'] = df['Score'] + np.random.normal(0, 1, size=len(df))

# Define the colors for the colormap
colors = ["blue", "gray", "red"]

# Create the colormap
cmap = mcolors.LinearSegmentedColormap.from_list("bgr", colors)

# Create a scatter plot with 'Playtime' on the x-axis and 'Playtime_Score' on the y-axis
scatter = plt.scatter(df['Playtime'], df['Playtime_Score'], c=df['Playtime'], cmap=cmap)

# Add labels and title
plt.xlabel('Playtime')
plt.ylabel('Playtime * Score')
plt.title('Scatterplot of Playtime vs Playtime * Score')

# Colorbar adjustment
sm = plt.cm.ScalarMappable(cmap=scatter.cmap, norm=scatter.norm)
sm.set_array([])  # Set empty array to avoid data range issues
plt.colorbar(sm, label='Playtime', ax=plt.gca())  # Create colorbar with label 'Playtime'

# Use mplcursors to add interactivity
cursor = mplcursors.cursor(scatter)

@cursor.connect("add")
def on_add(sel):
  sel.annotation.set_text(df['Review'].iloc[sel.target.index])

# Show the plot
plt.show()