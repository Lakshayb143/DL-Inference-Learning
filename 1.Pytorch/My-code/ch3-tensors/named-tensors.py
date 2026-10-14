import torch


img_t = torch.randn(3,5,5) # [channels, rows, columns]
weights = torch.tensor([0.2126, 0.7152, 0.0722])


batch_t = torch.randn(2,3,5,5)

# we can generalize dimesnion of RGB chaneels by counting from end : 
# as they aree always at [-3].


img_gray_naive = img_t.mean(-3)
batch_gray_naive = batch_t.mean(-3)

print(img_gray_naive.shape)
print(batch_gray_naive.shape)
