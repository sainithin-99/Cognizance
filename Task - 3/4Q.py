import pandas as pd

ser = pd.Series(['amrita', 'school', 'of', 'engineering' 'chennai' , 'campus'])

print("Series:")
print(ser)

newSeries = ser.map(lambda x: x[0].upper() + x[1:-1] + x[-1])

# Print the resulting series
print("\nResulting Series :")
print(newSeries)
