from platform import release
import app
from werkzeug.security import generate_password_hash, check_password_hash

class User(app.db.Model):
    id = app.db.Column(app.db.Integer, primary_key=True)
    name = app.db.Column(app.db.String(128))
    last_name = app.db.Column(app.db.String(128))
    patronym = app.db.Column(app.db.String(128))
    password_hash = app.db.Column(app.db.String(2048))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {} {} with id {}>'.format(self.name, self.last_name, self.id)

class Permissions(app.db.Model):
    id = app.db.Column(app.db.Integer, app.db.ForeignKey('user.id'), primary_key=True)
    entry_allowed = app.db.Column(app.db.Boolean, default=0)
    exit_allowed = app.db.Column(app.db.Boolean, default=0)

    release_after = app.db.Column(app.db.Time, index=True, default='')
    release_before = app.db.Column(app.db.Time, index=True, default='')

    letin_after = app.db.Column(app.db.Time, index=True, default='')
    letin_before = app.db.Column(app.db.Time, index=True, default='')

    def bool2perm(bool):
        if bool: return 'permitted'
        else: return 'denied'
    
    def __repr__(self):
        return 'Entry {}, exit {}'.format(self.bool2perm(self.entry_allowed), self.bool2perm(self.exit_allowed))
