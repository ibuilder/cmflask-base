from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from . import closeout_bp
from .forms import ManualForm, WarrantyForm, AtticStockForm
from app.models.closeout import Manual, Warranty, AtticStock
from app.models.project import Project
from app.extensions import db

@closeout_bp.route('/manuals')
@login_required
def manuals():
    project_id = request.args.get('project_id', type=int)
    project = Project.query.get_or_404(project_id)
    manuals = Manual.query.filter_by(project_id=project_id).all()
    return render_template('projects/closeout/manuals.html', project=project, manuals=manuals)

@closeout_bp.route('/manuals/create', methods=['GET', 'POST'])
@login_required
def create_manual():
    project_id = request.args.get('project_id', type=int)
    project = Project.query.get_or_404(project_id)
    form = ManualForm()
    if form.validate_on_submit():
        manual = Manual(
            project_id=project_id,
            title=form.title.data,
            description=form.description.data,
            created_by=current_user.id
        )
        db.session.add(manual)
        db.session.commit()
        flash('Manual created successfully!', 'success')
        return redirect(url_for('projects.closeout.manuals', project_id=project_id))
    return render_template('projects/closeout/create_manual.html', project=project, form=form)

@closeout_bp.route('/warranties')
@login_required
def warranties():
    project_id = request.args.get('project_id', type=int)
    project = Project.query.get_or_404(project_id)
    warranties = Warranty.query.filter_by(project_id=project_id).all()
    return render_template('projects/closeout/warranties.html', project=project, warranties=warranties)

@closeout_bp.route('/warranties/create', methods=['GET', 'POST'])
@login_required
def create_warranty():
    project_id = request.args.get('project_id', type=int)
    project = Project.query.get_or_404(project_id)
    form = WarrantyForm()
    if form.validate_on_submit():
        warranty = Warranty(
            project_id=project_id,
            title=form.title.data,
            description=form.description.data,
            expiration_date=form.expiration_date.data,
            created_by=current_user.id
        )
        db.session.add(warranty)
        db.session.commit()
        flash('Warranty created successfully!', 'success')
        return redirect(url_for('projects.closeout.warranties', project_id=project_id))
    return render_template('projects/closeout/create_warranty.html', project=project, form=form)

@closeout_bp.route('/attic_stock')
@login_required
def attic_stock():
    project_id = request.args.get('project_id', type=int)
    project = Project.query.get_or_404(project_id)
    attic_stocks = AtticStock.query.filter_by(project_id=project_id).all()
    return render_template('projects/closeout/attic_stock.html', project=project, attic_stocks=attic_stocks)

@closeout_bp.route('/attic_stock/create', methods=['GET', 'POST'])
@login_required
def create_attic_stock():
    project_id = request.args.get('project_id', type=int)
    project = Project.query.get_or_404(project_id)
    form = AtticStockForm()
    if form.validate_on_submit():
        attic_stock = AtticStock(
            project_id=project_id,
            item_name=form.item_name.data,
            quantity=form.quantity.data,
            created_by=current_user.id
        )
        db.session.add(attic_stock)
        db.session.commit()
        flash('Attic stock item created successfully!', 'success')
        return redirect(url_for('projects.closeout.attic_stock', project_id=project_id))
    return render_template('projects/closeout/create_attic_stock.html', project=project, form=form)