from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar
from kivy.clock import Clock

from downloader import DownloadManager


class DownloaderUI(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation = "vertical"
        self.padding = 20
        self.spacing = 15

        self.link_input = TextInput(
            hint_text="Enter URL",
            size_hint_y=None,
            height=50
        )

        self.add_widget(self.link_input)

        self.status = Label(
            text="Ready",
            size_hint_y=None,
            height=40
        )

        self.add_widget(self.status)


        self.progress = ProgressBar(
            max=100,
            value=0,
            size_hint_y=None,
            height=30
        )

        self.add_widget(self.progress)


        self.download_button = Button(
            text="Download",
            size_hint_y=None,
            height=60
        )

        self.download_button.bind(
            on_press=self.start_download
        )

        self.add_widget(self.download_button)


        self.paste_button = Button(
            text="Paste Link",
            size_hint_y=None,
            height=60
        )

        self.paste_button.bind(
            on_press=self.paste_link
        )

        self.add_widget(self.paste_button)


        self.manager = DownloadManager(
            self.update_progress,
            self.update_status
        )


    def paste_link(self, instance):
        import pyperclip
        self.link_input.text = pyperclip.paste()


    def start_download(self, instance):

        url = self.link_input.text

        if url:
            self.status.text = "Downloading..."
            self.manager.download(url)


    def update_progress(self, value):

        Clock.schedule_once(
            lambda dt: setattr(
                self.progress,
                "value",
                value
            )
        )


    def update_status(self, message):

        Clock.schedule_once(
            lambda dt: setattr(
                self.status,
                "text",
                message
            )
        )