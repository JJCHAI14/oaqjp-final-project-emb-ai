""" This module send the text from HTML webpage
    to the Watson NLP server to do the emotion
    detection
"""

import json
import requests

def emotion_detector(text_to_analyze):
    ''' This function take the input text as "text_to_analyze"
        and sent it to the Watson NLP server using request.post()
        the response from the server is then returned
    '''

    # initialize an instance of requests
    url = (
        "https://sn-watson-emotion.labs.skills.network/v1/"
        "watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )

    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    input = { "raw_document": { "text": text_to_analyze } }

    # send the requests to the Watson NLP Library and get the response
    response = requests.post(url, json = input, headers = header, timeout = 10)

    # process the response by getting the 'text' attribute
    formatted_response = json.loads(response.text)

    # return the result in dictionary form 
    return formatted_response

