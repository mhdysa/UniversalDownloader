[app]

title = Universal Downloader

package.name = universaldownloader

package.domain = org.universal

source.dir = .

source.include_exts = py,png,jpg,kv,json

version = 1.0.0

requirements = python3,kivy,kivymd,requests,pillow,pyperclip

orientation = portrait

fullscreen = 0


# Application icon

icon.filename = %(source.dir)s/icon.png


# Android permissions

android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE


# Android configuration

android.api = 35

android.minapi = 23

android.ndk = 25b

android.archs = arm64-v8a,armeabi-v7a


# Python settings

p4a.branch = master


# Build settings

android.accept_sdk_license = True

android.enable_androidx = True


# Include assets

source.include_patterns = assets/*


# Logging

log_level = 2


[buildozer]

warn_on_root = 1[app]

title = Universal Downloader

package.name = universaldownloader

package.domain = org.universal

source.dir = .

source.include_exts = py,png,jpg,kv,json

version = 1.0.0

requirements = python3,kivy,kivymd,requests,pillow,pyperclip

orientation = portrait

fullscreen = 0


# Application icon

icon.filename = %(source.dir)s/icon.png


# Android permissions

android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE


# Android configuration

android.api = 35

android.minapi = 23

android.ndk = 25b

android.archs = arm64-v8a,armeabi-v7a


# Python settings

p4a.branch = master


# Build settings

android.accept_sdk_license = True

android.enable_androidx = True


# Include assets

source.include_patterns = assets/*


# Logging

log_level = 2


[buildozer]

warn_on_root = 1
