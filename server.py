""" Executing this function initiates the application of emotionn
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

@app.route("/emotionDetector")
def sent_detector():
    ''' This code receives the text from the HTML interface and 
        runs emotion analysis over it using emotion_detector()
        function. The output returned shows the emotion and its 
        confidence score for the provided text.
    '''

    # get the variable from html
    text_to_analyze = request.args.get('textToAnalyze')

    # calling emotion analyzer in the emotion analysis
    response = emotion_detector(text_to_analyze)

    # extracting the result
    anger = response["anger"]
    disgust = response["disgust"]
    fear = response["fear"]
    joy = response["joy"]
    sadness = response["sadness"]
    dominant_emotion = response["dominant_emotion"]

    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    # returning the result
    result = (
        f"For the given statement, the system response is 'anger': {anger},"
        f" 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and "
        f" 'sadness': {sadness}. The dominant emotion is "
        f"<span style=\"font-weight: bold;\">{dominant_emotion}</span>."
    )

    return result

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
