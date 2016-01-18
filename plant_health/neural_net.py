#usr/bin/env python

from PIL import Image
import random
import glob
import math
import os

class Neuron():
	def __init__(self):
		self.act = None
		self.inputConnections = []
		self.hiddenConnections = []
		self.outputConnections = []

class NeuralNetwork():
	def __init__(self):
		self.inputLayer = []
		self.hiddenLayer = []
		self.outputLayer = []
		self.inputActivations = []
		self.hiddenActivations = []
		self.outputActivations = []
		self.epochError = 0
		self.epochs = 0
		self.stateList = []

	def makeNetwork(self):
		for input_node in range(1024): #training images are 32 x 32, these represent 1024 feature detectors
			self.inputLayer.append(Neuron())
		for hidden_node in range(512): #arbitrary number of hidden units
			self.hiddenLayer.append(Neuron())
		for output_node in range(2): #alive or dead
 			self.outputLayer.append(Neuron())

	def genInputActivations(self):
		for file_ in glob.glob("training_images/*"):
			plant = Image.open(file_)
			pix = list(plant.getdata())
			activation = []
			for pixel in pix:
				hexval = hex(pixel[0]) + hex(pixel[1])[:1] + hex(pixel[2])[:1]
				activation.append((int(hexval,16))/100000.0)
			self.inputActivations.append((activation,file_[16:-4]))

	def sigmoid(self,activation):
		try:
			return 1 / (1 + math.exp(-activation))
		except OverflowError:
			return 0

	def hiddenActivationFunction(self,node,index):
		xw = 0
		for input_node in self.inputLayer:
			xw += input_node.hiddenConnections[index] * float(input_node.act)
		return self.sigmoid(xw)

	def outputActivationFunction(self,node,index):
		f = 0
		for hidden_node in self.hiddenLayer:
			f += hidden_node.outputConnections[index] * float(hidden_node.act)
		return self.sigmoid(f)

	def getplant(self,node):
		if node == self.outputLayer[0]:
			return "alive"
		elif node == self.outputLayer[1]:
			return "dead"

	def getExpected(self,node,plant):
		if "alive" in plant[1]:
			if node == self.outputLayer[0]:
				return 1
			else:
				return 0
		elif "dead" in plant[1]:
			if node == self.outputLayer[1]:
				return 1
			else:
				return 0

	def trainingEpoch(self):
		file_ = 0
		for plant in self.inputActivations:
			output = self.minusPhase(plant)
			if self.plusPhase(plant,output) == False:
				self.epochError += 1

	def minusPhase(self,plant):
		#FORWARD
		input_counter = 0
		for input_node in self.inputLayer:
			input_node.act = plant[0][input_counter]
			input_counter += 1
		hiddenConnection = 0
		for hidden in self.hiddenLayer:
			hidden.act = self.hiddenActivationFunction(hidden,hiddenConnection)
			hiddenConnection += 1
		outputConnection = 0
		layerActivity = []
		for output in self.outputLayer:
			output.act = self.outputActivationFunction(output,outputConnection)
			layerActivity.append((output,output.act))
			outputConnection += 1
		return max(layerActivity, key = lambda x: x[1])

	def checkMinusPhaseOutput(self,plant,minusPhaseOutput):
		expected = self.getExpected(minusPhaseOutput[0],plant)
		plant_ = self.getplant(minusPhaseOutput[0])
		correct = False
		if plant_ in plant[1]:
			correct = True
		print correct
		print plant[1], plant_
		return correct, plant_

	def plusPhase(self,plant,minusPhaseOutput):
		correct, plant_ = self.checkMinusPhaseOutput(plant,minusPhaseOutput)
		print correct, plant_
		#BACKPROPAGATION
		outputCounter = 0
		for output in self.outputLayer:
			error = self.getExpected(output,plant) - output.act
			print error
			hiddenCounter = 0
			for hidden in self.hiddenLayer:
				#the change in weights for each output/hidden connection are:
					#the error for the output node (expected - output) multiplied by the activation of the unit
				new_weight = (hidden.act * error) + output.hiddenConnections[hiddenCounter]
				output.hiddenConnections[hiddenCounter] = new_weight
				hidden.outputConnections[outputCounter] = new_weight
				inputCounter = 0
				for input_ in self.inputLayer:
					#the change in weights for each input node are:
						#the sum over all hidden units of:
							#the expected output multiplied by the weight for the hidden/input pair
						#minus the sum over all hidden units of:
							#the output unit's activation multiplied by the weight for the hidden/input pair
						#multiplied by yprime????
							#I think y prime is the activation of the hidden layer unit
					backprop_counter = 0
					tw = 0
					zw = 0
					for output_backprop in self.outputLayer:
						weight = output_backprop.hiddenConnections[hiddenCounter]
						tw += self.getExpected(output_backprop,plant) * weight
						zw += output_backprop.act * weight
						backprop_counter += 1
					new_weight = ((tw - zw) * (hidden.act * (1 - hidden.act) * input_.act)) + hidden.inputConnections[inputCounter]
					hidden.inputConnections[inputCounter] = new_weight
					input_.hiddenConnections[hiddenCounter] = new_weight
					inputCounter += 1
				hiddenCounter += 1
			outputCounter += 1
		if correct == False:
			return False
		else:
			return True

	def initializeRandomWeights(self):
		for input_node in self.inputLayer:
			for hidden_node in self.hiddenLayer:
				randomWeight = random.uniform(-1,1)
				#input_node.hiddenConnections.append((hidden_node,randomWeight))
				input_node.hiddenConnections.append(randomWeight)
				#hidden_node.inputConnections.append((input_node,randomWeight))
				hidden_node.inputConnections.append(randomWeight)
		for hidden_node in self.hiddenLayer:
			for output_node in self.outputLayer:
				randomWeight = random.uniform(-1,1)
				#hidden_node.outputConnections.append((output_node,randomWeight))
				hidden_node.outputConnections.append(randomWeight)
				#output_node.hiddenConnections.append((hidden_node,randomWeight))
				output_node.hiddenConnections.append(randomWeight)

	def loadWeights(self):
		file_ = raw_input("Enter name of weights file: ")
		file_ = open(file_,"r")
		weights = []
		for weight in file_:
			weights.append(float(weight))
		file_.close()
		for input_node in self.inputLayer:
			for hidden_node in self.hiddenLayer:
				#input_node.hiddenConnections.append((hidden_node,weights[0]))
				input_node.hiddenConnections.append(weights[0])
				#hidden_node.inputConnections.append((input_node,weights[0]))
				hidden_node.inputConnections.append(weights[0])
				weights.pop(0)
		for hidden_node in self.hiddenLayer:
			for output_node in self.outputLayer:
				#hidden_node.outputConnections.append((output_node,weights[0]))
				hidden_node.outputConnections.append(weights[0])
				#output_node.hiddenConnections.append((hidden_node,weights[0]))
				output_node.hiddenConnections.append(weights[0])
				weights.pop(0)

	def train(self):
		self.epochError = 0
		self.trainingEpoch()
		self.epochs += 1
		print "Epoch:", self.epochs, "Error:", 100 * float(self.epochError)/float(len(self.inputActivations))
		if self.epochError < 1:
			return
		else:
			return self.train()

	def test(self):
		trial = 0
		for activation, plant in self.inputActivations:
			print "\nTrial: ", trial
			print "plant: ", plant[:-2]
			print "Gender: ", plant[-1:]
			output = self.minusPhase((activation,plant))
			correct, plant_ = self.checkMinusPhaseOutput((activation,plant),output)
			if correct == True:
				print "Correct!", "Output: ", plant_
			else:
				print "Test failed.", "Output: ", plant_
			trial += 1

	def saveWeights(self):
		weights = open(raw_input("Enter file name: "),"w")
		for node in self.inputLayer:
			for connection in node.hiddenConnections:
				weights.write(str(connection))
				weights.write("\n")
		for node in self.hiddenLayer:
			for connection in node.outputConnections:
				weights.write(str(connection))
				weights.write("\n")
		weights.close()

	def saveRFs(self):
		rf_counter = 0
		for output in self.outputLayer:
			rf = open("output_unit_receptive_fields/"+str(rf_counter)+".data","w")
			for weight in output.hiddenConnections:
				rf.write(str(weight))
				rf.write("\n")
			rf.close()
			rf_counter += 1

def main():
	#net = NeuralNetwork()
	net.makeNetwork()
	print "generating input activations...\n"
	net.genInputActivations()
	if raw_input("Would you like to load weights? (y/n) ") == "y":
		print "loading weights...\n"
		net.loadWeights()
	else:
		print "initializing random weights...\n"
		net.initializeRandomWeights()
	try:
		print "beginning training...\n"
		net.train()
		print "Success!"
		print "Error across 100 epochs: ", net.epochError
		print "Epochs to convergence:", net.epochs
	except:
		print "training failed"
	print "testing network...\n"
	net.test()
	if raw_input("Would you like to save the network's weights? (y/n) ") == "y":
		net.saveWeights()
	print "weights saved\n"
	net.saveRFs()

if __name__=="__main__":
	net = NeuralNetwork()
	main()
