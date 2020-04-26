import speech_recognition as sr
from speech import speak
from extendedfunc import terminate


def listMicros():
    mic_list = sr.Microphone.list_microphone_names()
    for i, microphone_name in enumerate(mic_list):
        print(str(i) + microphone_name)


class Ears:
    sample_rate = 48000
    chunk_size = 2048
    recognizer = sr.Recognizer()
    print("mic initialized")

    def run(self):
        with sr.Microphone(sample_rate=self.sample_rate, chunk_size=self.chunk_size) as source:
            self.recognizer.adjust_for_ambient_noise(source)
            try:
                print("listening:")
                audio = self.recognizer.listen(source)
                string = self.recognizer.recognize_google(audio)
                string = str(string).lower()
                print(string)
                if str(string).lower == 'exit':
                    print("exited")
                    terminate()
                else:
                    return string

            except Exception as e:
                return ""
