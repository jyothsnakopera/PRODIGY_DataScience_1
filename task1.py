import pandas as pd
import matplotlib.pyplot as plt

#loading the data
data = pd.read_csv('cancer.csv')

# creating a histogram as the data has most of the continous data
plt.figure(figsize=(8,6))
plt.hist(data['Radius (mean)'], bins=20, edgecolor='black', color='lightgreen')

# Adding labels and title
plt.xlabel('Radius (mean)')
plt.ylabel('Frequency')
plt.title('Distribution of Radius (mean)')

# Showing the plot
plt.grid(True)
plt.show()
