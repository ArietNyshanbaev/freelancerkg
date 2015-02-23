from django.contrib import admin
from .models import Information,Skill,Category,SkillofUser


admin.site.register(Skill)
admin.site.register(Information)
admin.site.register(Category)
admin.site.register(SkillofUser)


