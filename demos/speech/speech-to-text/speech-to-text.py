import os
import azure.cognitiveservices.speech as speechsdk
from dotenv import load_dotenv

# Get Configuration Settings
load_dotenv()
ai_endpoint = os.getenv("AI_SERVICE_REGION")
ai_key = os.getenv("AI_SERVICE_KEY")


def recognize_from_microphone():
    speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('AI_SERVICE_KEY'), region=os.environ.get('AI_SERVICE_REGION'))
    speech_config.speech_recognition_language="en-US"

    # audio_config = speechsdk.audio.AudioConfig(filename="AudioFile.wav") ## UNCOMMENT TO USE INCLUDED AUDIO FILE INSTEAD OF MICROPHONE INPUT
    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True) ## COMMENT TO USE INCLUDED AUDIO FILE INSTEAD OF MICROPHONE INPUT
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
    

    print("Speak into your microphone.") ## COMMENT TO USE INCLUDED AUDIO FILE INSTEAD OF MICROPHONE INPUT
    speech_recognition_result = speech_recognizer.recognize_once_async().get()

    if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Recognized: {}".format(speech_recognition_result.text))
    elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized: {}".format(speech_recognition_result.no_match_details))
    elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_recognition_result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))
            print("Did you set the speech resource key and region values?")

recognize_from_microphone()