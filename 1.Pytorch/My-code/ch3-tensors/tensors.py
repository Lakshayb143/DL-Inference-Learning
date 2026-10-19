import torch


a = torch.ones(5)
# print(a)

print("type of tensor = ", type(a[0]))

points = torch.tensor([[4.0, 1.0] , [5.0, 3.0], [2.0, 1.0]])
# print(points)


print(points[1:])

print(points[0:, 1])
print(points.shape)
print("\n")
print(points)

print("\n")
print(points[None]) # doubt need to learn about it. e

print("\n")
print(points.shape)


print("\n\n\n")


p = torch.rand(2,2)
print(p)


print(p.unsqueeze(0).shape)
print(p.unsqueeze(1).shape)
print(p.unsqueeze(2).shape)
# print(p.unsqueeze(3).shape)
# above line will not work because ? figure out.
