"""movieleaks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from catalogues import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    url(r'^$', views.index, name='home'),

    url(r'^bog/$', views.bog, name='bog'),
    url(r'^pta/$', views.pta, name='pta'),
    url(r'^principal/$', views.principal, name='principal'),
    url(r'^deputies/$', views.deputies, name='deputies'),

    url(r'^history/$', views.history, name='history'),
    url(r'^philosophy/$', views.philosophy, name='philosophy'),
    url(r'^location/$', views.location, name='location'),

    url(r'^hods/$', views.hods, name='hods'),
    url(r'^teachers/$', views.teachers, name='teachers'),
    url(r'^students/$', views.students, name='students'),

    url(r'^languages/$', views.languages, name='languages'),
    url(r'^sciences/$', views.sciences, name='sciences'),
    url(r'^boarding/$', views.boarding, name='boarding'),
    url(r'^games/$', views.games, name='games'),
    url(r'^guidance/$', views.guidance, name='guidance'),
    url(r'^humanities/$', views.humanities, name='humanities'),
    url(r'^mathematics/$', views.mathematics, name='mathematics'),
    url(r'^technicals/$', views.technicals, name='technicals'),

    url(r'^bakery/$', views.bakery, name='bakery'),
    url(r'^library/$', views.library, name='library'),
    url(r'^laboratories/$', views.laboratories, name='laboratories'),
    url(r'^dininghall/$', views.dininghall, name='dininghall'),
    url(r'^classrooms/$', views.classrooms, name='classrooms'),
    url(r'^transport/$', views.transport, name='transport'),
    url(r'^schoolfence/$', views.schoolfence, name='schoolfence'),
    url(r'^forest/$', views.forest, name='forest'),
    url(r'^carpark/$', views.carpark, name='carpark'),
    url(r'^generator/$', views.generator, name='generator'),
    url(r'^beautification/$', views.beautification, name='beautification'),

    url(r'^muslimstudents/$', views.muslimstudents, name='muslimstudents'),
    url(r'^christianunion/$', views.christianunion, name='christianunion'),
    url(r'^debate/$', views.debate, name='debate'),
    url(r'^drama/$', views.drama, name='drama'),
    url(r'^journalism/$', views.journalism, name='journalism'),
    url(r'^music/$', views.music, name='music'),
    url(r'^sports/$', views.sports, name='sports'),
    url(r'^scienceengineering/$', views.scienceengineering, name='scienceengineering'),
    url(r'^peace/$', views.peace, name='peace'),

    url(r'^performance/$', views.performance, name='performance'),
    url(r'^university/$', views.university, name='university'),

    url(r'^updates/$', views.updates, name='updates'),
    url(r'^alumnae/$', views.alumnae, name='alumnae'),
    url(r'^downloads/$', views.downloads, name='downloads'),

    url(r'^anthem/$', views.anthem, name='anthem'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^success/$', views.successView, name='success'),
    url(r'^error/$', views.errorView, name='failure'),
    url(r'^corevalues/$', views.corevalues, name='corevalues'),

    url(r'^search/$', views.search, name='search'),

    url(r'^admin/', admin.site.urls),

]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
