import os
import azure.cognitiveservices.speech as speechsdk
from dotenv import load_dotenv

# Get Configuration Settings
load_dotenv()
ai_endpoint = os.getenv("AI_SERVICE_REGION")
ai_key = os.getenv("AI_SERVICE_KEY")

def recognize_and_synthesize_from_microphone():
    speech_translation_config = speechsdk.translation.SpeechTranslationConfig(
        subscription=ai_key, 
        region=ai_endpoint
    )
    speech_translation_config.speech_recognition_language = "en-US"

    target_language = "it"
    speech_translation_config.add_target_language(target_language)

    # Set a voice name for speech synthesis in the target language
    speech_translation_config.voice_name = "it-IT-ElsaNeural"  

    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    translation_recognizer = speechsdk.translation.TranslationRecognizer(
        translation_config=speech_translation_config, 
        audio_config=audio_config
    )

    def synthesis_callback(evt):
        size = len(evt.result.audio)
        print(f'Audio synthesized: {size} byte(s) {"(COMPLETED)" if size == 0 else ""}')

        if size > 0:
            with open('translation.wav', 'wb') as file:
                file.write(evt.result.audio)
                print("Translation audio saved to 'translation.wav'")

    # Connect the synthesis callback
    translation_recognizer.synthesizing.connect(synthesis_callback)

    print("Speak into your microphone.")
    translation_recognition_result = translation_recognizer.recognize_once_async().get()

    if translation_recognition_result.reason == speechsdk.ResultReason.TranslatedSpeech:
        print("Recognized: {}".format(translation_recognition_result.text))
        print("""Translated into '{}': {}""".format(
            target_language, 
            translation_recognition_result.translations[target_language]
        ))
    elif translation_recognition_result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized: {}".format(translation_recognition_result.no_match_details))
    elif translation_recognition_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = translation_recognition_result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))

recognize_and_synthesize_from_microphone()
