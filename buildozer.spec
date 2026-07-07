[app]

title = Universal Downloader

package.name = universaldownloader

package.domain = org.example

source.dir = .

source.include_exts = py,png,jpg,kv,ico

version = 1.0

requirements = python3,kivy,kivymd,yt-dlp,pyperclip,requests,pillow

orientation = portrait

fullscreen = 0


# Android permissions

android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE


# Application icon

icon.filename = %(source.dir)s/icon.png


# Android settings

android.api = 35

android.minapi = 23

android.archs = arm64-v8a, armeabi-v7a


# Build options

presplash.filename = %(source.dir)s/icon.png


[buildozer]

log_level = 2