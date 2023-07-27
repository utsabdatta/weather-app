import logging
from flask import redirect, session

# Initialize Logger  here
logger = logging.getLogger(__name__)


def logout():
    logger.debug(f"{session['email']} got LoggedOut")
    session.pop("email", None)
    return redirect("/login")
