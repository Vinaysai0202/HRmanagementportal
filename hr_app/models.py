from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    empid = models.CharField(max_length=20, unique=True)
    designation = models.CharField(max_length=50)
    date_of_joining = models.DateField()
    department = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    experience = models.PositiveIntegerField()

    def __str__(self):
        return self.name
    
class Holiday(models.Model):
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f"Holiday on {self.date}"
    
class NewsArticle(models.Model):
    heading = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return(self.heading)

