from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [   
    path('', views.article_list, name="list"),
    path('<int:id>', views.article_id, name="article_id"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)