import torch
import torch.nn as nn

data = torch.Tensor([1, 2, 3])

softmax_function = nn.Softmax(dim=0)
output = softmax_function(data)


class MySoftmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        x_exp = torch.exp(x)
        partition = x_exp.sum(0, keepdims=True)
        return x_exp / partition


data = torch.Tensor([1, 2, 3])
my_softmax = MySoftmax()
output = my_softmax(data)

new_data = torch.Tensor([1, 2, 300000000])
output = my_softmax(new_data)


class SoftmaxStable(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        x_max = torch.max(x, dim=0, keepdims=True)
        x_exp = torch.exp(x - x_max.values)
        partition = x_exp.sum(0, keepdims=True)
        return x_exp / partition


data = torch.Tensor([1, 2, 3])
softmax_stable = SoftmaxStable()
output = softmax_stable(data)


new_data = torch.Tensor([1, 2, 300000000])
output = softmax_stable(new_data)
