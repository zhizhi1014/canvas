import torch
import torch.nn as nn

from .cmra import CMRA
from .tgm import TGM
from .savr import SAVR


class Canvas(nn.Module):
    def __init__(self, channels):
        super().__init__()
        self.cmra = CMRA(channels)
        self.tgm = TGM(channels)
        self.savr = SAVR(channels)

    def forward(self, I_o, I_t):
        F_t = self.cmra(I_o, I_t)
        F_ter, F_chg = self.tgm(F_t)
        B = self.savr(F_chg)
        return B
