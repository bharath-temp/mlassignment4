import numpy as np
import os
import math
from random import randint

def kMeans(data,k_Val,epochs):
	 
	randomCenters = []
	 
	for x in range(k_Val):	
		point = randint(0,data.shape[0])
		randomCenters.append(data[point])
		
	
	for y in range(epochs):
	
		clusters = [[] for z in xrange(k_Val)]
		
		for i in range(data.shape[0]):
			distances = []
			
			for j in range(k_Val):
				d = np.linalg.norm(data[i] - randomCenters[j])
				distances.append(d)
				c = min(distances)
			
			clusters[distances.index(c)].append(i)
		
		
		#reset centers
		
		
		for n in range(k_Val):
			print "Cluster %d: %d" % (n,len(clusters[n]))
		
		print "\n"
		
		for k in range(k_Val):
			randomCenters[k] = 0
		
		for z in range(k_Val):
			for val in range(len(clusters[z])):
				randomCenters[z] += data[clusters[z][val]]
			randomCenters[z] = randomCenters[z] / len(clusters[z])
		

def main():

	path = ("./data/data-1.txt")
	data = np.genfromtxt(path,delimiter=',')

	k_Val = 2
	epochs = 10
	
	kMeans(data,k_Val,epochs)
	
main()
