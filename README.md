# Image Download Service

This project implements a simple web service with a REST interface using Python and Django. It is designed to handle the upload, storage, and retrieval of images via URLs. The service offers three main REST operations: upload of image URLs, get a list of available images, and retrieve a specific image.

## Features

- Upload Image URLs:
  - Users can upload a list of image URLs. The service will download and store these images persistently.
- List Available Images:
  - Users can request a list of all images that have been successfully downloaded and stored.
- Retrieve an Image:
  - Users can retrieve a specific image by providing its URL.

### Requirements

- Python 3.x
- Django
- Django REST Framework

### Installation

- Clone the repository.
- Install the required packages using `pip install -r requirements.txt`.
- Run `python manage.py migrate` to set up the database.
- Start the server with `python manage.py runserver`.
