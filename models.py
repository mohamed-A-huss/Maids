from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Device(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    battery_power = db.Column(db.Float)
    blue = db.Column(db.Float)
    clock_speed = db.Column(db.Float)
    dual_sim = db.Column(db.Float)
    fc = db.Column(db.Float)
    four_g = db.Column(db.Float)
    int_memory = db.Column(db.Float)
    m_dep = db.Column(db.Float)
    mobile_wt = db.Column(db.Float)
    n_cores = db.Column(db.Float)
    pc = db.Column(db.Float)
    px_height = db.Column(db.Float)
    px_width = db.Column(db.Float)
    ram = db.Column(db.Float)
    sc_h = db.Column(db.Float)
    sc_w = db.Column(db.Float)
    three_g = db.Column(db.Float)
    touch_screen = db.Column(db.Float)
    predicted_price = db.Column(db.Float)

    def __repr__(self):
        return f'<Device {self.name}>'
