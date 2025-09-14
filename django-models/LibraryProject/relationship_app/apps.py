from django.apps import AppConfig


# relationship_app/apps.py
from django.apps import AppConfig

class RelationshipAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # type: ignore
    name = 'relationship_app'
