from django.contrib import admin
from .models import Post, Comment
# 同ディレクトリのPostクラスをインポート

admin.site.register(Post) # modelをadminページ上で見えるように登録する
admin.site.register(Comment) # コメントモデルを登録（migrationsした)

