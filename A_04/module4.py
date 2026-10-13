from multilayer_perceptron import MultilayerPerceptron
import numpy as np
    
def enter_input_vector():
    while True:
        print("Enter three numbers between 0 and 1 for the input vector (separated by spaces):")

        try:
            input_values = [float(x) for x in input().split()]
        except ValueError:
            print("Please enter valid numbers.")
            continue

        if len(input_values) != 3:
            print("Please enter exactly three numbers.")
            continue

        if( any(x < 0 or x > 1 for x in input_values)):
            print("Please enter numbers between 0 and 1.")
            continue

        return np.array([input_values])

def set_input_vector(in1, in2, in3):
    input_vector = np.array([[in1, in2, in3]])
    return input_vector

def run_model(model, input_vector):
    output = model.forward_propagation(input_vector)

    print("Input:", input_vector)
    print("Output of the Multilayer Perceptron:")
    print(output)
    print("Output shape:", output.shape)

    return output

def random_mlp_weights_and_biases(input_vector):
    model = MultilayerPerceptron()

    return run_model(model, input_vector)

def set_mlp_weights_and_biases(input_vector,w1, b1, w2, b2, w3, b3, w4, b4):
    model = MultilayerPerceptron(w1, b1, w2, b2, w3, b3, w4, b4)

    return run_model(model, input_vector)


def main():
    # Define an example input vector
    input_vector = set_input_vector(0.5, 0.2, 0.1)

    # Test the MLP with randomly initialized weights and biases
    random_mlp_weights_and_biases(input_vector)


if __name__ == "__main__":
    main()