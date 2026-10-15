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
#session numbers cannot be float! so we use round.
clean_data = np.where(gym_data == 0, np.round(np.mean(gym_data, axis = 0)), gym_data)
#take last 3 columns
gym_data_selected = clean_data[:,-3:] 
BMI = gym_data_selected[:,0] / (gym_data_selected[:,1]/100) **2
#ضریب 1
fitness = BMI + gym_data_selected[:,2] #نمره امادگی جسمانی
new_arr = np.column_stack((gym_data_selected, fitness))
print(new_arr)
print(member_names[np.argmax(fitness)], ":", np.max(fitness)) #Hassan

sessions = gym_data_selected[:,2] #temp var for simplicity
z_score = sessions - np.mean(sessions) / np.std(sessions) #for knowing which diff is bigger
dist = np.abs(z_score)
print(member_names[np.argmax(dist)], f"with {gym_data_selected[np.argmax(dist), 2]} sessions", np.round(np.max(dist),4)) #Neda with 5 sessions