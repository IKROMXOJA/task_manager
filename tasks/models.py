from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)          # Vazifa nomi
    description = models.TextField(blank=True)        # Tavsif (majburiy emas)
    completed = models.BooleanField(default=False)    # Bajarilgan yoki yo‘q
    created_at = models.DateTimeField(auto_now_add=True)  # Qo‘shilgan vaqt

    def __str__(self):
        return self.title
