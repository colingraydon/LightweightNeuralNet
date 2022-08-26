#this class will create the basic network of layers

import layer
import tensor
class network:


    def __init__(self, head=None, tail=None):

        self.head = head
        self.tail = tail

    def add_layer(self, l):

        if (self.head == None):
            self.head = l
            self.tail = self.head
        else:
            self.tail.set_next_layer(l)
            l.set_previous_layer(tail)
            tail = l
    
    def run_real(input, test_tensor, optimize, epoch_number):

        epoch_number = 1
        network.head.initialize_input(input)
        current = network.head
        while (current is not network.tail):
            current.propagate_forwards()
            current = current.next_layer
        current.propagate_forwards()
        while (current is not None):
            optimize.propagate_backwards(current, test_tensor, epoch_number)
            current = current.prev_layer

    def run_train(training_iterations, input, test_tensor, optimize):

        epoch_number = 1
        network.head.set_input(input)
        current = network.head
        while (current is not network.tail):
            current.propagate_forward()
            current = current.get_next()

        current.propagage_forward()

        print("Prediction is")
        tensor.print_tensor(current.get_output_tensor())
        print("Actual is")
        tensor.print_tensor(test_tensor)

        i = 0
        while (i < training_iterations):

            network.run_real(input, test_tensor, optimize, epoch_number)
            print("Iteration is", epoch_number)
            epoch_number += 1

        network.head.set_input(input)
        current = network.head
        while (current is not network.tail):
            current.propagate_forward()
            current = current.get_next()
        
        print("Prediction is")
        tensor.print_tensor(current.get_output_tensor())
        print("Actual is")
        tensor.print_tensor(test_tensor)



    

