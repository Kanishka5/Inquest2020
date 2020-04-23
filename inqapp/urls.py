from django.urls import path
from django.conf.urls import url,include
from inqapp import views
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    #url(r'^question/(?P<pk>\d+)/$', views.question, name='question'),
    path('leaderboard/', views.leaderboard,name='leaderboard'),
    #path('test', TemplateView.as_view(template_name='question.html'), name='test'),
    #path('test',views.test,name='test'),
    path('contact-us/',views.contact,name='contact'),
    path('', views.home,name='home'),
    #path('test', TemplateView.as_view(template_name='question.html'), name='test'),
    #path('test', views.test,name='test'),
    path('inquest/', views.question,name='inquest'),
    path('logout/',views.logoutred,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('accounts/profile/',views.profile,name='profile'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^auth/', include('social_django.urls', namespace='social')),
    url('nopage',views.noPage, name="404")
    #url(r'^(?P<string>[ \w\-]+)/$',views.question, name=''),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
