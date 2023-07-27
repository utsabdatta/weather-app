import logging
from datetime import datetime
from app.models.users import User
from app.schemas.users import UserSchema
from flask import request, render_template, redirect, session

# Initialize Logger  here
logger = logging.getLogger(__name__)


def login():
    """
    It is used to loggedin into te site
    :return: If successfully loggedIn the it will redirect to dashboard
    """
    if request.method == "POST":

        email = request.form['email']
        password = request.form['password']

        user = User.get_by_email(email)

        if user and user.check_password(password):
            session['email'] = user.email

            user.last_login = datetime.now()
            user.update()

            serializer = UserSchema()
            data = serializer.dump(user)

            logger.debug(f"{user.email} Logged in Successfully")
            logger.debug(f"Data: {data}")

            return redirect("/dashboard")
        else:
            logger.debug("Email or Password is Incorrect!!!")
            return render_template("login.html", message="Email or Password is Incorrect!!!")

    return render_template("login.html")
