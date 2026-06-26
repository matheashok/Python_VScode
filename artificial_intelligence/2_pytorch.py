# Main Features of PyTorch
'''1. Tensor Operations

The fundamental data structure in PyTorch is a Tensor.

A tensor is similar to a NumPy array but has additional capabilities:

Can run on CPUs or GPUs
Supports automatic differentiation
Efficient for large computations'''

# Example:
'''import torch

x = torch.tensor([1, 2, 3])
print(x)'''


# 2. GPU Support
# PyTorch can perform computations on a GPU, making deep learning training much faster.

# CPU:
'''import torch
x = torch.tensor([1,2,3])
print(x)'''

# GPU:
'''import torch
device = torch.device("cuda")
x = torch.tensor([1,2,3], device=device)
print(x)'''

# A GPU can often train deep learning models much faster than a CPU, especially for large datasets.

# 3. Automatic Differentiation (Autograd)
#This is one of PyTorch's most powerful features.
# Instead of manually calculating derivatives, PyTorch computes them automatically.

# Example:

'''import torch
x = torch.tensor(2.0, requires_grad=True)
y = x**2
y.backward()
print(x.grad)'''


# 4. Neural Network Module (torch.nn)
# Instead of writing every equation yourself, PyTorch provides ready-made neural network layers.

# Example:

'''import torch.nn as nn
model = nn.Linear(3, 1)
print(model)'''

# This creates a layer with:
# 3 input features
# 1 output

# PyTorch automatically creates the weights and bias.

# 5. Loss Functions
# PyTorch includes many common loss functions.

# Examples:
# nn.MSELoss()          # Mean Squared Error
# nn.CrossEntropyLoss() # Classification
# nn.L1Loss()

#Example:

'''import torch.nn as nn
import torch
loss_fn = nn.MSELoss()

prediction = torch.tensor([4.5])
target = torch.tensor([5.0])

loss = loss_fn(prediction, target)
print(loss_fn)
print(loss)'''


# 6. Optimizers
# Optimizers update the model's weights during training.

# Common optimizers:
# torch.optim.SGD()
# torch.optim.Adam()
# torch.optim.RMSprop()

# Example:

 
'''import torch
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
print(optimizer)'''

'''import torch
import torch.nn as nn

class NeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(1, 1)

    def forward(self, x):
        return self.linear(x)

model = NeuralNetwork()          # <-- This line is required

optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
print(optimizer)'''

# 7. Data Loading
# PyTorch provides tools for handling datasets efficiently.


# from torch.utils.data import Dataset
# from torch.utils.data import DataLoader

# A DataLoader automatically:

# Loads data
# Creates mini-batches
# Shuffles data
# Speeds up training