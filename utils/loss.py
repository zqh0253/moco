import torch
import torch.nn as nn

class LabelMoCoLoss(nn.Module):
    def __init__(self, T):
        super().__init__()
        self.T = T

    def forward(self, q, k, label, q_k, q_label):
        ''' 
        q:           N * C
        k:           N * C
        label:       N
        q_k:         K * C
        q_label:     K
        '''
        pass

