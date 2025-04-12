from app.extensions import db

class RFI(db.Model):
    __tablename__ = 'rfis'
    
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    submitted_date = db.Column(db.DateTime, nullable=False)
    response_date = db.Column(db.DateTime)
    status = db.Column(db.String(50), default='Open')
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    project = db.relationship('Project', back_populates='rfis')
    created_user = db.relationship('User', back_populates='rfis')

class Submittal(db.Model):
    __tablename__ = 'submittals'
    
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    submission_date = db.Column(db.DateTime, nullable=False)
    approval_date = db.Column(db.DateTime)
    status = db.Column(db.String(50), default='Pending')
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    project = db.relationship('Project', back_populates='submittals')
    created_user = db.relationship('User', back_populates='submittals')

class Drawing(db.Model):
    __tablename__ = 'drawings'
    
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    file_path = db.Column(db.String(255), nullable=False)
    upload_date = db.Column(db.DateTime, nullable=False)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    project = db.relationship('Project', back_populates='drawings')
    created_user = db.relationship('User', back_populates='drawings')

class Specification(db.Model):
    __tablename__ = 'specifications'
    
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    file_path = db.Column(db.String(255), nullable=False)
    upload_date = db.Column(db.DateTime, nullable=False)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    project = db.relationship('Project', back_populates='specifications')
    created_user = db.relationship('User', back_populates='specifications')

class FileExplorer(db.Model):
    __tablename__ = 'file_explorer'
    
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
    file_name = db.Column(db.String(255), nullable=False)
    file_path = db.Column(db.String(255), nullable=False)
    upload_date = db.Column(db.DateTime, nullable=False)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    project = db.relationship('Project', back_populates='files')
    created_user = db.relationship('User', back_populates='files')

class Permit(db.Model):
    __tablename__ = 'permits'
    
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    issue_date = db.Column(db.DateTime, nullable=False)
    expiration_date = db.Column(db.DateTime)
    status = db.Column(db.String(50), default='Active')
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    project = db.relationship('Project', back_populates='permits')
    created_user = db.relationship('User', back_populates='permits')

class Meeting(db.Model):
    __tablename__ = 'meetings'
    
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    meeting_date = db.Column(db.DateTime, nullable=False)
    agenda = db.Column(db.Text)
    minutes = db.Column(db.Text)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    project = db.relationship('Project', back_populates='meetings')
    created_user = db.relationship('User', back_populates='meetings')

class Transmittal(db.Model):
    __tablename__ = 'transmittals'
    
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    transmittal_date = db.Column(db.DateTime, nullable=False)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    project = db.relationship('Project', back_populates='transmittals')
    created_user = db.relationship('User', back_populates='transmittals')