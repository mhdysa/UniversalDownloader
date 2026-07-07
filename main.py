from kivy.app import App
from ui import DownloaderUI


class UniversalDownloaderApp(App):

    def build(self):
        self.title = "Universal Downloader"
        return DownloaderUI()


if __name__ == "__main__":
    UniversalDownloaderApp().run()