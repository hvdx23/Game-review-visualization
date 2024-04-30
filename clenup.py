import pandas as pd

# Load the data
df = pd.read_csv('review.csv')

# Map 'Feedback' to numerical values: 'Negative' as -1, 'Positive' as 1
df['Score'] = df['Feedback'].map({'Negative': -1, 'Positive': 1})

# Create a new column 'Playtime_Score' that is the product of 'Playtime' and 'Score'
df['Playtime_Score'] = df['Playtime'] * df['Score']

# Save the cleaned DataFrame to a new CSV file
df.to_csv('cleaned_review.csv', index=False)