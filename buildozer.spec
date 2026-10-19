[app]
title = Texss Systems Store
package.name = texsssystemsstore
package.domain = org.texss

# تحديد مسار الملفات والامتدادات وتشمل الصور
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
source.include_patterns = Images/*

version = 1.0
requirements = python3,kivy

orientation = portrait

# إعدادات التوافق مع أندرويد 5 (API 21)
android.api = 21
android.minapi = 21
android.sdk = 20
android.ndk = 19b
android.archs = armeabi-v7a
