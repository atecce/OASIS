# MarsOASIS Deep Neural Network 
## Used for visual classification of plant health based on overhead images of the grow bed

#### Warning: The images in the training and testing image directories are not representative of the grow bed, and should be replaced with actual photographs of lettuce in the system.

### Setup

The code has three dependencies:

	- glob, for file management
	- numpy for all the matrix computations 
	- PIL for image processing

You should probably already have glob and numpy installed, so you can just run:
```pip install pillow``` 

or

```easy_install pillow```

to download and install PIL.

### Running the network

Simply type:
```python neural_net.py```

The network will load in all the images, converting them to matrices of activation values between 0 and 1. 

Then, the network will build itself, outputting information about the size of the layer and synapse matrices.

After performing an initial test, the network will begin training, outputting the current error every 100 epochs. 

One epoch represents a complete forward and backward pass for all training images.

### Loading weights

After training, the network saves the learned weights to files in the main directory. These files can be loaded at runtime instead of generating new random weights, though currently the network learns so fast that this feature is unecessary. 

### Example Output

```
loading training data...
training_images/alive_1.jpg loaded
training_images/alive_2.jpg loaded
training_images/alive_3.jpg loaded
training_images/alive_4.jpg loaded
training_images/alive_5.jpg loaded
training_images/alive_6.jpg loaded
training_images/alive_7.jpg loaded
training_images/dead_1.jpg loaded
training_images/dead_2.jpg loaded
training_images/dead_3.jpg loaded
training_images/dead_4.jpg loaded
training_images/dead_5.jpg loaded
training_images/dead_6.jpg loaded
13
input training: (13, 1024)
output training: (13, 1)
syn0 (1024, 13)
syn1 (13, 1)
testing...
Error: 0.509492516465

training...
training for 100,000 epochs...
Epoch: 0 Error: 0.509492516465
Epoch: 100 Error: 0.433446269635
Epoch: 200 Error: 0.160453456373
Epoch: 300 Error: 0.044201279765
Epoch: 400 Error: 0.024638233989
Epoch: 500 Error: 0.0179077222164
Epoch: 600 Error: 0.0146248851714
Epoch: 700 Error: 0.0125913795081
Epoch: 800 Error: 0.0112362943558
Epoch: 900 Error: 0.0102555162981
Epoch: 1000 Error: 0.00949941338326
```

