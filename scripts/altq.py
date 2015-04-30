__author__ = 'frank'
if __name__ == "__main__":
    import os
    print "####### DJANGO SETTINGS"
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "protoboard.settings")


from activitytree.models import LearningStyleInventory, LearningActivity, Course, UserLearningActivity
from django.contrib.auth.models import User
from activitytree.interaction_handler import SimpleSequencing
User.objects.filter(username='frank').delete()
for i in range(20):

    nombre = "users"+str(i)
    edad = 8
    grado = 8
    correo='ejemlo@ejemplo.com'

    j = User.objects.create_user(nombre,correo,'1234' )
    j.is_active = True
    j.save()

    lsu=LearningStyleInventory(visual=0,verbal=0,aural=0,physical=0,logical=0,
                          social=0, solitary=0, age=edad, aca_lvl=grado, user = j)
    lsu.save()
    s = SimpleSequencing()

    a=LearningActivity.objects.all()
    print a[0]
    s.assignActivityTree(j,a[0])