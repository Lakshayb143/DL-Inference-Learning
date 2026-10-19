
import torch


weights = torch.tensor([0.2126, 0.7152, 0.0722])


# try predicting the output
#

answer = weights.unsqueeze(-1)
print(answer)
print(answer.shape)


answer = weights.unsqueeze(-1).unsqueeze(-1)
print(answer)
print(answer.shape)

answer = weights.unsqueeze(1).unsqueeze(2)
print(answer)

print(answer.shape)
