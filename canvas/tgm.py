import torch
import torch.nn as nn


class TGM(nn.Module):
    def __init__(self, channels):
        super().__init__()
        self.channels = channels

    def forward(self, F_delta):
        F_ter = ...
        F_chg = ...
        return F_ter, F_chg
