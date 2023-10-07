from django.contrib import admin
from hr_app.models import Employee, Holiday,NewsArticle

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['name','empid','designation','date_of_joining','department','salary','experience']

admin.site.register(Employee,EmployeeAdmin)



class HolidayAdmin(admin.ModelAdmin):
    list_display=['date','description']
admin.site.register(Holiday,HolidayAdmin)

class NewsArticleAdmin(admin.ModelAdmin):
    list_display=['heading','content']

admin.site.register(NewsArticle,NewsArticleAdmin)


