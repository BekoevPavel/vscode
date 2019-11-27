
from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import landing
import blog
import home
urlpatterns = [
    url(r'^admin/', admin.site.urls),

     url(r'^blog/', include('blog.urls')),
     url(r'', include('home.urls')),
     url(r'^landing/', include('landing.urls')),
]

urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)