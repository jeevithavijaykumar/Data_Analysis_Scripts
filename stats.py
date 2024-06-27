# Statistical analysis
# calculate mean and standard deviation of sensors

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\jeevi\OneDrive\Desktop\Pandas\pre_sensor.csv")
df.columns.tolist()
df_mean = pd.DataFrame(index=[0])
df_stddev = pd.DataFrame(index=[0])

for i in range(10):
    column_name = f'sensor_{i:02d}'
    mean_column = f'mean_sensor_{i:02d}'
    std_dev_column = f'stddev_sensor_{i:02d}'
    if column_name in df.columns.tolist():
        df_mean[mean_column]= df[column_name].mean()
        df_stddev[std_dev_column]=df[column_name].std()
    else:
        print(f'print  {column_name} column does not exist')

df_mean.head(5)
mean_transposed = df_mean.T
mean_transposed.index = [f'sensor_{i:02d}' for i in range(10)]
stddev_transposed = df_stddev.T
stddev_transposed.index = [f'sensor_{i:02d}' for i in range(10)]

plt.figure(figsize=(7,5))
for column in mean_transposed.columns:
    plt.errorbar(mean_transposed.index, mean_transposed[column], yerr=stddev_transposed[column],marker='o',linewidth=0.5,capsize=5,capthick=2)
plt.xlabel('Sensors')
plt.ylabel('Mean Values')
plt.title('sensor Data')
plt.grid(True,linestyle='--')
plt.tight_layout()
plt.show()

######### calculate mean and std dev for three diferent sensors ######
df2 = pd.read_csv(r'')
df3_mean = pd.DataFrame(index=[0])
df4_stddev = pd.DataFrame(index=[0])

for i in range(10):
    column_name = f'sensor_{i:02d}'
    mean_column = f'mean_sensor_{i:02d}'
    stddev_column = f'stddev_sensor_{i:02d}'
    df3_mean[mean_column] = df2.groupby('devicenumber')[column_name].mean()
    df4_stddev[stddev_column] = df2.groupby('devicenumber')[column_name].std()

mean_transposed_three = df3_mean.T
mean_transposed_three.index = [f'sensor_{i:02d}' for i in range(10)]
stddev_transposed_three = df4_stddev.T
stddev_transposed_three.index = [f'sensor_{i:02d}' for i in range(10)]

#define colormap
colors = plt.get_cmap('tab20c').colors
color_map ={
    'device1':colors[0],
    'device2':colors[1],
    'device3' :colors[2]}

plt.figure(figsize=(7,5))
for column in mean_transposed_three.columns:
    device_number = column[0]
    color = color_map.get(device_number)
    plt.errorbar(mean_transposed_three.index, mean_transposed_three[column],yerr=stddev_transposed_three[column],marker='o',capsize=5,capthick=2)
plt.xlabel('Sensors')
plt.ylabel('Mean Values')
plt.title('sensor Data')
plt.grid(True,linestyle='--')
plt.tight_layout()
plt.show()

