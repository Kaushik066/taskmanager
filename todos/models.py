from django.db import models
from datetime import datetime

class Todo(models.Model):
	title = models.CharField(max_length = 200)
	text = models.TextField()
	created_at = models.DateTimeField(default = datetime.now, blank = 'true')
	status = models.CharField(max_length = 200, default = 'not completed')
	def __str__(self):
		return self.title		
		
