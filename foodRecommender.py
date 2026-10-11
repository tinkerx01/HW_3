import numpy as np
#time to cook - calories - spicy - ingredients
recipes = np.array([[15, 350, 2, 5],
                    [45, 600, 7, 10],
                    [10, 200, 0, 3],
                    [30, 450, 5, 7],
                    [60, 800, 8, 12] ]) 
recipe_names = ["Salad", "Curry", "Toast", "Pasta", "Stew"]

r_min = np.min(recipes, axis = 0)
r_max = np.max(recipes, axis = 0)
recipes_scaled = (recipes - r_min ) / (r_max - r_min)

# print(recipes_scaled)
# print("="*50)
users = np.array([[10, 250, 1, 4],
                  [50, 700, 8, 11], 
                  [25, 400, 4, 6] ])
users_scaled = (users - r_min) / (r_max - r_min)

# print(users_scaled)
dist = np.linalg.norm(recipes_scaled[:, None, :] - users_scaled[None, :, :], axis = 2)
closest_recipe = np.argmin(dist, axis=0) #search each row, find smallest value
                                         #which will match users taste best
user_indx = np.arange(len(users))          

recommends = np.column_stack((
    user_indx,
    np.array(recipe_names)[closest_recipe],
))

print(recommends)
print("="*50)
#=========================================  
recipe_names_arr = np.array(recipe_names) #np arr so it's easier to work with
sorted_names = recipe_names_arr[np.argsort(dist, axis=0)].T 
print(np.column_stack((user_indx, sorted_names)))