import torch.nn as nn


class Conv1x1(nn.Module):
    def __init__(
        self,
        in_channels,
        out_channels,
        kernel_size=None,
        stride=1,
        bias=False,
        padding=1,
    ):
        super(Conv1x1, self).__init__()
        self.conv = nn.Conv2d(
            in_channels,
            out_channels,
            kernel_size=1,
            stride=stride,
            bias=bias,
            padding=padding,
        )

    def forward(self, x):
        return self.conv(x)

    def __str__(self):
        return "Conv1x1"

    def __repr__(self):
        return "Conv1x1"
