import yt_dlp
import os


class DownloadManager:

    def __init__(self, progress_callback, status_callback):

        self.progress_callback = progress_callback
        self.status_callback = status_callback


    def download(self, url):

        folder = "Downloads"

        if not os.path.exists(folder):
            os.makedirs(folder)


        options = {

            "format":
            "bestvideo+bestaudio/best",

            "outtmpl":
            f"{folder}/%(title)s.%(ext)s",

            "progress_hooks":
            [
                self.progress_hook
            ],

            "merge_output_format":
            "mp4"
        }


        try:

            with yt_dlp.YoutubeDL(options) as ydl:

                ydl.download([url])


            self.status_callback(
                "Download Complete"
            )


        except Exception as error:

            self.status_callback(
                "Download Failed"
            )


    def progress_hook(self, data):

        if data["status"] == "downloading":

            total = data.get(
                "total_bytes",
                data.get("total_bytes_estimate", 1)
            )

            downloaded = data.get(
                "downloaded_bytes",
                0
            )


            percent = (
                downloaded / total
            ) * 100


            self.progress_callback(
                percent
            )