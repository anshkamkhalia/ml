import pandas as pd
import numpy as np
import tensorflow.keras.datasets.fashion_mnist as tf # ONLY FOR DATA LOADING I PROMISE
import tensorflow.keras.utils as tf2 # FOR ENCODING

class NeuralNetwork:
    """
    A Neural Network built to predict 28x28 pixel grayscale images of various pieces of clothing.

    Structure:
        - Input layer (784 neurons)
        - Dense layer (128 nuerons, activation=relu -> Rectified Linear Unit)
        - Dense layer (64 nuerons, activation=relu -> Rectified Linear Unit)
        - Output layer (10 nuerons, activation=softmax -> To squish the values between 0 and 1 (probability distributions))

    """

    def __init__(self):
        
        (self.X_train_raw, self.y_train), (self.X_test_raw, self.y_test) = tf.load_data()
        self.X_train = self.X_train_raw/255.0
        self.X_test = self.X_test_raw/255.0

        self.X_train = self.X_train.reshape(-1, 784) # Flattens the array
        self.X_test = self.X_test.reshape(-1, 784)

        # Weights and biases for each layer
        self.W1 = np.random.randn(128, 784) * np.sqrt(2 / 784)
        self.b1 = np.zeros((128, 1))

        self.W2 = np.random.randn(64, 128) * np.sqrt(2 / 128)
        self.b2 = np.zeros((64, 1))

        self.W3 = np.random.randn(10, 64) * np.sqrt(2 / 64)
        self.b3 = np.zeros((10, 1))

        # Labels
        self.fashion_labels = {
                0: "T-shirt/top",
                1: "Trouser",
                2: "Pullover",
                3: "Dress",
                4: "Coat",
                5: "Sandal",
                6: "Shirt",
                7: "Sneaker",
                8: "Bag",
                9: "Ankle boot"
            }
        
        # IMPORTANT - Saves each "version" of the model
        self.best_model = None
        self.best_loss = float('inf')


        # Creating an array of labels with the string representation
        self.y_train_string = np.array(list(map(lambda item: self.fashion_labels.get(item, item), self.y_train)))
        self.y_test_string = np.array(list(map(lambda item: self.fashion_labels.get(item, item), self.y_test)))
    
    @staticmethod
    def relu(x): # For dense layers
        return np.maximum(0, x)

    @staticmethod
    def softmax(x): # For output layer to get probability distributions
        e_x = np.exp(x - np.max(x))
        return e_x / e_x.sum(axis=0)
    
    @staticmethod
    def cross_entropy(predictions, targets):
        """
        The loss function of the model
        """
        # predictions and targets shape: (n_classes, batch_size)
        # Add a tiny epsilon to avoid log(0)
        epsilon = 1e-12
        predictions = np.clip(predictions, epsilon, 1. - epsilon)
        return -np.sum(targets * np.log(predictions)) / predictions.shape[1]

    def fit(self, epochs=10, alpha=0.01, batch_size=100):
        """
        Fits the neural network to the data using backpropagation
        args: 
            epochs = number of times looped over the training data
            alpha = learning rate
            batch_size = Size of batches the model is trained on each epoch
        """

        self.epochs = epochs
        self.alpha = alpha
        self.batch_size = batch_size

        # THIS IS ONLY TO ENCODE I SWEAR
        # Log loss needs encoded labels
        self.y_train = tf2.to_categorical(self.y_train, num_classes=10)
        self.y_test = tf2.to_categorical(self.y_test, num_classes=10)

        # Main training loop
        for epoch in range(self.epochs):
        
            # Get indices
            self.n_samples = self.X_train.shape[0]
            permutation_indices = np.random.permutation(self.n_samples)

            # Shuffle data
            self.X_train_shuffled = self.X_train[permutation_indices]
            self.y_train_shuffled = self.y_train[permutation_indices]
            
            # Mini batching
            for start in range(0, self.n_samples, self.batch_size):

                # Create batches
                self.stop = start + self.batch_size

                # Train on these batches
                self.X_batch = self.X_train_shuffled[start:self.stop] 
                self.y_batch = self.y_train_shuffled[start:self.stop]

                # Forward pass
                self.A0 = self.X_batch.T             

                # Forward propagation
                self.Z1 = self.W1 @ self.A0 + self.b1
                self.A1 = self.relu(x=self.Z1)          

                self.Z2 = self.W2 @ self.A1 + self.b2
                self.A2 = self.relu(x=self.Z2)
                
                self.Z3 = self.W3 @ self.A2 + self.b3
                self.A3 = self.softmax(x=self.Z3) # These are the probability distributions

                # Backpropagation
                self.y_batch = self.y_batch.T
                self.loss = self.cross_entropy(predictions=self.A3, targets=self.y_batch)

                self.m = self.A3.shape[1] # Batch size

                # Calculate gradients
                self.dZ3 = self.A3 - self.y_batch
                self.dW3 = (1 / self.m) * self.dZ3 @ self.A2.T
                self.db3 = (1 / self.m) * np.sum(self.dZ3, axis=1, keepdims=True)

                self.dA2 = self.W3.T @ self.dZ3
                self.dZ2 = self.dA2 * (self.Z2 > 0) 
                self.dW2 = (1 / self.m) * self.dZ2 @ self.A1.T  
                self.db2 = (1 / self.m) * np.sum(self.dZ2, axis=1, keepdims=True) 

                self.dA1 = self.W2.T @ self.dZ2
                self.dZ1 = self.dA1 * (self.Z1 > 0)
                self.dW1 = (1 / self.m) * self.dZ1 @ self.A0.T  # where A0 = X.T
                self.db1 = (1 / self.m) * np.sum(self.dZ1, axis=1, keepdims=True)

                # Gradient descent step (update weights and biases)
                self.W3 -= alpha * self.dW3
                self.b3 -= alpha * self.db3

                self.W2 -= alpha * self.dW2
                self.b2 -= alpha * self.db2

                self.W1 -= alpha * self.dW1
                self.b1 -= alpha * self.db1

                # Model checkpointing
                if self.loss < self.best_loss:
                    self.best_loss = self.loss
                    self.best_model = {
                        "Model no.": epoch + 1,
                        "W1": self.W1.copy(),
                        "W2": self.W2.copy(),
                        "W3": self.W3.copy(),
                        "b1": self.b1.copy(),
                        "b2": self.b2.copy(),
                        "b3": self.b3.copy()
                    }

                                
            # Progress
            print(f"Epoch:{epoch+1}\nLoss:{self.loss}\n----------------------------")

    def predict(self, input):
        self.Z1 = self.W1 @ input.T + self.b1
        self.A1 = self.relu(x=self.Z1)          

        self.Z2 = self.W2 @ self.A1 + self.b2
        self.A2 = self.relu(x=self.Z2)
                
        self.Z3 = self.W3 @ self.A2 + self.b3
        self.A3 = self.softmax(x=self.Z3) 

        return np.argmax(self.A3, axis=0)

    def evaluate(self):
        """
        Returns the score of the model using the testing data
        """

        predictions = self.predict(self.X_test)
        true_labels = np.argmax(self.y_test, axis=1)
        accuracy = np.mean(predictions == true_labels)

        
        A0 = self.X_test.T
        Z1 = self.W1 @ A0 + self.b1
        A1 = self.relu(Z1)
        Z2 = self.W2 @ A1 + self.b2
        A2 = self.relu(Z2)
        Z3 = self.W3 @ A2 + self.b3
        A3 = self.softmax(Z3)
        loss = self.cross_entropy(A3, self.y_test.T)

        print(f"Loss: {loss:.4f}, Accuracy: {accuracy * 100:.2f}%")
        return loss, accuracy
    
    def get_best_model(self):
        if self.best_model is None:
            raise ValueError("No model has been trained yet.")
        
        model = self.best_model
        self.W1 = model["W1"]
        self.W2 = model["W2"]
        self.W3 = model["W3"]
        self.b1 = model["b1"]
        self.b2 = model["b2"]
        self.b3 = model["b3"]

        return self

# ITS OVER
model = NeuralNetwork()
model.fit(epochs=100)
print(f"Accuracy of trained model: {model.evaluate()}\n")
model = model.get_best_model()
print(f"Accuracy of best model (I think) from training: {model.evaluate()}")