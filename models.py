from django.db import models

class ModelName1(models.Model):
  class Meta():
    db_table = 'table_name'
                
  title = models.CharField(max_length = 200)
  text = models.TextField()
  date = models.DateTimeField()
  likes = models.IntegerField(default=0)
        	
class ModelName2(models.Model):
  class Meta():
    db_table = 'table_name'
                
  text = models.TextField()
  article = models.ForeignKey(ModelName1)
