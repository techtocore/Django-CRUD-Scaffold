from rest_framework import routers
from CRUD_App import api_views as myapp_views

router = routers.DefaultRouter()
router.register(r'SampleObjects', myapp_views.SampleObjectViewset)