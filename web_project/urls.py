
from django.conf.urls import url,include
from django.contrib import admin
import landing
import blog
import home
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^landing/', include('landing.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'', include('home.urls')),
]
