#program5.Write a program to visualize the dataset to gain insigths using matplotlib by plotting scatter plot and bar charts
import pandas as pd
import matplotlib.pyplot as plt

#load the data
data=pd.read_csv('C:/Users/nazmu/Desktop/Machine Learning Python/study_data.csv')
print(data.head())


#Scatter plot of studyHours vs Exam Scores
plt.figure(figsize=(14,7))
plt.subplot(1,2,1)#1 row,2column,1st subplot
plt.scatter(data["Study Hours"], data["Exam Score"], color='dodgerblue', edgecolor='k',
alpha=0.7)
plt.title("Study Hours vs Exam Score")
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.grid(True)

#Bar chart for Average Exam Score by Study Hour range
#creating bins for study hour ranges
bins=[0,2,4,6,8,10,12]
labels=['0-2','2-4','4-6','6-8','8-10','10-12']
data['Study Hours range']=pd.cut(data['Study Hours'],bins=bins,labels=labels,right=False)
grouped_data=data.groupby('Study Hours range')['Exam Score'].mean()
plt.subplot(1,2,2)
grouped_data.plot(kind='bar',color='salmon')
plt.title('average Exam score by Study Hours Range')
plt.xlabel('Study Hours range')
plt.ylabel('Average Exam Score')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
