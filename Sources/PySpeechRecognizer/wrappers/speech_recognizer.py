


@wrapper
class SpeechRecognizer:

    def __init__(self, locale: str): ...

    class Callbacks:

        def speak(self,message: str): ...


    def start(self): ...

    def stop(self): ...