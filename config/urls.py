from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from master.urls import master_router
from django.views.generic import TemplateView


api_urlpatterns = [
    # マスタ系画面API
    path('masters/', include(master_router.urls)),
]

urlpatterns = [
    # Django管理画面URL
    path('admin/', admin.site.urls),
    # 通常ログイン用URL
    path('accounts/', include('django.contrib.auth.urls')),
    # Googlen認証用URL
    path('auth/', include('social_django.urls', namespace='social')),
    # APIのベースURL
    path('api/', include(api_urlpatterns)),
    # ログイン後の初期画面HTML
    path('', login_required(TemplateView.as_view(template_name="vue/index.html")), name='index'),
] + static(settings.STATIC_URL)

# 開発環境でメディアファイルにアクセスする
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)