from flask_serialize import FlaskSerialize
from web_count import adb

fs_mixin = FlaskSerialize(db)

class WebsiteSerializer(db.Model, fs_mixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    content = db.Column(db.String(120), unique=True, nullable=False)

