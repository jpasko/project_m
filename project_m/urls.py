from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'portfolios.views.main_page'),
    url(r'^user/(\w+)/$', 'portfolios.views.user_page'),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'portfolios.views.logout_page'),
    url(r'^register/$', 'portfolios.views.register_page'),
    url(r'^register/success/$', direct_to_template,
        {'template': 'registration/register_success.html'}),
    url(r'^password_change/$', 'django.contrib.auth.views.password_change',
        {'post_change_redirect': '/password_changed/'}),
    url(r'^password_changed/$', direct_to_template,
        {'template': 'registration/password_change_done.html'}),
    url(r'^all_users/$', direct_to_template,
        {'template': 'all_users.html'}),
    url(r'^list_users/$', 'portfolios.views.list_users'),
    url(r'^delete/$', 'portfolios.views.delete'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # Simply a test URL to see if AJAX works:
    url(r'^xhr_test/$', 'portfolios.views.xhr_test'),

    # Test to see if user authentication works across apps:
    url(r'^images_test/$', 'images.views.test_view'),

    url(r'^upload_image/$', 'images.views.upload_image'),

    url(r'^gallery/(\w+)/$', 'images.views.all_portfolio_images'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
    )
