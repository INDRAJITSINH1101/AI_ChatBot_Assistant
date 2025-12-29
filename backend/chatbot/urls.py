from django.urls import path
from .views import chat, train_api, crawl_api, crawl_status

urlpatterns = [
    path("train/", train_api),
    path("chat/", chat),
    path("crawl/", crawl_api),
    path("status/", crawl_status),

]
