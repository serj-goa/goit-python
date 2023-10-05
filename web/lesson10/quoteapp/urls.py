from django.urls import path

from . import views as v


app_name = 'quoteapp'

urlpatterns = [
    path('', v.main, name='main'),
    path('page/<int:page>', v.main, name='main_paginate'),
    path('author/<str:author_name>', v.author_detail, name='author_detail'),
    path('tag/<str:tag_name>/', v.quotes_by_tag, name='quotes_by_tags'),
    path('tag/<str:tag_name>/page/<int:page>/', v.quotes_by_tag, name='quotes_by_tags_paginate'),
    path('quote/', v.quote, name='quote'),
    path('add-author/', v.author, name='author'),
]
