from django.contrib import admin
from django.urls import path
from core.views import (
    home, dashboard, projects, boards, teams, tasks,
    delete_project, delete_board, delete_team, delete_task,
    update_task_status, assign_task, unassign_task,
    task_detail, team_detail, team_add_member, team_remove_member,
    add_comment, delete_comment,
    upload_attachment, delete_attachment, download_attachment,
    notifications, mark_notification_read, mark_all_notifications_read,
    add_dependency, remove_dependency,
    analytics, export_projects_csv, export_tasks_csv, generate_report,
    api_projects, api_tasks, api_teams, api_stats, api_task_detail, get_realtime_updates
)

urlpatterns = [
    # Main pages
    path('', home, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('projects/', projects, name='projects'),
    path('boards/', boards, name='boards'),
    path('teams/', teams, name='teams'),
    path('tasks/', tasks, name='tasks'),
    
    # Detail pages
    path('task/<int:task_id>/', task_detail, name='task_detail'),
    path('team/<int:team_id>/', team_detail, name='team_detail'),
    
    # Delete actions
    path('project/delete/<int:project_id>/', delete_project, name='delete_project'),
    path('board/delete/<int:board_id>/', delete_board, name='delete_board'),
    path('team/delete/<int:team_id>/', delete_team, name='delete_team'),
    path('task/delete/<int:task_id>/', delete_task, name='delete_task'),
    
    # Task actions
    path('task/update-status/<int:task_id>/', update_task_status, name='update_task_status'),
    path('task/assign/<int:task_id>/', assign_task, name='assign_task'),
    path('task/unassign/<int:task_id>/', unassign_task, name='unassign_task'),
    
    # Team actions
    path('team/add-member/<int:team_id>/', team_add_member, name='team_add_member'),
    path('team/remove-member/<int:team_id>/', team_remove_member, name='team_remove_member'),
    
    # Comments
    path('comment/add/<int:task_id>/', add_comment, name='add_comment'),
    path('comment/delete/<int:comment_id>/', delete_comment, name='delete_comment'),
    
    # Attachments
    path('attachment/upload/<int:task_id>/', upload_attachment, name='upload_attachment'),
    path('attachment/delete/<int:attachment_id>/', delete_attachment, name='delete_attachment'),
    path('attachment/download/<int:attachment_id>/', download_attachment, name='download_attachment'),
    
    # Notifications
    path('notifications/', notifications, name='notifications'),
    path('notification/read/<int:notification_id>/', mark_notification_read, name='mark_notification_read'),
    path('notifications/read/all/', mark_all_notifications_read, name='mark_all_notifications_read'),
    
    # Dependencies
    path('dependency/add/<int:task_id>/', add_dependency, name='add_dependency'),
    path('dependency/remove/<int:dependency_id>/', remove_dependency, name='remove_dependency'),
    
    # Analytics & Reports
    path('analytics/', analytics, name='analytics'),
    path('export/projects/', export_projects_csv, name='export_projects_csv'),
    path('export/tasks/', export_tasks_csv, name='export_tasks_csv'),
    path('report/generate/<int:project_id>/', generate_report, name='generate_report'),
    
    # API Endpoints
    path('api/projects/', api_projects, name='api_projects'),
    path('api/tasks/', api_tasks, name='api_tasks'),
    path('api/teams/', api_teams, name='api_teams'),
    path('api/stats/', api_stats, name='api_stats'),
    path('api/task/<int:task_id>/', api_task_detail, name='api_task_detail'),
    path('api/realtime/', get_realtime_updates, name='get_realtime_updates'),
    
    # Admin
    path('admin/', admin.site.urls),
]
