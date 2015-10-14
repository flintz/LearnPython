from django.db import models

class Article(models.Model):
  class Meta():
    db_table = 'article'
  
  #CharField fields : max_length, null, blank, default
  name  = models.CharField("artist", max_length=50)
  title = models.CharField(max_length = 200)
  text  = models.TextField()
  date  = models.DateTimeField()
  date1 = models.DateTimeField(blank=true, null=True)
  like  = models.IntegerField(default=0)
  #IntegerField fields: null, default
  year_formed = models.PositiveIntegerField()
  
  # field choices
    SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
  size = models.CharField(max_length=1, choices=SIZES)
        	
class Comments(models.Model):
  class Meta():
    db_table = 'table_name'
                
  text = models.TextField()
  article = models.ForeignKey(Article)
