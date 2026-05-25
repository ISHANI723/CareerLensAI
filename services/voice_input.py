import azure.cognitiveservices.speech as speechsdk
SPEECH_KEY="GH80LRopeKmUREexO7NGizufj4vuNSFnneGi8dmWnAB43d0CpNPzJQQJ99CEACYeBjFXJ3w3AAAYACOGcoRK"
REGION="eastus"

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