import torch

t = torch.tensor([
    # Channel 0
    [
        [10, 20, 30, 40, 50],
        [10, 20, 30, 40, 50],
        [10, 20, 30, 40, 50],
        [10, 20, 30, 40, 50],
        [10, 20, 30, 40, 50],
    ],

    # Channel 1
    [
        [20, 30, 40, 50, 60],
        [20, 30, 40, 50, 60],
        [20, 30, 40, 50, 60],
        [20, 30, 40, 50, 60],
        [20, 30, 40, 50, 60],
    ],

    # Channel 2
    [
        [30, 40, 50, 60, 70],
        [30, 40, 50, 60, 70],
        [30, 40, 50, 60, 70],
        [30, 40, 50, 60, 70],
        [30, 40, 50, 60, 70],
    ]
], dtype=torch.float32)

print(t.shape)
# print(t[0])
# print(t[0,0])
#

# results = t.mean(1)

# print(results)

# print(results.shape)

# p = torch.tensor(
#     [
#         [1],
#         [3,4],
#         [1,2,3],
#         [1,2,3,4]
#     ]
    # [
    #     [1,2,3],
    #     [4,5,6],
    # ],
    # [
    #     [1],
    #     [2],
    #     [3]
    # ]
# )

# print(p.shape)


s = torch.tensor([
    # Channel 0
    [
        [1., 2.],
        [3., 4.]
    ],

    # Channel 1
    [
        [5., 6.],
        [8., 7.]
    ],

    # Channel 2
    [
        [9., 10.],
        [11., 12.]
    ]
])


r1 = s.mean(-3)
print(r1)
print(r1.shape)



r2 = s.mean(-2)
print(r2)
print(r2.shape)


r3 = s.mean(-1)
print(r3)
print(r3.shape)




