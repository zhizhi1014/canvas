import torch
import torch.nn as nn


class CMRA(nn.Module):
    def __init__(self, channels):
        super().__init__()
        self.channels = channels

    def forward(self, F_o, F_t):
        F_t = ...
        return F_t
