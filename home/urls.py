from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'freelancer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #urls of worker section
    url(r'^$', 'home.views.mainpage',name='mainpage'),
    #url(r'^profile$', 'home.views.profile',name='profile'),
    #url(r'^create_info$', 'home.views.create_info',name='create_info'),
    #url(r'^modify_info$', 'home.views.modify_info',name='modify_info'),
    #url(r'^change_password$', 'home.views.change_password',name='change_password'),
    #url(r'^modify_skills$', 'home.views.modify_skills',name='modify_skills'),
    #url(r'^list_jobs/(?P<category_id>.+)/$', 'home.views.list_jobs',name='list_jobs'),
    #url(r'^list_jobs/$','home.views.list_jobs',name='list_jobs'),
    #url(r'^job_info/(?P<job_id>.+)$', 'home.views.job_info',name='job_info'),
    #url(r'^delete_skill/(?P<skill_id>.+)$', 'home.views.delete_skill',name='delete_skill'),
    #urls of hirer section
    #url(r'^hire$', 'home.views.mainpage_hire',name='mainpage_hire'),
    url(r'^look_profile/(?P<worker_id>.+)$', 'home.views.look_profile',name='look_profile'),
    url(r'^list_workers/(?P<category_id>.+)/$', 'home.views.list_workers',name='list_workers'),
    url(r'^list_workers/$','home.views.list_workers',name='list_workers'),
    #url(r'^my_projects$', 'home.views.my_projects',name='my_projects'),
    #url(r'^delete_job/(?P<job_id>.+)$', 'home.views.delete_job',name='delete_job'),
)
