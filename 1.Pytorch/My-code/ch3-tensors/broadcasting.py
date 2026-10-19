import torch


points = torch.tensor([1,2,3])
print(points)

print( points + 10)

# doubt

tensor_a = torch.tensor([[1, 2, 3],
                        [4, 5, 6]]) # 2x3 matrix
tensor_b = torch.tensor([[[10, 20, 30]],
                         [[40, 50, 60]]]) # 2x1x3 tensor
result = tensor_a + tensor_b



p = torch.tensor([6,2,3])
w = torch.tensor([
    [10,20,30],
    [40,50,60]
])

print(p*w)
