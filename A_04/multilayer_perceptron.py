#Input Layer: 3 neurons
#Hidden Layer 1: 5 neurons
#Hidden Layer 2: 5 neurons
#Hidden Layer 3: 2 neurons
#Output Layer: 2 neuron

#Activation Functions:
#   Layers 1-3: Sigmoid
#   Layer 4: ReLU

#Weights and Biases: you may choose

#Implementation should include the forward propagation process from the input layer to the output layer

import numpy as np

class MultilayerPerceptron:
    def __init__(self, w1=None, b1=None, w2=None, b2=None, w3=None, b3=None, w4=None, b4=None):
        parameters = (w1, b1, w2, b2, w3, b3, w4, b4)
        if all(p is None for p in parameters):
            self.w1 = np.random.rand(3, 5)
            self.b1 = np.random.rand(1, 5)
            self.w2 = np.random.rand(5, 5)
            self.b2 = np.random.rand(1, 5)
            self.w3 = np.random.rand(5, 2)
            self.b3 = np.random.rand(1, 2)
            self.w4 = np.random.rand(2, 2)
            self.b4 = np.random.rand(1, 2)
        elif any(p is None for p in parameters):
            raise ValueError("Either provide all weights and biases or none.")
        else:
            self.w1 = np.array(w1, dtype=float)
            self.b1 = np.array(b1, dtype=float)
            self.w2 = np.array(w2, dtype=float)
            self.b2 = np.array(b2, dtype=float)
            self.w3 = np.array(w3, dtype=float)
            self.b3 = np.array(b3, dtype=float)
            self.w4 = np.array(w4, dtype=float)
            self.b4 = np.array(b4, dtype=float)


    def forward_propagation(self, x):
        z1 = x @ self.w1 + self.b1
        a1 = self.sigmoid(z1)

        z2 = a1 @ self.w2 + self.b2
        a2 = self.sigmoid(z2)

        z3 = a2 @ self.w3 + self.b3
        a3 = self.sigmoid(z3)

        z4 = a3 @ self.w4 + self.b4
        a4 = self.relu(z4)

        print("Hidden Layer 1:", a1)
        print("Hidden Layer 2:", a2)
        print("Hidden Layer 3:", a3)
        print("Output Layer:", a4)

        return a4

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def relu(self, z):
        return np.maximum(0, z)