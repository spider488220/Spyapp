[app]
title = SpyApp
package.name = spyapp
package.domain = org.spider.spyapp
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.1.0,android
orientation = portrait
osx.python_version = 3
osx.kivy_version = 2.1.0
fullscreen = 1
android.build_tools = 31.0.0
android.api = 33
android.p4a_branch = develop
android.use_prebuilt_python = true
android.accept_sdk_license = True
android.skip_update = Fals
[buildozer]
log_level = 2
warn_on_root = 0

[android]
# Build configuration
android.arch = armeabi-v7a  # Build only 32-bit
android.minapi = 21
android.ndk = 25.2.9519653
android.sdk = 33
android.gradle_dependencies = 'com.android.tools.build:gradle:7.2.2'
android.allow_backup = False
android.enable_androidx = True
android.use_androidx = True
android.enable_jetifier = True
