import logging
from app.models.users import User
from flask import render_template, session

# Initialize Logger  here
logger = logging.getLogger(__name__)


def index():
    """
    Default Page of the Site
    :return: If Already LoggedIn the it will render dashboard else it will remain in the index page
    """
    if session.get('email', None):
        try:
            user = User.query.filter_by(email=session['email']).first()
            logger.debug(f"Email: {session['email']}")
            if len(user.email):
                return render_template("dashboard.html", user=user)
            else:
                session.pop('email', None)
                return render_template("index.html")
        except:
            session.pop('email', None)
            return render_template("index.html")
    return render_template("index.html")
