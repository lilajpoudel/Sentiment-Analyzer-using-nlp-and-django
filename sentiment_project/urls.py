from django.contrib import admin    # ← this line is required
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # ← this line needs the import above
    path('', include('analyzer.urls')),
]
