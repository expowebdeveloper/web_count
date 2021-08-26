from web_count import db

class Website(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return '<name %r>' % self.name

    @staticmethod    
    def create(**kwargs):
        obj = Website(**kwargs)
        db.session.add(obj)
        db.session.commit()
        return obj

    @staticmethod
    def update(obj,**kwargs):
        name = kwargs.get('name')
        content = kwargs.get('content')
        if name:
            obj.name=name
        if content:
            obj.content = content
        db.session.commit()

    @property
    def serialize(self):
       """Return object data in easily serializable format"""
       return {
           'id'  : self.id,
           'name': self.name,
           'content'  : self.content
       }

db.create_all()