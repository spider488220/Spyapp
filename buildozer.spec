[app]
title = SpyApp
package.name = spyapp
package.domain = org.spider.spyapp
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 1
android.build_tools = 31.0.0
android.api = 31
android.p4a_branch = develop
android.use_prebuilt_python = true
android.accept_sdk_license = True
android.skip_update = Fals
android.ndk = 25b
android.arch = armeabi-v7a  # Build only 32-bit ARM
[buildozer]
log_level = 2
warn_on_root = 0
