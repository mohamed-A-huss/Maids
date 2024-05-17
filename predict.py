from sklearn.linear_model import LinearRegression
import numpy as np
from models import Device
import pickle
# Dummy data for training the model

def predict_price(device_id):
    device = Device.query.get(device_id)
    if device:
        # Using a simple prediction based on device ID for demonstration
        model = pickle.load(open("C:/Users/Babak/Desktop/study/Maids/c/finalized_model.sav", 'rb'))
        prediction = model.predict(np.array([[device.id]]))[0]
        device.prediction = prediction
        db.session.commit()
        return prediction
    return None
