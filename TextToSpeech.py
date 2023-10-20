import os

import azure.cognitiveservices.speech as speechsdk
from credentials import *

# Creates an instance of a speech config with specified subscription key and service region.
# Replace with your own subscription key and service region (e.g., "westus").
speech_key, service_region = speechkey, "eastus"
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

# uncomment this line to change the voice used for synthesis
#speech_config.speech_synthesis_voice_name = "en-CA-Linda"

# Creates a speech synthesizer using the default speaker as audio output.
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

# ssml_string = open("C://Users//ais//PycharmProjects//pythonProject_AZURE//ssml.xml", "r").read()
# result = speech_synthesizer.speak_ssml_async(ssml_string).get()

# Receives a text from console input.
# print("Type some text that you want to speak...")
# text = input()

# Synthesizes the received text to speech.
# The synthesized speech is expected to be heard on the speaker with this line executed.
result = speech_synthesizer.speak_text_async(text).get()
# # Checks result.
if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    print("Speech synthesized to speaker for text [{}]".format(text))
elif result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = result.cancellation_details
    print("Speech synthesis canceled: {}".format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        if cancellation_details.error_details:
            print("Error details: {}".format(cancellation_details.error_details))
    print("Did you update the subscription info?")

# Creates an audio configuration that points to an audio file.
# Replace with your own audio filename.
audio_filename = "C://Users//ais//PycharmProjects//pythonProject_AZURE//text-to-speech-py.wav"
audio_output = speechsdk.audio.AudioOutputConfig(filename=audio_filename,use_default_speaker=True)

result = speechsdk.AudioDataStream(result)
result.save_to_wav_file("C://Users//ais//PycharmProjects//pythonProject_AZURE//text-to-speech-py.wav")
print("result saved")

print("Done")



#-------------------------------------------------------------------------------------
# import azure.cognitiveservices.speech as speechsdk
# from credentials import *
#
# # Creates an instance of a speech config with specified subscription key and service region.
# # Replace with your own subscription key and service region (e.g., "westus").
# speech_key, service_region = speechkey, "eastus"
# speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
#
# # uncomment this line to change the voice used for synthesis
# #speech_config.speech_synthesis_voice_name = "en-CA-Linda"
#
# # Creates a speech synthesizer using the default speaker as audio output.
# speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)
#
# # Receives a text from console input.
# print("Type some text that you want to speak...")
# text = input()
#
# # Synthesizes the received text to speech.
# # The synthesized speech is expected to be heard on the speaker with this line executed.
# result = speech_synthesizer.speak_text_async(text).get()
#
# # Checks result.
# if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
#     print("Speech synthesized to speaker for text [{}]".format(text))
# elif result.reason == speechsdk.ResultReason.Canceled:
#     cancellation_details = result.cancellation_details
#     print("Speech synthesis canceled: {}".format(cancellation_details.reason))
#     if cancellation_details.reason == speechsdk.CancellationReason.Error:
#         if cancellation_details.error_details:
#             print("Error details: {}".format(cancellation_details.error_details))
#     print("Did you update the subscription info?")
#
# # Creates an audio configuration that points to an audio file.
# # Replace with your own audio filename.
# audio_filename = "C://Users//ais//PycharmProjects//pythonProject_AZURE//text-to-speech-py.wav"
# audio_output = speechsdk.audio.AudioOutputConfig(filename=audio_filename,use_default_speaker=True)
#
