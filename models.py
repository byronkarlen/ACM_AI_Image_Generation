import torch

class Generator(torch.nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(
            in_channels=100, 
            out_channels=64,
            kernel_size=4,
            stride=2,
            padding=1,
            bias=False
        ) 

    def forward(self, z):
        z = self.conv(z)
        return z
    
class Discriminator(torch.nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.sigmoid = torch.nn.Sigmoid()
        self.conv1 = torch.nn.Conv2d(
            in_channels=3,
            out_channels=1,
            kernel_size=4,
            stride=1,
            padding=0,
            bias=False
        )

    def forward(self, image):
        x = self.sigmoid(self.conv(x))
        return x