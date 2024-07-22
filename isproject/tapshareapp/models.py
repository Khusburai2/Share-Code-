from django.db import models

class SharedContent(models.Model):
    code = models.CharField(max_length=8, unique=True)
    text = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='uploads/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
