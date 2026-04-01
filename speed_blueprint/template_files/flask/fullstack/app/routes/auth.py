"""Authentication routes."""
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user
from app.forms.auth import LoginForm, RegistrationForm
from app.models.user import User

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    """Login page."""
    # Redirect if already logged in
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.get_by_username(form.username.data)

        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            flash('Login successful!', 'success')

            # Redirect to next page or dashboard
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.dashboard'))
        else:
            flash('Invalid username or password', 'danger')

    return render_template('auth/login.html', form=form)


@bp.route('/register', methods=['GET', 'POST'])
def register():
    """Registration page."""
    # Redirect if already logged in
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))

    form = RegistrationForm()

    if form.validate_on_submit():
        try:
            # Create new user
            User.create_user(
                username=form.username.data,
                email=form.email.data,
                password=form.password.data,
                full_name=form.full_name.data if form.full_name.data else None
            )

            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('auth.login'))

        except ValueError as e:
            flash(str(e), 'danger')

    return render_template('auth/register.html', form=form)


@bp.route('/logout')
def logout():
    """Logout."""
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('main.index'))
