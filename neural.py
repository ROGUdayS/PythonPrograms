import numpy as np
class NeuralNetwork:
    def __init__(self):
        #seeding for random number generation
        np.random.seed(1)
        #Converting weights  to a 3 by 1 matrix with values from -1 to 1 and mean of 0
        self.synaptic_weights=2*np.random((3,1))-1

    def sigmoid(self,x):
        #apply the sigmoid function
        return 1/(1+np.exp(-x))

    def sigmoid_derivative(self,x):
        #Computing derivative to the sigmoid function
        return x*(1-x)

    def train(self,training_input,training_outputs)