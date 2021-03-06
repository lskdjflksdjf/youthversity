from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('', include('django.contrib.auth.urls')),
    path('feed/', views.feed, name='feed'),
    path('topics/', views.topics, name='topics'),
    path('topics/<int:id>/subtopics/', views.subtopics, name='subtopics'),
    path('projects/filter/', views.projects_filter, name='projects_filter'),
    path('projects/all/', views.projects_all, name='projects_all'),
    path('projects/my/', views.projects_my, name='projects_my'),
    path('projects/new/', views.projects_new, name='projects_new'),
    path('projects/<int:id>/', views.projects_id, name='projects_id'),
    path('projects/<int:id>/report/', views.report, name='report'),
    path('projects/<int:id>/new_comment/', views.project_new_comment, name='project_new_comment'),
    path('projects/saved/', views.projects_saved, name='projects_saved'),
    path('comments/my/', views.comments_my, name='comments_my'),
    # path('help/', views.help, name='help'),
    path('faq/', views.faq, name='faq'),
    path('imprint/', views.imprint, name='imprint'),
    path('privacy/', views.privacy, name='privacy'),
    path('me/', views.me, name='me'),
    path('comment_guidelines/', views.comment_guidelines, name='comment_guidelines'),
    path('project_guidelines/', views.project_guidelines, name='project_guidelines'),
    path('about_us/', views.about_us, name='about_us'),
    path('copyright/', views.copyright, name='copyright'),
    path('profile/', views.me, name='profile'),
    path('upvote_post/<int:id>/', views.upvote_post, name='upvote_post'),
    path('upvote_comment/<int:id>/', views.upvote_comment, name='upvote_comment'),
]
