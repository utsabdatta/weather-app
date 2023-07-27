import logging
from app.models.users import User
from flask import render_template, redirect, session

# Initialize Logger  here
logger = logging.getLogger(__name__)


def dashboard():
    """
    It will show the loggedin user from here we have options to see history of search results and can search for new
    city.
    :return: If Loggedin then Dashboard Page Else Login Page
    """
    try:
        if session['email']:
            user = User.query.filter_by(email=session['email']).first()
            logger.debug(f"Email: {session['email']}")
            return render_template("dashboard.html", user=user)

        return redirect("/login")
    except:
        return render_template("index.html", message="You must loggedIn to Access the Page")
