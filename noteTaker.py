import numpy as np

importance = np.array([3, 8, 1, 9, 4, 7])
method1 = importance.reshape(6,1)
method2 = np.transpose([importance])
print(method1.shape, method2.shape)

model_out = np.array([[[0.9]]])
print("raw print:", model_out)
print("item print:", model_out.item())
print("index print:", model_out[0, 0, 0])

# notes = np.array([5, 10, 15, 20, 25]) 
# pinned = notes[1:3] 
# pinned[0] = 999 
# print(notes) -> [5, 999, 20, 25] my guess

notes = np.array([5, 10, 15, 20, 25]) 
pinned = notes[1:3] 
pinned[0] = 999 
print(notes)

