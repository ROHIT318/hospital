from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


app_name="account"
urlpatterns = [
	path('', views.home, name='home'),
	path('loginDoctor', views.loginDoctor, name='loginDoctor'),
	path('signupPatient', views.signupPatient, name='signupPatient'),
	path('loginPatient', views.loginPatient, name='loginPatient'),
	path('signupDoctor', views.signupDoctor, name='signupDoctor'),
	path('dashboardShow', views.dashboardShow, name = 'dashboardShow'),
	
	path('logout', views.logout, name = 'logout'),

	path('success', views.success, name = 'success'),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)