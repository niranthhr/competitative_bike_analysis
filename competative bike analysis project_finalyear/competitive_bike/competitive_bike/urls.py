"""competitive_bike URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from Remote_User import views as remoteuser
from competitive_bike import settings
from Service_Provider import views as serviceprovider
from django.conf.urls.static import static


urlpatterns = [
    url('admin/', admin.site.urls),

    url(r'^$', remoteuser.login, name="login"),


    url(r'^Register1/$', remoteuser.Register1, name="Register1"),

    url(r'^Share/(?P<pk>\d+)/$', remoteuser.Share, name="Share"),
    url(r'^Review/(?P<pk>\d+)/$', remoteuser.Review, name="Review"),
    url(r'^ViewAllAppDetails/$', remoteuser.ViewAllAppDetails, name="ViewAllAppDetails"),
    url(r'^Viewreviews/$', remoteuser.Viewreviews, name="Viewreviews"),
    url(r'^ratings/(?P<pk>\d+)/$', remoteuser.ratings, name="ratings"),
    url(r'^dislikes/(?P<pk>\d+)/$', remoteuser.dislikes, name="dislikes"),
    url(r'^likes/(?P<pk>\d+)/$', remoteuser.likes, name="likes"),
    url(r'ViewTrending/$', remoteuser.ViewTrending, name="ViewTrending"),
    url(r'^ViewYourProfile/$', remoteuser.ViewYourProfile, name="ViewYourProfile"),
    url(r'^viewallappshared_details/$', remoteuser.viewallappshared_details, name="viewallappshared_details"),

    url(r'^Upload_Apps/$', serviceprovider.Upload_Apps, name="Upload_Apps"),
    url(r'^serviceproviderlogin/$',serviceprovider.serviceproviderlogin, name="serviceproviderlogin"),
    url(r'viewallclients/$',serviceprovider.viewallclients,name="viewallclients"),
    url(r'ViewTrendings/$',serviceprovider.ViewTrendings,name="ViewTrendings"),
    url(r'^charts/(?P<chart_type>\w+)', serviceprovider.charts,name="charts"),
    url(r'^dislikeschart/(?P<dislike_chart>\w+)', serviceprovider.dislikeschart,name="dislikeschart"),
    url(r'^likeschart/(?P<like_chart>\w+)', serviceprovider.likeschart,name="likeschart"),
    url(r'^View_AllApps_Details/$',serviceprovider.View_AllApps_Details, name='View_AllApps_Details'),
    url(r'^viewallpostsreviews/$', serviceprovider.viewallpostsreviews, name='viewallpostsreviews'),
    url(r'^viewallappshared/$', serviceprovider.viewallappshared, name='viewallappshared'),

     url(r'^Positivereviews/$', serviceprovider.Positivereviews, name="Positivereviews"),
    url(r'^Negativereviews/$', serviceprovider.Negativereviews, name="Negativereviews"),
    url(r'^Neutralreviews/$', serviceprovider.Neutralreviews, name="Neutralreviews"),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
