# Import modulu admin z balíku django.contrib
from django.contrib import admin
# Import modulu path z balíku django.urls
from django.urls import path
# Import metody include() - pomocí ní připojíme cesty nastavené v souboru urls.py, který je součástí aplikace movies
from django.urls import include
# Třída RedirectView, která je součástí balíku django.views.generic umožňuje přesměrování pohledů (stránek)
from django.views.generic import RedirectView
# Z balíku django.conf importujeme nastavení (settings)
from django.conf import settings
# Z balíku django.conf.urls.static importujeme metodu static(),
# pomocí které zajistíme obsluhu statických souborů (jen ve vývojové fázi aplikace)
from django.conf.urls.static import static

# Mapování URL adres webu - propojení URL s jejich obsluhou
urlpatterns = [
                  # URL "admin/" je namapováno na administrační rozhraní webu
                  path('admin/', admin.site.urls),
                  # URL "movies/" je namapováno na aplikaci movies a její vlastní soubor 'movies.urls'
                  path('formula1/', include('formula1.urls')),
                  path('accounts/', include('accounts.urls')),
                  path('accounts/', include('django.contrib.auth.urls')),
                  # domovská stránka webu ('') je automaticky přesměrována na url z předešlého řádku ('movies')
                  path('', RedirectView.as_view(url='formula1/')),
              ]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
