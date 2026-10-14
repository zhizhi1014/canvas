import torch
import torch.nn as nn


class TGM(nn.Module):
    def __init__(self, channels):
        super().__init__()
        self.desc = ...
        self.graph = ...
        self.gcn = ...
        self.head = ...

    def forward(self, F_delta):
        D = self.desc(F_delta)
        A = self.graph(D)
        F_ter = self.gcn(F_delta, A)
        F_ter = self.head(F_ter)
        F_chg = F_delta - F_ter
        return F_ter, F_chg
