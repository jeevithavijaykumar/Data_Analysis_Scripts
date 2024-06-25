# browse the folder to find the csv files
# Plot histogram of the combined data set

import pandas as pd
import matplotlib.pyplot as plt
import os

directory = r"C:\Users\jeevi\OneDrive\Desktop\Pandas\test"
dfs =[]

for root,dir,files in os.walk(directory):
    for file in files:
        if file.endswith(".csv"):
            filepath = os.path.join(root,file)
            df1 = pd.read_csv(filepath)
            if 'Feature1' in df1.columns:  # Ensure 'Feature1' exists
                dfs.append(df1)
            dfs.append(df1)

df=pd.concat(dfs)
df.dropna(inplace=True)

# Plot histogram
plt.figure(figsize=(7,5))
ax = plt.hist(df['Feature1'],bins=50,alpha=0.5,color='blue')
counts,bins,patches = plt.hist(df['Feature1'],bins=50,alpha=0.5,color='blue')
for c,b in zip(counts,bins):
    if(c>0):
        plt.annotate(f'{int(c)}',(b,c),ha='center', va='bottom')
plt.xlabel('Feature1')
plt.ylabel('Frequency')
plt.title('Histogram of Feature1')
plt.show()

