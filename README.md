# Maids
 Devices Price Classification System (AI System)
 
Database Setup:

models.py defines the Device model with fields.
db is initialized with SQLAlchemy and linked to the Flask app.

Prediction Model:

predict.py trains a simple linear regression model using dummy data.
predict_price function takes a device ID, fetches the device from the database, makes a prediction, updates the device's prediction field, and commits the changes.

Endpoints:

POST /api/devices/: Returns a list of all devices.
GET /api/devices/{id}: Returns details of a specific device by ID.
POST /api/devices: Adds a new device.
POST /api/predict/{deviceId}: Predicts the price for the device with the given ID and saves the result.

Serialization:

We added a serialized property to the Device model to convert it to JSON format.
