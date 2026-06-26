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

# Example: 

'''import torch
import torch.nn as nn

# Create model
model = nn.Linear(1, 1)

# Loss function
loss_fn = nn.MSELoss()

# Optimizer
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

# Data
x = torch.tensor([[1.0], [2.0], [3.0]])
y = torch.tensor([[2.0], [4.0], [6.0]])

# Training loop
for epoch in range(100):

    prediction = model(x)

    loss = loss_fn(prediction, y)

    optimizer.zero_grad()

    loss.backward()

    optimizer.step()

print(model.weight)
print(model.bias)'''

# Example: 

'''import torch

# Enabling autograd using flag requires_grad=True
x = torch.tensor(2.0, requires_grad=True)

# 2x +3 
y = 2*x + 3

print(y)
# Output
# tensor(7., grad_fn=<AddBackward0>)

# It started backward propagation and goes until leaf node, nothing but starting point of computational graph
y.backward()

# print x.grad to see the gradient
# Please note, unless you execute y.backward(), backward propagation won't start
print(x.grad)
# Output : tensor(2.) because derivative of (2x + 3) is 2'''

# Example 2 : We need to apply chain rule here as it is a function, g(x) i.e. d/dx(2x+3)²

'''import torch

x1 = torch.tensor(3.0, requires_grad=True)
y = (2*x1 + 3)**2
print(y) # tensor(81., grad_fn=<PowBackward0>)
y.backward() # backward propagation initiated
print(x1.grad) # Printing gradinet of x :  tensor(36.)
x1.grad.zero_ 
# if we don't set x1.grad.zero_ then 
# result will be accumulated each time you run this program'''


'''import torch.nn as nn

model = nn.Linear(5, 1)
loss = nn.MSELoss()
print(model)
print(loss)'''


