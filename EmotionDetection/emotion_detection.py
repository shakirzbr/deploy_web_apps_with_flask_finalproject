import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    formatted_response = json.loads(response.text)

    if response.status_code = 200:
        return formatted_response
    elif response.status_code ==  400:
        formatted_response = {
                                'anger': anger_score,
                                'disgust': disgust_score,
                                'fear': fear_score,
                                'joy': joy_score,
                                'sadness': sadness_score,
                                'dominant_emotion': 'joy'}
        return formatted_response