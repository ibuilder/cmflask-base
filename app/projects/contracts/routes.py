from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from . import contracts_bp
from .forms import PrimeContractForm, SubcontractForm, AgreementForm, LienWaiverForm, InsuranceForm, LetterOfIntentForm
from app.models.contracts import PrimeContract, Subcontract, ProfessionalServiceAgreement, LienWaiver, CertificateOfInsurance, LetterOfIntent
from app.models.project import Project
from app.extensions import db

@contracts_bp.route('/contracts')
@login_required
def contracts():
    project_id = request.args.get('project_id', type=int)
    project = Project.query.get_or_404(project_id)
    contracts = PrimeContract.query.filter_by(project_id=project_id).all()
    return render_template('projects/contracts/list.html', project=project, contracts=contracts)

@contracts_bp.route('/contracts/create', methods=['GET', 'POST'])
@login_required
def create_contract():
    project_id = request.args.get('project_id', type=int)
    project = Project.query.get_or_404(project_id)
    form = PrimeContractForm()
    
    if form.validate_on_submit():
        contract = PrimeContract(
            project_id=project_id,
            title=form.title.data,
            description=form.description.data,
            contract_value=form.contract_value.data,
            start_date=form.start_date.data,
            end_date=form.end_date.data,
            created_by=current_user.id
        )
        db.session.add(contract)
        db.session.commit()
        flash('Contract created successfully!', 'success')
        return redirect(url_for('projects.contracts.contracts', project_id=project_id))
    
    return render_template('projects/contracts/create.html', project=project, form=form)

@contracts_bp.route('/contracts/<int:id>')
@login_required
def view_contract(id):
    contract = PrimeContract.query.get_or_404(id)
    project = Project.query.get_or_404(contract.project_id)
    return render_template('projects/contracts/view.html', project=project, contract=contract)

@contracts_bp.route('/subcontracts')
@login_required
def subcontracts():
    project_id = request.args.get('project_id', type=int)
    project = Project.query.get_or_404(project_id)
    subcontracts = Subcontract.query.filter_by(project_id=project_id).all()
    return render_template('projects/contracts/subcontracts/list.html', project=project, subcontracts=subcontracts)

@contracts_bp.route('/subcontracts/create', methods=['GET', 'POST'])
@login_required
def create_subcontract():
    project_id = request.args.get('project_id', type=int)
    project = Project.query.get_or_404(project_id)
    form = SubcontractForm()
    
    if form.validate_on_submit():
        subcontract = Subcontract(
            project_id=project_id,
            title=form.title.data,
            description=form.description.data,
            subcontract_value=form.subcontract_value.data,
            start_date=form.start_date.data,
            end_date=form.end_date.data,
            created_by=current_user.id
        )
        db.session.add(subcontract)
        db.session.commit()
        flash('Subcontract created successfully!', 'success')
        return redirect(url_for('projects.contracts.subcontracts', project_id=project_id))
    
    return render_template('projects/contracts/subcontracts/create.html', project=project, form=form)

@contracts_bp.route('/agreements')
@login_required
def agreements():
    project_id = request.args.get('project_id', type=int)
    project = Project.query.get_or_404(project_id)
    agreements = ProfessionalServiceAgreement.query.filter_by(project_id=project_id).all()
    return render_template('projects/contracts/agreements/list.html', project=project, agreements=agreements)

@contracts_bp.route('/agreements/create', methods=['GET', 'POST'])
@login_required
def create_agreement():
    project_id = request.args.get('project_id', type=int)
    project = Project.query.get_or_404(project_id)
    form = AgreementForm()
    
    if form.validate_on_submit():
        agreement = ProfessionalServiceAgreement(
            project_id=project_id,
            title=form.title.data,
            description=form.description.data,
            agreement_value=form.agreement_value.data,
            start_date=form.start_date.data,
            end_date=form.end_date.data,
            created_by=current_user.id
        )
        db.session.add(agreement)
        db.session.commit()
        flash('Agreement created successfully!', 'success')
        return redirect(url_for('projects.contracts.agreements', project_id=project_id))
    
    return render_template('projects/contracts/agreements/create.html', project=project, form=form)

@contracts_bp.route('/lien_waivers')
@login_required
def lien_waivers():
    project_id = request.args.get('project_id', type=int)
    project = Project.query.get_or_404(project_id)
    waivers = LienWaiver.query.filter_by(project_id=project_id).all()
    return render_template('projects/contracts/lien_waivers/list.html', project=project, waivers=waivers)

@contracts_bp.route('/lien_waivers/create', methods=['GET', 'POST'])
@login_required
def create_lien_waiver():
    project_id = request.args.get('project_id', type=int)
    project = Project.query.get_or_404(project_id)
    form = LienWaiverForm()
    
    if form.validate_on_submit():
        waiver = LienWaiver(
            project_id=project_id,
            title=form.title.data,
            description=form.description.data,
            created_by=current_user.id
        )
        db.session.add(waiver)
        db.session.commit()
        flash('Lien waiver created successfully!', 'success')
        return redirect(url_for('projects.contracts.lien_waivers', project_id=project_id))
    
    return render_template('projects/contracts/lien_waivers/create.html', project=project, form=form)

@contracts_bp.route('/certificates_of_insurance')
@login_required
def certificates_of_insurance():
    project_id = request.args.get('project_id', type=int)
    project = Project.query.get_or_404(project_id)
    certificates = CertificateOfInsurance.query.filter_by(project_id=project_id).all()
    return render_template('projects/contracts/certificates_of_insurance/list.html', project=project, certificates=certificates)

@contracts_bp.route('/certificates_of_insurance/create', methods=['GET', 'POST'])
@login_required
def create_certificate_of_insurance():
    project_id = request.args.get('project_id', type=int)
    project = Project.query.get_or_404(project_id)
    form = InsuranceForm()
    
    if form.validate_on_submit():
        certificate = CertificateOfInsurance(
            project_id=project_id,
            title=form.title.data,
            description=form.description.data,
            created_by=current_user.id
        )
        db.session.add(certificate)
        db.session.commit()
        flash('Certificate of insurance created successfully!', 'success')
        return redirect(url_for('projects.contracts.certificates_of_insurance', project_id=project_id))
    
    return render_template('projects/contracts/certificates_of_insurance/create.html', project=project, form=form)

@contracts_bp.route('/letters_of_intent')
@login_required
def letters_of_intent():
    project_id = request.args.get('project_id', type=int)
    project = Project.query.get_or_404(project_id)
    letters = LetterOfIntent.query.filter_by(project_id=project_id).all()
    return render_template('projects/contracts/letters_of_intent/list.html', project=project, letters=letters)

@contracts_bp.route('/letters_of_intent/create', methods=['GET', 'POST'])
@login_required
def create_letter_of_intent():
    project_id = request.args.get('project_id', type=int)
    project = Project.query.get_or_404(project_id)
    form = LetterOfIntentForm()
    
    if form.validate_on_submit():
        letter = LetterOfIntent(
            project_id=project_id,
            title=form.title.data,
            description=form.description.data,
            created_by=current_user.id
        )
        db.session.add(letter)
        db.session.commit()
        flash('Letter of intent created successfully!', 'success')
        return redirect(url_for('projects.contracts.letters_of_intent', project_id=project_id))
    
    return render_template('projects/contracts/letters_of_intent/create.html', project=project, form=form)