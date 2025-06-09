[app]
title = SpyApp
package.name = spyapp
package.domain = org.spider.spyapp
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.1.0
orientation = portrait
fullscreen = 1
osx.python_version = 3
osx.kivy_version = 2.1.0

# Android-specific settings
android.api = 29
android.sdk = 29
android.build_tools = 29.0.0
android.ndk = 25
android.p4a_branch = develop
android.use_prebuilt_python = True
android.skip_update = False

[buildozer]
log_level = 2
warn_on_root = 0

[android]
# Architecture and minimum API
android.arch = arm64-v8a
android.minapi = 21


# Backup & artifat
android.accept_sdk_license = True

# (Optional) Permissions — uncomment if your app needs these:
# android.permissions = CAMERA,RECORD_AUDIO,INTERNET,ACCESS_FINE_LOCATION,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE
