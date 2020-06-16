#Objective: Introduce Seaborn for Python
import seaborn as sns #Import necessary for visualizing data
#Seaborn uses matplotlib to draw plots

sns.set() #Apply the default seaborn theme, scaling, and color palettte
tips = sns.load_dataset("tips") #load example dataset
sns.relplot(x="total_bill",y="tip",col="time",
            hue="smoker",style="smoker",size="size",
            data=tips) #Draw a scatter plot

dots = sns.load_dataset("dots") #load example dataset
sns.relplot(x="time",y="firing_rate",col="align",
            hue="choice",style="choice",size="coherence",facet_kws=dict(sharex=False),
            data=dots,kind="line",legend="full") #Draw a line plot
