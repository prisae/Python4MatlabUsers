import numpy as np
import matplotlib.pyplot as plt

#%%%

x = np.linspace(0, 100, 301)
y = np.sin(x)

plt.figure()

plt.plot(x, y)

#%%%
fig, ax = plt.subplots(1, 1)

ax.plot(x, y, 'r--')


#%%%

% MY OLD MATLAB CODE
m = 2.0;

for i=1:5
m = m^i
end

#%%%

# MY NEW PYTHON IMPLEMENTATION

m = 2.0

for i in range(1, 6):
    m **= i
    print(m)
    

