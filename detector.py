from urllib.parse import urlparse


class WebsiteDetector:

    def detect(self, url):

        domain = urlparse(url).netloc.lower()


        if "youtube.com" in domain or "youtu.be" in domain:
            return {
                "name": "YouTube",
                "icon": "assets/youtube.png"
            }


        elif "instagram.com" in domain:
            return {
                "name": "Instagram",
                "icon": "assets/instagram.png"
            }


        elif "facebook.com" in domain:
            return {
                "name": "Facebook",
                "icon": "assets/facebook.png"
            }


        elif "tiktok.com" in domain:
            return {
                "name": "TikTok",
                "icon": "assets/tiktok.png"
            }


        elif "x.com" in domain or "twitter.com" in domain:
            return {
                "name": "X",
                "icon": "assets/x.png"
            }


        else:
            return {
                "name": "Website",
                "icon": "assets/website.png"
            }