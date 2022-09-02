"""
network architechture for place recognition (Oxford dataset)
"""

import torch
import torch.nn as nn
# import vgtk
import SPConvNets.utils as M
# import vgtk.spconv.functional as L
import SPConvNets.models.pr_so3net_pn as frontend
import config as cfg

class E2PNGeM(nn.Module):
    def __init__(self, opt):
        super(E2PNGeM, self).__init__()
        self.opt = opt
        
        # epn param
        self.mlps=[[32], [64]]
        out_mlps=[self.mlps[-1][0], cfg.LOCAL_FEATURE_DIM]
        self.e2pn = frontend.build_model(self.opt, self.mlps, out_mlps, outblock='linear')
        self.gem = M.GeM()

        print('E2PN', self.e2pn)

    def forward(self, x):
        '''
        INPUT: B, N, D_input=3
        Local Feature: B, N', D_local
        Global Feature: B, D_output
        '''
        B, _, _ = x.shape
        x_frontend = torch.empty(size=(B, cfg.NUM_POINTS, cfg.LOCAL_FEATURE_DIM), device=x.device)
        for i in range(B):
            x_onlyone = x[i, :, :].unsqueeze(0)
            x_frontend[i], _, _ = self.e2pn(x_onlyone)

        x_out = self.gem(x_frontend)

        return x_out, x_frontend #, pcd_downsampled