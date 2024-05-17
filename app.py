from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import db, Device
from predict import predict_price

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///devices.db'
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/api/devices/', methods=['POST'])
def get_devices():
    devices = Device.query.all()
    return jsonify([device.serialize for device in devices])

@app.route('/api/devices/<int:id>', methods=['GET'])
def get_device(id):
    device = Device.query.get_or_404(id)
    return jsonify(device.serialize)

@app.route('/api/devices', methods=['POST'])
def add_device():
    data = request.json
    new_device = Device(name=data['ram'])
    db.session.add(new_device)
    db.session.commit()
    return jsonify(new_device.serialize), 201

@app.route('/api/predict/<int:deviceId>', methods=['POST'])
def predict_device_price(deviceId):
    prediction = predict_price(deviceId)
    if prediction is not None:
        return jsonify({"deviceId": deviceId, "predicted_price": prediction}), 200
    return jsonify({"error": "Device not found"}), 404

# Helper method to serialize the Device model
@property
def serialize(self):
    return {
        'id': self.id,
        'battery_power': self.battery_power,
        'blue': self.blue,
        'clock_speed': self.clock_speed,
        'dual_sim': self.dual_sim,
        'fc': self.fc,
        'four_g': self.four_g,
        'int_memory': self.int_memory,
        'm_dep': self.m_dep,
        'mobile_wt': self.mobile_wt,
        'n_cores': self.n_cores,
        'pc': self.pc,
        'px_height': self.px_height,
        'px_width': self.px_width,
        'ram': self.ram,
        'sc_h': self.sc_h,
        'sc_w': self.sc_w,
        'three_g': self.three_g,
        'touch_screen': self.touch_screen,
        'predicted_price': self.predicted_price,
    }

Device.serialize = serialize

if __name__ == '__main__':
    app.run(debug=True)
