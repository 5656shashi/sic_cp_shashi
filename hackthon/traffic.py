

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder, StandardScaler
df = pd.read_csv('Banglore_traffic.csv')
df.fillna(df.median(numeric_only=True), inplace=True)

high_traffic_areas = df[[ 'Area Name','Traffic Volume']].sort_values(by='Traffic Volume', ascending=False).head(5)
print("table for high traffic areas HIGH TO LOW")
print(high_traffic_areas)

plt.figure(figsize=(8,8))
sns.set_style("darkgrid")
sns.barplot(data=high_traffic_areas, y="Traffic Volume", x="Area Name", palette="deep")
plt.ylabel("Traffic Volume")
plt.xlabel("area")
plt.title("Top 5 places wher traffic is more")
plt.show()

change_traffic_congestion= df[['Traffic Volume', 'Congestion Level']].sort_values(by='Congestion Level').head(6)
print("Table for change in traffic level base on congestion LOW TO HIGH")
print(change_traffic_congestion)


plt.figure(figsize=(10,5))
sns.lineplot(data=change_traffic_congestion,x="Traffic Volume",y="Congestion Level",marker="o",color="red",palette="darkgrid")
plt.xlabel("Traffic Volume")
plt.ylabel("Congestion Level")
plt.title("change in traffic based on congestion")
plt.show()

ped_publictransport= df[['Public Transport Usage', 'Pedestrian and Cyclist Count']].sort_values(by='Public Transport Usage').head(5)
print("table pedestrian vs public transport LOW to HIGH")
print(ped_publictransport)


plt.figure(figsize=(10,5))
sns.lineplot(data=ped_publictransport,x="Public Transport Usage",y="Pedestrian and Cyclist Count",marker="*",color="green",palette="darkgrid")
plt.ylabel("Public Transport Usage")
plt.xlabel("Pedestrian and Cyclist Count")
plt.title("variation in public transport based on no of pedestrians")
plt.show()