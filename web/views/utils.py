import os
from flask import redirect, url_for

def save_image(image, directory, id):
    upload_folder = "web/static/images/{}".format(directory)
    allowed_filetypes = {'png', 'jpg', 'jpeg'}
    filename = ""

    if image.filename != "":
        filetype = image.filename.split(".")[1].lower()
        if filetype not in allowed_filetypes:
            flash("Invalid filetype")
            return redirect(url_for('profile'))
        filename = id + '.' + filetype
        upload_path = os.path.join(upload_folder, filename)
        image.save(upload_path)
    return filename