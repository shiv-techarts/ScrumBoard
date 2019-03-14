from django.contrib import admin
from .models import List, Card


admin.site.register([List, Card])
