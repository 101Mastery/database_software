from flask_server import db
from datetime import datetime
from uuid import uuid4


class Formula(db.Model):
    __tablename__ = 'formula'
    __table_args__ = {'extend_existing': True}

    name = db.Column(db.String(80), nullable=False)

    id = db.Column(db.Integer, primary_key=True)

    key = db.Column(db.String(80), default=uuid4())

    description = db.Column(db.String(250))

    user_key = db.Column(db.String(80))

    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    prep = db.Column(db.String(1000))

    time_rq_days = db.Column(db.Float)

    time_rq_hr = db.Column(db.Float)

    time_rq_min = db.Column(db.Float)

    beyond_use = db.Column(db.Float)

    storage = db.Column(db.String(80))

    explosive = db.Column(db.Boolean, default=False)

    flammable = db.Column(db.Boolean, default=False)

    oxidizer = db.Column(db.Boolean, default=False)

    corrosive = db.Column(db.Boolean, default=False)

    toxic = db.Column(db.Boolean, default=False)

    approved = db.Column(db.Boolean, default=False)

    formula_yield = db.Column(db.Float)

    f_yield_unit = db.Column(db.String(10))

    dose_size = db.Column(db.Float)

    d_size_unit = db.Column(db.String(10))

    dose_form = db.Column(db.String(50))

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

    id = db.Column(db.Integer, primary_key=True)

    ingredient_name = db.Column(db.String(80))

    formula_key = db.Column(db.String(80))

    ingredient_key = db.Column(db.String(80))

    step_key = db.Column(db.String(80))

    amount = db.Column(db.Float)

    unit = db.Column(db.String(10))


class Instruction(db.Model):
    __tablename__ = 'instruction'
    __table_args__ = {'extend_existing': True}

    formula_key = db.Column(db.String(80))

    step_number = db.Column(db.Integer)

    step = db.Column(db.String(1000) )

    key = db.Column(db.String(80), default=uuid4())

    id = db.Column(db.Integer, primary_key=True)


class Attachment(db.Model):
    __tablename__ = 'attachment'
    __table_args__ = {'extend_existing': True}

    name = db.Column(db.String(80))

    id = db.Column(db.Integer, primary_key=True)

    product_key = db.Column(db.String(80))

    product_model = db.Column(db.Integer)

    file_location = db.Column(db.String(80))

    key = db.Column(db.String(80), default=uuid4())


