#import azure.cognitiveservices.speech as speechsdk

# def speak(text):
#     print(text)
#     speech_key, service_region = "98bdfd40c251462288ce87343fe61d89", "eastus"
#     speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
#     speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)
#     result = speech_synthesizer.speak_text_async(text).get()
    
#     if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
#         pass
#     elif result.reason == speechsdk.ResultReason.Canceled:
#         print("There is some trouble.")

def speak(text):
    print(text)