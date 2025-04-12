from app.extensions import db

class QualifiedBidder(db.Model):
    __tablename__ = 'qualified_bidders'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    contact_info = db.Column(db.String(255), nullable=True)
    qualifications = db.Column(db.Text, nullable=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)

class BidPackage(db.Model):
    __tablename__ = 'bid_packages'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    due_date = db.Column(db.Date, nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)

class BidManual(db.Model):
    __tablename__ = 'bid_manuals'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    document_url = db.Column(db.String(255), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)

class Project(db.Model):
    __tablename__ = 'projects'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    qualified_bidders = db.relationship('QualifiedBidder', backref='project', lazy=True)
    bid_packages = db.relationship('BidPackage', backref='project', lazy=True)
    bid_manuals = db.relationship('BidManual', backref='project', lazy=True)