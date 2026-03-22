import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import pickle

# dataset load
data = pd.read_csv('dataset.csv')

# features & target
X = data[['sleep_hours', 'screen_time' , 'work_hours' , 'physical_activity']]
y = data['stress_level']

# model
model = RandomForestRegressor()
model.fit(X, y)

# save model
pickle.dump(model, open('stress_model.pkl', 'wb'))

print("Model trained & saved successfully!")