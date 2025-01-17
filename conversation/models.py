from django.contrib.auth.models import User
from django.db import models

from item.models import Item

# Create your models here.
class Conversation(models.Model):
    item = models.ForeignKey(Item, related_name='conversation', on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-modified_at',)
        verbose_name_plural = 'Conversations'
        
    def __str__(self):
        return self.item.name

class ConversationMessage(models.Model):
    conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE) 
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='created_messages', on_delete=models.CASCADE)


    class Meta:
        verbose_name_plural = 'Conversation Messages'

    def __str__(self):
        return self.content
        
     