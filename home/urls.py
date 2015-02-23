from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'freelancer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'home.views.mainpage',name='mainpage'),
    url(r'^profile$', 'home.views.profile',name='profile'),
    url(r'^create_info$', 'home.views.create_info',name='create_info'),
    url(r'^add_skill$', 'home.views.add_skill',name='add_skill'),
    
)
