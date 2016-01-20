import glob
import numpy as np
from PIL import Image

class NeuralNetwork():

        # 3 layer deep network

	# training matrices
	input_training_matrix  = list()
	output_training_matrix = list()

    	def __init__(self):
        	
		self.training_size = 0
		self.loadTrainingData()
		
		#good practice to seed random numbers
		np.random.seed(1)

		# synapses
		# randomly initialize weights with mean 0
		self.syn0 = 2*np.random.random((1024,self.training_size)) - 1 # weights connecting input and hidden layers
		self.syn1 = 2*np.random.random((self.training_size,1)) - 1    # weights connecting hidden and output layers
		
		#self.syn0 = np.load('syn0_weights')
		#self.syn1 = np.load('syn1_weights')

	def saveWeights(self):
		with open("syn0_weights", "w") as weights1:
			np.save(weights1, self.syn0) 
		with open("syn1_weights", "w") as weights2:
			np.save(weights2, self.syn1) 

    	def loadTrainingData(self):
        	for file_ in glob.glob("training_images/*"):
			print file_
			plant = Image.open(file_)
			pix = list(plant.getdata())
			activation = []
			for pixel in pix:
				hexval = hex(pixel[0]) + hex(pixel[1])[:1] + hex(pixel[2])[:1]
				activation.append((int(hexval,16))/100000.0)
            		self.input_training_matrix.append(activation)
			if "alive" in file_:
            			self.output_training_matrix.append([0])
            		else:
                		self.output_training_matrix.append([1])
		self.training_size = len(self.input_training_matrix)
		print self.training_size
            	self.input_training_matrix = np.array(self.input_training_matrix)
        	self.output_training_matrix = np.array(self.output_training_matrix)

	def sigmoid(self,x,deriv=False):
		if(deriv==True):
	    		return x*(1-x)
		return 1/(1+np.exp(-x))

	def train(self):
		for epoch in xrange(10000000):
			input_layer  = self.input_training_matrix
			# multiply input_layer and syn0 matrices, 
			# passes product into sigmoid activation function
			# (20 x 1024) dot (1024 x 20) = (20 x 20)?
			hidden_layer  = self.sigmoid(np.dot(input_layer,self.syn0))
			# (20 x 20) dot (1 x 20) = ????????
			output_layer = self.sigmoid(np.dot(hidden_layer,self.syn1))
			# calculating error
			output_layer_error = self.output_training_matrix - output_layer
			if epoch % 100000 == 0:
				print "Epoch:", epoch, "Error:", str(np.mean(np.abs(output_layer_error)))
			
			# in what direction is the target value?
  			# were we really sure? if so, don't change too much.
    			output_layer_delta = output_layer_error*self.sigmoid(output_layer,deriv=True)

    			# how much did each hidden_layer value contribute to the output_layer error (according to the weights)?
    			hidden_layer_error = output_layer_delta.dot(self.syn1.T)

    			# in what direction is the target hidden_layer?
   			# were we really sure? if so, don't change too much.
    			hidden_layer_delta = hidden_layer_error * self.sigmoid(hidden_layer,deriv=True)

   			self.syn1 += hidden_layer.T.dot(output_layer_delta)
   			self.syn0 += input_layer.T.dot(hidden_layer_delta)





net = NeuralNetwork()
print "input training:", net.input_training_matrix.shape
print "output training:", net.output_training_matrix.shape
print "syn0", net.syn0.shape
print "syn1", net.syn1.shape

print "testing..."

try:
	print "training..."
	net.train()
except KeyboardInterrupt:
	net.saveWeights()
	print "weights saved"
net.saveWeights()
print "weights saved"

