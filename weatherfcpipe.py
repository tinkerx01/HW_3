import numpy as np

def analyze_day(day):
    if day.shape == (4,8):
        return True

weather_data = np.random.randn(2, 8, 4) * 5 + 20
day2 = weather_data[1].T
analyze_day(day2)
weather_data = weather_data.reshape(-1)
#OR weather_data = weather_data.flatten()
print(weather_data.shape)

day3 = np.random.randn(8, 4)
weather_data = weather_data.reshape(-1,8,4)
weather_data = np.vstack([weather_data, [day3]])
print(weather_data.shape)

m = np.array([[1, 2],
             [3, 4]])

# trpose = m.T

# flat = m.flatten()

# print(trpose,"\n", flat)

#trpose != flat
#one makes a 1,n matrix while the other replaces columns with rows