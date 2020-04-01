import matplotlib.pyplot as pyp
import matplotlib.animation as animation

#Create figure
figure = pyp.figure()

#Create a subplot with 1 row, 1 column and an index of 1
subplot = figure.add_subplot(1,1,1)

#Function will read data from cpu.txt and feed to subplot
def animation_function():

	cpu_data = open("cpu.txt").readlines()

	x=[]

	for each_value in cpu_data:
		if len(each_value) > 1:
			x.append(float(each_value))


	subplot.clear()

	#Plot values in the list
	subplot.plot(x)

#Using the figure, the function and a polling interval of 10000 ms (10 seconds) to build the graph.
graph_animation = animation.FuncAnimation(figure, animation_function, interval = 10000)

#Display graph
pyp.show()