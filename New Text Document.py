import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv(r"ENTER FILE PATH")
print(data)

plt.scatter(data['date'], data["open"], color='black', marker="^")
plt.scatter(data['date'], data["close"], color='yellow', marker="x")

plt.xlabel('Date')
plt.ylabel('Open & Close value')
plt.title('Bit coin open and close values')

plt.show()