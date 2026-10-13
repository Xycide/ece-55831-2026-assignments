# ece-55831-2026-assignments
# A_04

Author: Errick Lisk
Class: ECE 55831
Date - 10/13/2026

This folder contains the files required for the 4th assignment in ECE 55831.

### multilayer_perceptron.py
Contains the MultilayerPerceptron class with 4 functions to initialize and perform forward propagation through a neural network. It has 3 input neurons, 3 hidden layers (5, 5, and 2 neurons), and 2 output neurons. Hidden Layers 1-3 use Sigmoid activation while the output layer uses ReLU.

* __init__(self, w1, b1, w2, b2, w3, b3, w4, b4) - Initializes the network's weights and biases with optional parameters
* forward_propagation(self, x) - Performs forward propagation through all layers and returns the output
* sigmoid(self, z) - Applies the sigmoid activation function
* relu(self, z) - Applies the ReLU activation function

### module4.py
Contains 6 functions to create input vectors, intialize the Multilayer Perceptron with random or manually specified weights and biases, and test the network's forward propagation.

* enter_input_vector() - Prompts the user to enter three input values between 0 and 1
* set_input_vector(in1, in2, in3) - Creates an input vector from three specified values
* run_model(model, input_vectors) - Executes forward propagation and prints the results
* random_mlp_weights_and_biases(input_vector) - Tests the network using randomly generated weights and biases
* set_mlp_weights_and_biases(input_vector, w1, b1, w2, b2, w3, b3, w4, b4) - Tests the network using manually specified weights and biases
* main() - Tests the MLP with an example input vector


### module4.ipynb
Jupyter notebook which invokes module4.py to show the forward propagation through the multilayer perceptron. The notebok demonstates:
* Forward propagation with randomly generated weights and biases
* Forward propagation with manually selected weights and biases
* The outputs of each hidden layer and the final output layer
* Verification that the network produces an output shape of (1, 2)