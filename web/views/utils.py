from PIL import Image
from web.app import app
import os
from flask import redirect, url_for, flash

def save_image(image, directory, id):
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