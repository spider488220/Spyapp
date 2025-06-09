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
android.api = 33
android.sdk = 33
android.build_tools = 33.0.0
android.ndk = 25
android.p4a_branch = develop
android.use_prebuilt_python = True
android.skip_update = False

[buildozer]
log_level = 2
warn_on_root = 0

[android]
# Architecture and minimum API
android.arch = armeabi-v7a
android.minapi = 21

# Gradle
android.gradle_dependencies = com.android.tools.build:gradle:7.2.2

# Enable AndroidX
android.use_androidx = True
android.enable_androidx = True
android.enable_jetifier = True

# Backup & artifacts
android.allow_backup = False
android.accept_sdk_license = True
android.release_artifact = False
android.debug_artifact = True

# (Optional) Permissions — uncomment if your app needs these:
# android.permissions = CAMERA,RECORD_AUDIO,INTERNET,ACCESS_FINE_LOCATION,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE
