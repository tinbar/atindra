import app

db = app.db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(), unique=True)
    password = db.Column(db.String())
    mobile_device_id = db.Column(db.String())
    salt = db.Column(db.String())
    email = db.Column(db.String(), unique=True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    postal_code = db.Column(db.String())
    city_of_residence = db.Column(db.String())
    # no address param since the user will have interval readings which themselves have address values
    user_token = db.relationship('UserToken', cascade='all, delete, delete-orphan', backref='user', uselist=False)
    blogs = db.relationship('Blog', cascade='all, delete, delete-orphan', backref='user')
    confirmed = db.Column(db.Boolean, default=False)
    confirmed_on = db.Column(db.DateTime)

    def __repr__(self):
        return '<id {}>'.format(self.id)

class UserToken(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    access_token = db.Column(db.String())
    refresh_token = db.Column(db.String())
    resource_uri = db.Column(db.String())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<id {}>'.format(self.id)

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    body = db.Column(db.String())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<id {}>'.format(self.id)