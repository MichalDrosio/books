from django.urls import path

from api.views import BookListView, BookDetailView
app_name ='api'

urlpatterns = [
    path('books/', BookListView.as_view(), name='book_list_api'),
    path('books/<pk>', BookDetailView.as_view(), name='book_detail_api'),

]