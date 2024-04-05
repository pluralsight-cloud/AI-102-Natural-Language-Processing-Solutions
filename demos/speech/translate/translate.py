import os
import azure.cognitiveservices.speech as speechsdk
from dotenv import load_dotenv

# Get Configuration Settings
load_dotenv()
ai_endpoint = os.getenv("AI_SERVICE_REGION")
ai_key = os.getenv("AI_SERVICE_KEY")

def recognize_from_microphone():
    # This example requires environment variables named "AI_SERVICE_KEY" and "AI_SERVICE_REGION"
    speech_translation_config = speechsdk.translation.SpeechTranslationConfig(subscription=os.environ.get('AI_SERVICE_KEY'), region=os.environ.get('AI_SERVICE_REGION'))
    speech_translation_config.speech_recognition_language="en-US"

    target_language="it"
    speech_translation_config.add_target_language(target_language)

    # audio_config = speechsdk.audio.AudioConfig(filename="AudioFile.wav") ## UNCOMMENT TO USE INCLUDED AUDIO FILE INSTEAD OF MICROPHONE INPUT
    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True) ## COMMENT TO USE INCLUDED AUDIO FILE INSTEAD OF MICROPHONE INPUT
    translation_recognizer = speechsdk.translation.TranslationRecognizer(translation_config=speech_translation_config, audio_config=audio_config)

    print("Speak into your microphone.") ## COMMENT TO USE INCLUDED AUDIO FILE INSTEAD OF MICROPHONE INPUT
    translation_recognition_result = translation_recognizer.recognize_once_async().get()

    if translation_recognition_result.reason == speechsdk.ResultReason.TranslatedSpeech:
        print("Recognized: {}".format(translation_recognition_result.text))
        print("""Translated into '{}': {}""".format(
            target_language, 
            translation_recognition_result.translations[target_language]))
    elif translation_recognition_result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized: {}".format(translation_recognition_result.no_match_details))
    elif translation_recognition_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = translation_recognition_result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))
            print("Did you set the speech resource key and region values?")

recognize_from_microphone()