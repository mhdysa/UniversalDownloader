import pyperclip


class ClipboardManager:


    @staticmethod
    def copy(text):

        pyperclip.copy(text)



    @staticmethod
    def paste():

        return pyperclip.paste()