from application import app,db

app.app_context().push()
db.create_all()

class FriendsCharacter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    catch_phrase = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"My name is {self.name} and my catch phrase is {self.catch_phrase}"
    
    def __init__(self, name, age, catch_phrase):
        self.name = name
        self.age = age
        self.catch_phrase = catch_phrase

with app.app_context():
    db.create_all()
    print("Database tables created")