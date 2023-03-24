"""
This module contains helper functions to be used by the app views.

Functions:
    - save_image(image, directory, id): Saves an uploaded image to the static folder and returns the filename.
    - update_invitations_status(response): Updates the status of invitations in the database after a request has been made.
"""
from PIL import Image
from web.app import app, mail

from flask_mail import Message
from itsdangerous import URLSafeTimedSerializer
import os
from flask import redirect, url_for, flash, g, render_template

def save_image(image, directory, id):
    """
    Saves an uploaded image to the static folder and returns the filename.

    Args:
        image: The image to be saved, either as a PIL Image object or the path to the file.
        director (str): The subdirectory within 'static/images' where the image should be saved.
        id: The identifier to be used for the filename.

    Returns:
        str: The filename of the saved image.

    Raises:
        flash("Invalid filetype"): If the filetype is not supported.
    """
    allowed_filetypes = {'.png', '.jpg', '.jpeg'}
    filename = ""

    if image.filename != "":
        _, filetype = os.path.splitext(image.filename)
        if filetype not in allowed_filetypes:
            flash("Invalid filetype")
            return redirect(url_for('profile'))
        filename = id + filetype
        upload_path = os.path.join(app.root_path, 'static/images/{}'.format(directory), filename)

        img = Image.open(image)
        max_dimension = 200

        width, height = img.size
        if width > height:
            left = (width - height) / 2
            right = (width + height) / 2
            top = 0
            bottom = height
        else:
            top = (height - width) / 2
            bottom = (height + width) / 2
            left = 0
            right = width

        cropped_image = img.crop((left, top, right, bottom))

        resized_image = cropped_image.resize((max_dimension, max_dimension))

        resized_image.save(upload_path)
    return filename


@app.after_request
def update_invitions_status(response):
    """
    Updates the status of invitations in the database after a request has been made.

    Args:
        response: The Flask response object.

    Returns:
        The updated Flask response object.

    Notes:
        This function is intended to be used as an after_request callback in the Flask app.
        It checks if there are any invitation objects stored in the g variable, and if any of them have been
        accepted or declined, it updates their status in the database to 'seen'.
    """
    if not g.get('invites'):
        return response

    if response.status_code == 200:
        for invite in g.invites:
            if invite.status in ['accepted', 'declined']:
                invite.status = 'seen'
                invite.save()
    return response

def verify_reset_token(token):
    s = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    try:
        user_id = s.loads(token, max_age=600)['user_id']
    except:
        return None
    return user_id


def get_reset_token(user):
    s = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    return s.dumps({'user_id': user.id})

def send_reset_email(user):
    token = get_reset_token(user)
    msg = Message('Password Reset Request', sender='noreply@teamzone.com', recipients=[user.email])
    msg.html = render_template('email.html', url=url_for('reset_token', token=token, _external=True), name=user.name)
    mail.send(msg)