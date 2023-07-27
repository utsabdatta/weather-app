import logging
from datetime import datetime
from app.models.users import User
from app.schemas.users import UserSchema
from flask import request, render_template

# Initialize Logger  here
logger = logging.getLogger(__name__)


def register():
    """
    If user email is not existing it will create a new user details
    :return: If created successfully it will render login Page
    """
    if request.method == 'POST':

        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        password = request.form['password']

        created_at = datetime.now()

        logger.debug(f"fname: {fname} lname: {lname} email: {email} password: {password}")

        try:

            user = User.get_by_email(email)
        except:
            user = None

        if not user:

            new_user = User(fname=fname, lname=lname, email=email, password=password, created_at= created_at)
            new_user.save()

            serializer = UserSchema()

            data = serializer.dump(new_user)
            logger.debug(f"User Schema: {data}")
            return render_template('login.html', message="Registered Successfully")
        else:
            logger.debug(f"{email} Already Exist")
            return render_template("login.html", message="Same Email Already Exist. Want to Login?")
    return render_template("register.html")