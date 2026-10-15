import numpy as np

def calculateFinal():
    return scores @ weight_matrix.T

def methodPicker():
    print(np.mean(final_scores, axis = 0))
    print("biggest mean is for method number:", np.argmax(np.mean(final_scores, axis = 0)))

#quiz - midterm - final
scores = np.array([ [18, 15, 20],
                    [12, 14, 16],
                    [20, 19, 18],
                    [10, 8, 15] ])

scheme_A = np.array([0.5, 0.3, 0.2]) 
scheme_B = np.array([0.2, 0.3, 0.5]) 
scheme_C = np.array([0.1, 0.2, 0.7])

weight_matrix = np.vstack([scheme_A, scheme_B, scheme_C])

final_scores = calculateFinal()
methodPicker()

new_weights = [0.25, 0.25, 0.5] #added new weight vector
weight_matrix = np.vstack([weight_matrix, new_weights])

final_scores = calculateFinal()
methodPicker()