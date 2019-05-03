## TODO: define the convolutional neural network architecture

import torch
import torch.nn as nn
import torch.nn.functional as F
# can use the below import should you choose to initialize the weights of your Net
import torch.nn.init as I


class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        
        ## TODO: Define all the layers of this CNN, the only requirements are:
        ## 1. This network takes in a square (same width and height), grayscale image as input
        ## 2. It ends with a linear layer that represents the keypoints
        ## it's suggested that you make this last layer output 136 values, 2 for each of the 68 keypoint (x, y) pairs
        
        # As an example, you've been given a convolutional layer, which you may (but don't have to) change:
        # 1 input image channel (grayscale), 32 output channels/feature maps, 5x5 square convolution kernel
        
        # 1St Model 
#         self.conv1 = nn.Conv2d(1, 32, 5)
#         self.conv2 = nn.Conv2d(32, 64, 5)
#         self.pool = nn.MaxPool2d(2, 2)
#         self.fc1 = nn.Linear(64*53*53, 50)
#         self.fc1_drop = nn.Dropout(p=0.4)
#         self.fc2 = nn.Linear(50, 136)
        
        
        # 2nd Model
        self.conv1 = nn.Conv2d(1, 32, 4)
        self.conv2 = nn.Conv2d(32, 64, 3)
        self.conv3 = nn.Conv2d(64, 128, 2)
        self.conv4 = nn.Conv2d(128, 256, 1)
        
        self.pool = nn.MaxPool2d(2, 2)
        
#         self.conv1_drop1 = nn.Dropout(p=0.1)
#         self.conv2_drop2 = nn.Dropout(p=0.2)
#         self.conv3_drop3 = nn.Dropout(p=0.3)
#         self.conv4_drop4 = nn.Dropout(p=0.4)

        self.fc1_drop5 = nn.Dropout(p=0.3)
        self.fc2_drop6 = nn.Dropout(p=0.3)
        
        self.fc1 = nn.Linear(256*13*13, 512)
        self.fc2 = nn.Linear(512, 256)
        self.fc3 = nn.Linear(256, 136)
        
        
        ## Note that among the layers to add, consider including:
        # maxpooling layers, multiple conv layers, fully-connected layers, and other layers (such as dropout or batch normalization) to avoid overfitting
        
    def forward(self, x):
        ## TODO: Define the feedforward behavior of this model
        ## x is the input image and, as an example, here you may choose to include a pool/conv step:

        # 1St Model
#          x = self.pool(F.relu(self.conv1(x)))
#         x = self.pool(F.relu(self.conv2(x)))
#         x = x.view(x.size(0), -1)
#         x = F.relu(self.fc1(x))
#         x = self.fc1_drop(x)
#         x = self.fc2(x)
        
        
    # 2nd Model
        x = self.pool(F.elu(self.conv1(x)))
        x = self.pool(F.elu(self.conv2(x)))
        x = self.pool(F.elu(self.conv3(x)))
        x = self.pool(F.elu(self.conv4(x)))
        x = x.view(x.size(0), -1)
        x = F.elu(self.fc1(x))
        x = self.fc1_drop5(x)
        x = F.relu(self.fc2(x))
        x = self.fc2_drop6(x) 
        x = self.fc3(x)
        
#         x = self.conv1_drop1(self.pool(F.elu(self.conv1(x))))
#         x = self.conv2_drop2(self.pool(F.elu(self.conv2(x))))
#         x = self.conv3_drop3(self.pool(F.elu(self.conv3(x))))
#         x = self.conv4_drop4(self.pool(F.elu(self.conv4(x))))
        
        
        # a modified x, having gone through all the layers of your model, should be returned
        return x
