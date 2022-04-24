allowed_extensions = ['mp4']


def validate_file_extension(filename):

    if '.' not in filename:
        return False

    extension = filename.rsplit('.', 1)[1]

    if extension.lower() in allowed_extensions:
        return True
    else:
        return False
