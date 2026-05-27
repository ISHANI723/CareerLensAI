import azure.cognitiveservices.speech as speechsdk
SPEECH_KEY="xxxxx"
REGION="xxxxx"

def get_voice_text():
    speech_config = speechsdk.SpeechConfig(
    subscription=SPEECH_KEY,
    region=REGION
    )

    recognizer = speechsdk.SpeechRecognizer(
    speech_config=speech_config
    )

    result = recognizer.recognize_once()
    return result.text
