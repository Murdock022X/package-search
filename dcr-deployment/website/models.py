from flask_login import UserMixin

from website import db, login_manager

@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))

class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(100), unique=True)

    password_hash = db.Column(db.String(100))

    first_name = db.Column(db.String(50))

    last_name = db.Column(db.String(50))

    admin_status = db.Column(db.Boolean, default=False)

    organization_id = db.Column(db.Integer, db.ForeignKey('organizations.id'))

    messages = db.relationship('Messages', backref='users')

class Messages(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(200))

    message = db.Column(db.String(5000))

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

class ClusterRequests(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100))

    es_host = db.Column(db.String(200), unique=True)

    es_port = db.Column(db.String(5))

    es_user = db.Column(db.String(100))

    es_password = db.Column(db.String(100))

    secure = db.Column(db.Boolean)

    organization_id = db.Column(db.Integer, db.ForeignKey('organizations.id'))

class Clusters(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100))

    es_host = db.Column(db.String(200), unique=True)

    es_port = db.Column(db.String(5))

    es_user = db.Column(db.String(100))

    es_password = db.Column(db.String(100))

    secure = db.Column(db.Boolean)

    organization_id = db.Column(db.Integer, db.ForeignKey('organizations.id'))

class Organizations(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), unique=True)

    users = db.relationship('Users', backref='organizations')

    cluster_requests = db.relationship('ClusterRequests', backref='organizations')

    clusters = db.relationship('Clusters', backref='organizations')

    software_types = db.relationship('SoftwareTypes', backref='organizations')

    languages = db.relationship('Languages', backref='organizations')

class SoftwareTypes(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    type = db.Column(db.String(50))

    instances = db.Column(db.Integer)

    org_id = db.Column(db.Integer, db.ForeignKey('organizations.id'))

class Languages(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(150))

    instances = db.Column(db.Integer)

    org_id = db.Column(db.Integer, db.ForeignKey('organizations.id'))
