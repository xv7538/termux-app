[app]
title = Termux App
package.name = termuxapp
package.domain = org.termux
source.include_exts = py,png,jpg,kv,atlas
requirements = python3,kivy
orientation = portrait
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

[buildozer]
log_level = 2
warn_on_root = 1
