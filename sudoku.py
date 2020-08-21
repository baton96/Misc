import numpy as np


def clear(i, val):
    m[i] = val + 1
    m2[i] = np.zeros(9)
    m2[9 * (i // 9):9 * (i // 9) + 9, val] = 0
    m2[i % 9:i % 9 + 72:9, val] = 0
    for j in range(27 * (i // 27), 27 * (i // 27) + 27, 9):
        for k in range(3 * ((i % 9) // 3), 3 * ((i % 9) // 3) + 3):
            m2[j + k, val] = 0


'''
m = [[[1,2,3],[4,5,6],[7,8,9]],
     [[4,5,6],[7,8,9],[1,2,3]],
     [[7,8,9],[1,2,3],[4,5,6]],

     [[1,2,3],[4,5,6],[7,8,9]],
     [[4,5,6],[7,8,9],[1,2,3]],
     [[7,8,9],[1,2,3],[4,5,6]],

     [[1,2,3],[4,5,6],[7,8,9]],
     [[4,5,6],[7,8,9],[1,2,3]],
     [[7,8,9],[1,2,3],[4,5,6]]]

m = [[[0,0,4],[0,5,0],[0,0,3]],
     [[2,0,0],[0,0,6],[0,1,0]],
     [[0,0,5],[1,0,0],[0,0,6]],

     [[0,8,0],[0,0,0],[0,7,0]],
     [[0,2,3],[0,9,7],[1,6,0]],
     [[0,7,1],[3,8,4],[0,0,2]],

     [[9,0,0],[0,0,0],[2,0,0]],
     [[0,0,7],[4,1,2],[6,0,9]],
     [[8,4,0],[7,0,9],[5,0,1]]]
'''
m = np.array(
    [0, 0, 4, 0, 5, 0, 0, 0, 3,
     2, 0, 0, 0, 0, 6, 0, 1, 0,
     0, 0, 5, 1, 0, 0, 0, 0, 6,

     0, 8, 0, 0, 0, 0, 0, 7, 0,
     0, 2, 3, 0, 9, 7, 1, 6, 0,
     0, 7, 1, 3, 8, 4, 0, 0, 2,

     9, 0, 0, 0, 0, 0, 2, 0, 0,
     0, 0, 7, 4, 1, 2, 6, 0, 9,
     8, 4, 0, 7, 0, 9, 5, 0, 1])

nums = set(range(1, 10))
m2 = np.ones((81, 9))

for i, val in enumerate(m):
    if val != 0:
        clear(i, val - 1)

for i in range(9):
    print(m[i * 9:i * 9 + 9])
while np.count_nonzero(m) != 81:
    for i in range(9):
        for val in range(9):
            if m[i * 9 + val] == 0 and sum(m2[i * 9 + val]) == 1:
                clear(i * 9 + val, np.argmax(m2[i * 9 + val]))

            tmp = m2[i * 9:i * 9 + 9, val]
            if sum(tmp) == 1:
                clear(i * 9 + np.argmax(tmp), val)

            tmp = m2[i:i + 72:9, val]
            if sum(tmp) == 1:
                clear(i + np.argmax(tmp) * 9, val)

            idx = [j + k for j in range(27 * (i // 3), 27 * (i // 3) + 27, 9) for k in
                   range(3 * (i % 3), 3 * (i % 3) + 3)]
            tmp = m2[idx, val]
            if sum(tmp) == 1:
                clear(idx[np.argmax(tmp)], val)

            tmp = m[idx]
            if np.count_nonzero(tmp) == 8:
                clear(idx[np.argmin(tmp)], list(nums - set(tmp))[0] - 1)
print('-' * 19)
for i in range(9):
    print(m[i * 9:i * 9 + 9])
