#Objective: Introduce Matplotlib Python library
from matplotlib import pyplot as plt #Import basic plot functions

x = [5,2,9,4,7] #X axis values
y = [10,5,8,4,2] #Y axis values
hist = [2,2,2,3,54,6,4,3,2,2,24,5,6] #Histogram values

x2 = 10*x
y2 = 5*y

#plt.plot(x,y) #Plot points on graph
#plt.bar(x,y) #Plot points on bar graph
#plt.hist(hist) #Plot values on histogram
#plt.scatter(x,y) #Plot points on scatter graph

fig = plt.figure(figsize = (25,10)) #Create 25 x 10 figure
ax = fig.add_subplot(111) #
ax.bar(x,y) #Create a bar graph in the subplot
ax.bar(y,x,color = 'red') #Append an additional bar graph in the subplot
ax2 = ax.twinx() #Create a twin axes sharing the xaxis
ax2.plot(hist, color = 'green') #Plot aditional data 

ax.set_xlabel('Test X-axis') #Set the x-axis label
ax.set_ylabel('Test Y-axis') #Set the y-axis label

ax.set_xticks([1,3,5,7,9,11]) #Sets the x-axis tick marks
ax.set_yticks([1,3,5,7,9,11]) #Sets the y-axis tick marks

ax.set_xticklabels(['a','b','c','d','e','f']) #For the x-axis ticks, set a label
ax.set_yticklabels(['g','h','i','j','k','l']) #For the y-axis ticks, set a label

ax.legend(loc = "Upper right",fontsize = 18)

plt.title("Test graph") #Add title to the graph



plt.axvspan(2,10,0.4,0.5) #Add demarkation regions to the graph
plt.axvline(1,0,1) #Adds demarkation line to the graph

plt.gca().invert_xaxis() #Flip graph on x-axis
plt.savefig("result.png") #Save the picture to a file
plt.show() #Display plot