import torch
import torch.nn as nn

from .cmra import CMRA
from .tgm import TGM
from .savr import SAVR


class Canvas(nn.Module):
    def __init__(self, in_o=3, in_t=1, channels=256, n_class=2):
        super().__init__()
        self.encoder_o = ...
        self.encoder_t = ...
        self.cmra = CMRA(channels)
        self.tgm = TGM(channels)
        self.savr = SAVR(channels)
        self.decoder = ...

    def forward(self, I_o1, I_t1, I_o2, I_t2):
        F_o1, F_t1 = self.encoder_o(I_o1), self.encoder_t(I_t1)
        F_o2, F_t2 = self.encoder_o(I_o2), self.encoder_t(I_t2)

        F_o1, F_t1 = self.cmra(F_o1, F_t1)
        F_o2, F_t2 = self.cmra(F_o2, F_t2)

        d_o = F_o2 - F_o1
        d_t = F_t2 - F_t1
        F_delta = torch.cat([d_o, d_t], dim=1)

        F_ter, F_chg = self.tgm(F_delta)
        M = self.savr(F_chg)
        pred = self.decoder(F_chg, M)
        return {'pred': pred, 'M': M, 'F_ter': F_ter, 'F_chg': F_chg}
