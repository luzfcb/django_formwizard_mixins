from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from views import (
    MIXIN_DEMO_WIZARD_DONE_URL_NAME,
    MIXIN_DEMO_WIZARD_STEP_URL_NAME,
    MIXIN_DEMO_WIZARD_CONFIRM_ALL_DONE_URL_NAME,
    MIXIN_DEMO_WIZARD_CONFIRM_ALL_STEP_URL_NAME,
    home_demo_wizard_view,
    mixin_demo_wizard_view,
    mixin_demo_wizard_confirm_all_view)

urlpatterns = patterns('',
    # Examples:
    url(r'^$', home_demo_wizard_view, name='home-wizard-demo'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^example1/$', mixin_demo_wizard_view, name=MIXIN_DEMO_WIZARD_DONE_URL_NAME),
    url(r'^example1/(?P<step>.+)/$', mixin_demo_wizard_view, name=MIXIN_DEMO_WIZARD_STEP_URL_NAME),

    url(r'^example2/$', mixin_demo_wizard_confirm_all_view, name=MIXIN_DEMO_WIZARD_CONFIRM_ALL_DONE_URL_NAME),
    url(r'^example2/(?P<step>.+)/$', mixin_demo_wizard_confirm_all_view, name=MIXIN_DEMO_WIZARD_CONFIRM_ALL_STEP_URL_NAME),

    url(r'^admin/', include(admin.site.urls)),
)
