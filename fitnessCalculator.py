import numpy as np
#age - weight - height - sessionsperweek
gym_data = np.array([[28, 75, 175, 4],
                    [34, 68, 168, 3], 
                    [45, 82, 180, 2], 
                    [22, 58, 162, 5], 
                    [38, 90, 0, 1], 
                    [29, 65, 170, 0]])

member_names = np.array(["Ali", "Sara", "Reza", "Neda", "Hassan", "Maryam"])
#replace 0 with mean
clean_data = np.where(gym_data == 0, np.mean(gym_data, axis = 0), gym_data)
#take last 3 columns
gym_data_selected = clean_data[:,-3:] 
BMI = gym_data_selected[:,0] / (gym_data_selected[:,1]/100) **2 #تبدیل سانتی متر به متر
#ضریب 1
fitness = BMI + gym_data_selected[:,2] #نمره امادگی جسمانی
print(member_names[np.argmax(fitness)], ":", np.max(fitness)) #Hassan

distances = gym_data_selected[:,2] - np.std(gym_data_selected[:,2]) 
print(distances)
print(np.round(np.max(distances),4))