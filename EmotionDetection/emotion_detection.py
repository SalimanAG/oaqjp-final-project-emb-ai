'''
    fichier emotion_detection.py pour interagir avec watson NLP
'''
import requests
import json

def emotion_detector (text_to_analyze):
    '''
        fonction pour exécuter la détection des émotions
    '''
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    json_body = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = json_body, headers = headers)
    dic_response = json.loads(response.text)
    emotions = dic_response['emotionPredictions'][0]['emotion']
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']
    max_score = 'anger'
    max_val = emotions['anger']
    if disgust_score > max_val :
        max_val = emotions['disgust']
        max_score = 'disgust'
    if fear_score > max_val :
        max_val = emotions['fear']
        max_score = 'fear'
    if joy_score > max_val :
        max_val = emotions['joy']
        max_score = 'joy'
    if sadness_score > max_val :
        max_val = emotions['sadness']
        max_score = 'sadness'
    return {'anger': anger_score, 'disgust': disgust_score, 'fear': fear_score, 'joy': joy_score,
            'sadness': sadness_score, 'dominant_emotion': max_score}