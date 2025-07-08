"""
URL configuration for HateSpeech project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from hate_speech_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('c_update', views.c_update, name="c_update"),
    path('u_update', views.u_update, name="u_update"),
    path('registration', views.registration, name="registration"),
    path('customer_login', views.customer_login, name="customer_login"),
    path('my_profile', views.my_profile, name="my_profile"),
    path('customer_change_password', views.customer_change_password, name="customer_change_password"),
    path('customer_view_details/<int:id>', views.customer_view_details, name="customer_view_details"),
    path('customer_view_notifications', views.customer_view_notifications, name="customer_view_notifications"),
    path('customer_home', views.customer_home, name="customer_home"),

    path('admin_change_password', views.admin_change_password, name="admin_change_password"),
    path('admin_view_contact', views.admin_view_contact, name="admin_view_contact"),
    path('admin_view_customer', views.admin_view_customer, name="admin_view_customer"),
    path('admin_loginn', views.admin_loginn, name="admin_loginn"),
    path('admin_logout', views.admin_logout, name="admin_logout"),
    path('admin_home', views.admin_home, name="admin_home"),
    path('admin_add_notifications', views.admin_add_notifications, name="admin_add_notifications"),
    path('admin_view_notification', views.admin_view_notification, name="admin_view_notification"),
    path('logout', views.logout, name="logout"),
    path('accept_customer/<int:id>', views.accept_customer, name="accept_customer"),
    path('reject_customer/<int:id>', views.reject_customer, name="reject_customer"),
    path('upload_dataset',views.upload_dataset,name="upload_dataset"),
    path('display_polarity_graphs',views.display_polarity_graphs,name="display_polarity_graphs"),
    path('delete_speech/<int:id>',views.delete_speech,name="delete_speech"),

    path('add_speech', views.add_speech, name="add_speech"),
    path('view_my_speech', views.view_my_speech, name="view_my_speech"),
    path('view_all_speech', views.view_all_speech, name="view_all_speech"),
    path('view_positive_speech', views.view_positive_speech, name="view_positive_speech"),
    path('view_negative_speech', views.view_negative_speech, name="view_negative_speech"),
    path('view_hate_speech', views.view_hate_speech, name="view_hate_speech"),
    path('admin_view_speech', views.admin_view_speech, name="admin_view_speech"),
    path('del_customer/<int:id>', views.del_customer, name="del_customer"),
    path('admin_delete_not/<int:id>', views.admin_delete_not, name="admin_delete_not"),
    path('del_coupon/<int:id>', views.del_coupon, name="del_coupon"),
    path('admin_delete_not/<int:id>', views.admin_delete_not, name="admin_delete_not"),


    path('', views.login, name="login"),
    path('Register1/', views.Register1, name="Register1"),
    path('Search_PersonDataSets/', views.Search_PersonDataSets, name="Search_PersonDataSets"),
    path('ViewYourProfile/', views.ViewYourProfile, name="ViewYourProfile"),
    path('Add_DataSet_Details/', views.Add_DataSet_Details, name="Add_DataSet_Details"),
    path('serviceproviderlogin/', views.serviceproviderlogin, name="serviceproviderlogin"),
    path('View_Remote_Users/', views.View_Remote_Users, name="View_Remote_Users"),
    path('charts/<str:chart_type>/', views.charts, name='charts'),
    path('likeschart/<str:like_chart>/', views.likeschart, name='likeschart'),
    path('ratings/<int:pk>/', views.ratings, name='ratings'),
    path('Search_Person/', views.Search_Person, name="Search_Person"),
    path('View_Positive_Speech/', views.View_Positive_Speech, name="View_Positive_Speech"),
    path('View_Negative_Speech/', views.View_Negative_Speech, name="View_Negative_Speech"),
    path('View_HateSpeech_Speech/', views.View_HateSpeech_Speech,
         name="View_HateSpeech_Speech"),
    path('View_PersonSpeechDataSets_Details/', views.View_PersonSpeechDataSets_Details,
         name="View_PersonSpeechDataSets_Details"),
    path('person', views.person, name='person'),
    path('Search_Person_manual_data/', views.Search_Person_manual_data,
         name="Search_Person_manual_data"),
    path('delete_manual_data/<int:id>', views.delete_manual_data, name="delete_manual_data"),
    path('View_PersonSpeechData_Details/', views.View_PersonSpeechData_Details,
         name="View_PersonSpeechData_Details"),
    path('edit_persondata/<int:id>', views.edit_persondata, name="edit_persondata"),
    path('update_person/', views.update_person, name="update_person"),
    path('add_notifications/', views.add_notifications, name="add_notifications"),
    path('view_notifications/', views.view_notifications, name="view_notifications"),
    path('delete_notifications/<int:id>/', views.delete_notifications,
         name="delete_notifications"),
    path('view_notification/', views.view_notification, name="view_notification"),
    path('logout', views.logout, name="logout"),
    path('update_profile', views.update_profile, name="update_profile")

]

if settings.DEBUG:  # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
