import os
import datetime
import random
from werkzeug.utils import secure_filename


import cloudinary
import cloudinary.uploader
import cloudinary.api

# Cloudinary configuration
cloudinary.config(
    cloud_name='dthb3hxxb',
    api_key='133472944653861',
    api_secret='mNDMZdDbMrEJO7I_2kv5tDFTeZw',
    secure=True
)

 # ID
 # Feature          ID
 # Users            1
 # Sliders          2
 # Questions        3
 # Colors           4
 # Sizes            5
 # Materials        6
 # Products         7      

valid_features = ["users", "sliders", "questions", "colors", "sizes", "materials", "products", "services", "settings", "phones", "emails", "locations", "inquiries"] 
valid_actions = ["view", "add", "edit", "delete"]

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'svg'}



def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



def delete_image(image_url):
    try:
        # Extract the public ID from the URL
        url_parts = image_url.split('/')
        #file_name = image_url.rsplit('/', 1)[-1].split('.')[0]
        folder_name = url_parts[-2]
        file_name_with_ext = url_parts[-1]
        
        # Remove the file extension from the file name
        file_name = file_name_with_ext.split('.')[0]

        print(f"Deleting image with folder name: {folder_name}")
        public_id = f"{folder_name}/{file_name}"
        print(f"Deleting image with public ID: {public_id}")
        delete_result = cloudinary.uploader.destroy(public_id)
        print(delete_result)

        return None  # Success
    except Exception as e:
        return f"Error deleting image: {str(e)}"


def process_image(file, folder_name, old_image_url=None):
    try:
        # Check if the file has a valid extension
        if not file or not allowed_file(file.filename):
            return None, "Invalid file type. Allowed types are: png, jpg, jpeg."

        # Upload the file to Cloudinary
        upload_result = cloudinary.uploader.upload(file, folder=folder_name)

        # Delete the old image if provided
        if old_image_url:
            error = delete_image(old_image_url)
            if error:
                return None, error


        # Return the secure URL of the uploaded image
        return upload_result.get("secure_url"), None

    except Exception as e:
        # Return an error message if an exception occurs
        return None, f"Error uploading file: {str(e)}"












'''def delete_image(image_path):
    try:
        if os.path.exists(image_path):
            os.remove(image_path)
    except Exception as e:
        return f"Error deleting image: {str(e)}"

    
def process_image(file, UPLOAD_FOLDER, old_image_path=None):
    try:
        if not os.path.exists(UPLOAD_FOLDER):
            os.makedirs(UPLOAD_FOLDER)

        # Check if file has a valid extension
        if not file or not allowed_file(file.filename):
            return None, "Invalid file type. Allowed types are: png, jpg, jpeg."
        
        # Generate a secure and unique filename
        original_filename = secure_filename(file.filename)
        name, ext = original_filename.rsplit('.', 1)
        
        # Append timestamp to the filename to make it unique
        timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        filename = f"{name}_{timestamp}.{ext}"
        print(filename)
        
        # Ensure the filename is unique by appending a random number if the filename already exists
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        while os.path.exists(file_path):
            filename = f"{name}_{timestamp}_{random.randint(1000, 9999)}.{ext}"
            file_path = os.path.join(UPLOAD_FOLDER, filename)
        # Save the file
        file.save(file_path)

        if old_image_path:
            error = delete_image(old_image_path)
            if error:
                return None, error
        

        return file_path, None  # Successfully saved

    except Exception as e:
        # Return an error message if an exception occurs
        return None, f"Error saving file: {str(e)}"
'''



