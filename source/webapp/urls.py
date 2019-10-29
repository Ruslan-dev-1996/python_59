from django.urls import path
from webapp.view import IndexView, TrackerView, TrackerCreateView, TrackerUpdateView, \
    TrackerDeleteView, StatusView, TypeView, StatusCreateView, TypeCreateView, \
    StatusUpdateView, TypeUpdateView, StatusDeleteView, TypeDeleteView, \
    ProjectView, ProjectDetailView, ProjectCreateView,  ProjectUpdateView, \
    ProjectDeleteView

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('tracker/<int:pk>/', TrackerView.as_view(), name='tracker_view'),
    path('tracker/add/', TrackerCreateView.as_view(), name='tracker_add'),
    path('tracker/<int:pk>/update/', TrackerUpdateView.as_view(), name='tracker_update'),
    path('tracker/<int:pk>/delete/', TrackerDeleteView.as_view(), name='tracker_delete'),
    path('status/view/', StatusView.as_view(), name='status_view'),
    path('type/view/', TypeView.as_view(), name='type_view'),
    path('status/add/', StatusCreateView.as_view(), name='status_add'),
    path('type/add', TypeCreateView.as_view(), name='type_add'),
    path('status/<int:pk>/update/',StatusUpdateView.as_view(), name='status_update'),
    path('type/<int:pk>/update/', TypeUpdateView.as_view(), name='type_update'),
    path('status/<int:pk>/delete/', StatusDeleteView.as_view(), name='status_delete'),
    path('type/<int:pk>/delete/',TypeDeleteView.as_view(), name='type_delete'),
    path('project/view', ProjectView.as_view(), name='project_view'),
    path('project/<int:pk>/detail', ProjectDetailView.as_view(), name='detail_view'),
    path('project/add/', ProjectCreateView.as_view(), name='project_add'),
    path('project/<int:pk>/update/', ProjectUpdateView.as_view(), name='project_update'),
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),

]