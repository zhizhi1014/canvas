import torch
import torch.nn as nn


class CMRA(nn.Module):
    def __init__(self, channels):
        super().__init__()
        self.proj = ...
        self.w = ...
        self.reg = ...

    def forward(self, F_o, F_t):
        F_o, F_t = self.proj(F_o), self.proj(F_t)
        w = self.w(F_o, F_t)
        a, b = self.reg(w, F_o, F_t)
        F_o = a * F_o + b
        return F_o
