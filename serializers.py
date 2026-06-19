from rest_framework import serializers
from .models import (
    User, Organization, Team, Project, Board, Task, 
    Comment, Attachment, ActivityLog, Notification
)

class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'full_name', 
                 'phone', 'avatar', 'bio', 'last_seen', 'created_at']
        read_only_fields = ['id', 'created_at', 'last_seen']
    
    def get_full_name(self, obj):
        return obj.get_full_name()

class OrganizationSerializer(serializers.ModelSerializer):
    owner_details = UserSerializer(source='owner', read_only=True)
    
    class Meta:
        model = Organization
        fields = ['id', 'name', 'slug', 'description', 'logo', 'owner', 'owner_details',
                 'created_at', 'updated_at', 'is_active']
        read_only_fields = ['id', 'slug', 'created_at', 'updated_at']

class TeamSerializer(serializers.ModelSerializer):
    lead_details = UserSerializer(source='lead', read_only=True)
    
    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'organization', 'lead', 'lead_details',
                 'created_at', 'updated_at', 'is_active']
        read_only_fields = ['id', 'created_at', 'updated_at']

class ProjectSerializer(serializers.ModelSerializer):
    owner_details = UserSerializer(source='owner', read_only=True)
    
    class Meta:
        model = Project
        fields = ['id', 'name', 'slug', 'description', 'organization', 'owner', 'owner_details',
                 'status', 'priority', 'start_date', 'end_date', 'created_at', 'updated_at', 'is_active']
        read_only_fields = ['id', 'slug', 'created_at', 'updated_at']

class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['id', 'name', 'description', 'project', 'columns', 'is_default',
                 'created_at', 'updated_at', 'is_active']
        read_only_fields = ['id', 'created_at', 'updated_at']

class TaskSerializer(serializers.ModelSerializer):
    reporter_details = UserSerializer(source='reporter', read_only=True)
    
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'priority', 'project', 'board',
                 'reporter', 'reporter_details', 'due_date', 'created_at', 'updated_at', 
                 'completed_at', 'is_active']
        read_only_fields = ['id', 'created_at', 'updated_at', 'completed_at']

class CommentSerializer(serializers.ModelSerializer):
    user_details = UserSerializer(source='user', read_only=True)
    
    class Meta:
        model = Comment
        fields = ['id', 'content', 'user', 'user_details', 'content_type', 'object_id',
                 'created_at', 'updated_at', 'is_deleted']
        read_only_fields = ['id', 'created_at', 'updated_at']

class AttachmentSerializer(serializers.ModelSerializer):
    user_details = UserSerializer(source='user', read_only=True)
    
    class Meta:
        model = Attachment
        fields = ['id', 'file', 'name', 'user', 'user_details', 'file_size',
                 'content_type', 'object_id', 'created_at']
        read_only_fields = ['id', 'created_at']

class NotificationSerializer(serializers.ModelSerializer):
    actor_details = UserSerializer(source='actor', read_only=True)
    
    class Meta:
        model = Notification
        fields = ['id', 'recipient', 'actor', 'actor_details', 'verb', 'description',
                 'notification_type', 'is_read', 'read_at', 'created_at']
        read_only_fields = ['id', 'created_at']
