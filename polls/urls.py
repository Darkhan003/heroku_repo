from django.urls import path
from .views import send_message, HomeView, AddPostView, ArticleDetailView
from django.conf import settings
from  django.conf.urls.static import static
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('send/', send_message),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

