import json
from watson_developer_cloud import VisualRecognitionV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import sys
import ibm_watson

authenticator = IAMAuthenticator(
    '0XCyw-LZ-3V257fcyMFGZjF8vQbe2sZfUNa0fG8bggDL')  # here goes service api key

visual_recognition = VisualRecognitionV3(
    '2018-03-19',
    iam_apikey='0XCyw-LZ-3V257fcyMFGZjF8vQbe2sZfUNa0fG8bggDL'
)


def detect_image(file):
    file = 'C:/Users/Adhikari/Desktop/Hackday-master/upload/'+file
    with open(file, 'rb') as images_file:
        classes = visual_recognition.classify(
            images_file,
            threshold='0.6',
            classifier_ids='DefaultCustomModel_422700449').get_result()
    #print(json.dumps(classes, indent=2))
    return classes
