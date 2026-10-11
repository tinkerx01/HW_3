import numpy as np
#length - exc-count -caps 
X_messages = np.array([ [12, 0, 1],
                        [45, 5, 8], 
                        [8, 0, 0], 
                        [30, 3, 4] ]) 
w = np.array([0.1, 0.8, 0.5]) 
b = -2.0

raw = X_messages @ w + b
final_report = np.maximum(0, raw) #ReLU activation
moods = np.where(final_report < 5, "energetic", "calm") #threshold = 5
print(np.vstack([final_report, moods]).T)
#second and 3rd messages are energetic
