from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group

@receiver(post_migrate)
def create_user_groups(sender, **kwargs):
    # Define the roles/groups
    roles = ['buyer', 'seller', 'agent']
    for role in roles:
        # Get or create the groups in the database
        Group.objects.get_or_create(name=role)
