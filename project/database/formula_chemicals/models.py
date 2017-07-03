from flask_server import db
from datetime import datetime

class Formula(db.Model):
    __tablename__ = 'formula'
    __table_args__ = {'extend_existing': True}

    name = db.Column(db.String(80), nullable=False)

    id = db.Column(db.Integer, primary_key=True)

    key = db.Column(db.String(80), default=uuid4())

    cas = db.Column(db.String(80))

    description = db.Column(db.String(250))

    user_key = db.Column(db.String(80))

    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    prep = db.Column(db.String(1000))

    time_rq_days = db.Column(db.Integer)

    time_rq_hr = db.Column(db.Integer)

    time_rq_min = db.Column(db.Integer)

    time_rq_sec = db.Column(db.Integer)

    beyond_use = db.Column(db.Integer)

    storage = db.Column(db.String(80))

    explosive = db.Column(db.Boolean, default=False)

    flammable = db.Column(db.Boolean, default=False)

    oxidizer = db.Column(db.Boolean, default=False)

    corrosive = db.Column(db.Boolean, default=False)

    toxic = db.Column(db.Boolean, default=False)

    approved = db.Column(db.Boolean, default=False)

    def get_key(self):
        return self.key


class Chemical(db.Model):
    __tablename__ = 'chemical'
    __table_args__ = {'extend_existing': True}

    name = db.Column(db.String(80), nullable=False)

    id = db.Column(db.Integer, primary_key=True)

    key = db.Column(db.String(80), default=uuid4())

    cas = db.Column(db.String(80))

    user_key = db.Column(db.String(80))

    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    beyond_use = db.Column(db.Integer)

    storage = db.Column(db.String(80))

    explosive = db.Column(db.Boolean, default=False)

    flammable = db.Column(db.Boolean, default=False)

    oxidizer = db.Column(db.Boolean, default=False)

    corrosive = db.Column(db.Boolean, default=False)

    toxic = db.Column(db.Boolean, default=False)

    def get_key(self):
        return self.key


class Ingredient(db.Model):
    __tablename__ = 'ingredient'
    __table_args__ = {'extend_existing': True}

    formula_key = db.Column(db.String(80))

    ingredient_key = db.Column(db.String(80))

    step_key = db.Column(db.String(80))


class Instructions(db.Model):
    __tablename__ = 'ingredient'
    __table_args__ = {'extend_existing': True}

    formula_key = db.Column(db.String(80))

    step_number = db.Column(db.Integer)

    key = db.Column(db.String(80), default=uuid4())


class Attachment(db.Model):
    __tablename__ = 'ingredient'
    __table_args__ = {'extend_existing': True}

    name = db.Column(db.String(80))

    product_key = db.Column(db.String(80))

    product_model = db.Column(db.Integer)

    file_location = db.Column(db.String(80))

    key = db.Column(db.String(80), default=uuid4())


