from flask import request, Response, Blueprint, make_response, jsonify
from image_processing.image_utils import background_removal
import urllib
import numpy as np
import cv2

main = Blueprint('main', __name__)

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

@main.route("/")
@main.route("/home")
def home():
	return "Hey! You should try using /background!"


@main.route("/background", methods=['POST'])
def background():

    image_requested = request.files.get('', '')
    image_data = image_requested.read()
    image = cv2.imdecode(np.fromstring(image_data, np.uint8), cv2.IMREAD_COLOR)

    result_image = background_removal.remove_background(image)

    retval, buffer = cv2.imencode('.png', result_image)
    
    response = make_response(buffer.tobytes())
    response.headers['Content-Type'] = 'image/png'
    return response
