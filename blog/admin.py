from django.contrib import admin
from .models import Post
# 同ディレクトリのPostクラスをインポート

admin.site.register(Post) # modelをadminページ上で見えるように登録する

