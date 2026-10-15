import numpy as np

def calculateFinal():
    return scores @ weight_matrix.T

def methodPickerStud():
    methods = ['A', 'B', 'C', 'D']
    for stud in range(final_scores.shape[0]):
        best_idx = np.argmax(final_scores[stud])
        print(f"student {stud}:", methods[best_idx], final_scores[stud, best_idx])

def methodPickerClass():
    methods = ['A', 'B', 'C', 'D']
    stud_means = np.mean(final_scores, axis = 0)
    print(methods[np.argmax(stud_means)])
    print("biggest mean for class is for method number:", np.argmax(np.mean(final_scores, axis = 0)))

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
print(final_scores)
print("="*20)
methodPickerStud()

new_weights = [0.25, 0.25, 0.5]
weight_matrix = np.vstack([weight_matrix, new_weights])
print("="*20)
print(weight_matrix)