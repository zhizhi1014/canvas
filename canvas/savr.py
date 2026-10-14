import torch
import torch.nn as nn


class SAVR(nn.Module):
    def __init__(self, channels):
        super().__init__()
        self.evidence = ...
        self.refine = ...

    def forward(self, F_chg):
        M0 = self.evidence(F_chg)
        M = self.refine(M0)
        return M
