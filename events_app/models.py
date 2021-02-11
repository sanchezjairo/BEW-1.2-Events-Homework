"""Create database models to represent tables."""
from events_app import db
from sqlalchemy.orm import backref

# Creates a model called `Guest` with the following fields:
# - id: primary key
# - name: String column
# - email: String column
# - phone: String column
# - events_attending: relationship to "Event" table with a secondary table

class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80))
    phone = db.Column(db.String(80))
    genres = db.relationship( 'Event', secondary='guest_event')

    def __str__(self):
        return f'<Name:{self.name}'

    def __repr__(self):
        return f'<Name:{self.name}'

# Creates a model called `Event` with the following fields:
# - id: primary key
# - title: String column
# - description: String column
# - date_and_time: DateTime column
# - guests: relationship to "Guest" table with a secondary table

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(80))
    date_and_time = db.Column(db.Date)
    guests = db.relationship('Guest', secondary = 'guest_event')

    def __str__(self):
        return f'<Event Title: {self.title}>'

    def __repr__(self):
        return f'<Event Title: {self.title}>'
# Creates a table `guest_event_table` with the following columns:
# - event_id: Integer column (foreign key)
# - guest_id: Integer column (foreign key)

guest_event_table = db.Table('guest_event',
    db.Column('guest_id', db.Integer, db.ForeignKey('guest.id')),
    db.Column('event_id', db.Integer, db.ForeignKey('event.id'))

)

guest_event_table = None