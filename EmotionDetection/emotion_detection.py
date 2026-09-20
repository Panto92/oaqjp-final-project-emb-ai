import json
import requests


def emotion_detector(text_to_analyze):
    """Analyse the emotions in a text and return scores plus dominant emotion."""
    url = ("https://sn-watson-emotion.labs.skills.network/v1/"
           "watson.runtime.nlp.v1/NlpService/EmotionPredict")
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(url, json=payload, headers=headers, timeout=10)

    response_dict = json.loads(response.text)
    scores = response_dict["emotionPredictions"][0]["emotion"]

    result = {
        "anger": scores["anger"],
        "disgust": scores["disgust"],
        "fear": scores["fear"],
        "joy": scores["joy"],
        "sadness": scores["sadness"],
    }
    result["dominant_emotion"] = max(result, key=result.get)
    return result
