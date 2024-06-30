# Box plot
# transform data from wide format to long format
# find max, min and mean values by operations

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\jeevi\OneDrive\Desktop\Pandas\pre_sensor.csv")
df.head(5)
#trnasforms data from wide format to long format
df_mini = pd.melt(df,id_vars=['operation','timestamp'],value_vars=['sensor_00','sensor_01',
                                'sensor_02','sensor_03','sensor_04','sensor_05','sensor_06',
                                'sensor_07','sensor_08','sensor_09','sensor_10'],
                              var_name='sensors',value_name='value')
# Boxplot
plt.figure(figsize=(7,5))
sns.boxplot(data=df_mini,x='sensors',y='value',palette='Paired',width=0.3,hue='operation')
plt.xlabel('sensors')
plt.ylabel('values')
plt.title('sensor data')
plt.grid(True,linestyle='--')
plt.legend(title='operation')
plt.show()

# find max, min and median values
df['max_val']= df.groupby('operation')['sensor_00'].transform('max')
df['min_val'] = df.groupby('operation')['sensor_00'].transform('min')
df['mean_val']=df.groupby('operation')['sensor_00'].transform('mean')
print('Max value by operation are \n',df[['max_val','operation']].value_counts())
print('Min value by operation are \n',df[['min_val','operation']].value_counts())
print('Mean value by operation are \n',df[['mean_val','operation']].value_counts())
