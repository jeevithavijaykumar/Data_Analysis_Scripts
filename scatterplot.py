# Use marker size to show intensity
# Use colorbar to show intensity
# Draw Rectangle to highlight high density area

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\jeevi\OneDrive\Desktop\Pandas\tableConvert.com_w113vw.csv")
df.head(5)

df1 = df[df['species']=='setosa'].copy()
df2 = df[df['species']=='versicolor'].copy()
df3= df[df['species']=='virginica'].copy()

# calculate min and max value to determine global clim
minval = df['sepal_length'].min()
maxval = df['sepal_length'].max()

def scatterplot1(df,title):
    top5 = df[['sepal_width', 'petal_width']].value_counts().head(5).index
    min_sepal_width = min(top5, key=lambda x: x[0])[0]
    max_sepal_width = max(top5, key=lambda x: x[0])[0]
    min_petal_width = min(top5, key=lambda x: x[1])[1]
    max_petal_width = max(top5, key=lambda x: x[1])[1]
    rect= [(min_sepal_width-0.05,min_petal_width-0.05),(max_sepal_width+0.05,max_petal_width+0.05)]

    plt.figure(figsize=(10,7))
    ax = plt.gca()
    ax.set_facecolor('dimgray')
    plt.scatter(df['sepal_width'],df['petal_width'],c=df['sepal_length'],marker='o',s=df['sepal_length']*20,vmin=minval,
                vmax=maxval,cmap='viridis',edgecolor='black',label='')
    if rect:
            density_area = plt.Rectangle(rect[0],(rect[1][0]-rect[0][0]),(rect[1][1]-rect[0][1]),color='red',label='High Density area',alpha=1,linewidth=0.8,fill=None)
            ax.add_patch(density_area)
    plt.title(title + ': Scatter plot of Sepal width vs Petal Width')
    plt.xlabel('Sepal Width')
    plt.ylabel('Petal Width')
    plt.grid(True,linestyle='--')
    plt.colorbar(label='sepal length')
    handles,labels = ax.get_legend_handles_labels()
    handles.append(rect)
    labels.append('High Density area')
    ax.legend(handles=handles,labels=labels)
    plt.show()

scatterplot1(df1,'Setosa')
scatterplot1(df2,'Versicolor')
scatterplot1(df3,'Virginica')
