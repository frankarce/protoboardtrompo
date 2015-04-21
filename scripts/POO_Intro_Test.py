# -*- coding: utf-8 -*-

##
##
##  Example of a Learning Activity Tree
##
##



if __name__ == "__main__":
    import os
    print "####### DJANGO SETTINGS"
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "protoboard.settings")






from activitytree.models import LearningStyleInventory, LearningActivity, Course, UserLearningActivity
from django.contrib.auth.models import User
from activitytree.interaction_handler import SimpleSequencing



LearningActivity.objects.all().delete()
##############################          1
agua = LearningActivity( name = 'El agua', slug = 'agua',
    uri = "/activity/POO",
    parent = None,
    root   = None,

    flow = True,
    forward_only = False,
    choice = True,
    choice_exit = False,

    rollup_rule  = "",
    rollup_objective = True,
    rollup_progress = True,

    is_container = True,
    is_visible = True,
    order_in_container = 0
    )

agua.save()
description= u"""
        <p> En este curso aprenderemos cosas relacionadas con el agua .</p>"""


cursoagua = Course(short_description=description, root=agua)
cursoagua.save()

#pretest = LearningActivity( name = 'pretest', slug = 'pretest',
#    uri = "/test/pretest",
#   lom = ,
#    parent = POO, root  = POO,

#    pre_condition_rule = "",
#    post_condition_rule = "" ,

#    rollup_rule  = "",
#    rollup_objective = True,
#    rollup_progress = True,
#    choice_exit = False,


#    is_container = False,
#    is_visible = False,
#    order_in_container = 0
#    )
#pretest.save()


##############################     agua definicion
Aguadef1 = LearningActivity( name = 'Agua', slug = 'Agua',
    uri = "/activity/Agua1",
#   lom =
    parent = agua, root  = agua,
    post_condition_rule = "",

    flow = True,
    forward_only = True,
    choice = False,

    rollup_rule  = "",
    rollup_objective = True,
    rollup_progress = True,
    is_container = True,
    is_visible = True,
    order_in_container = 1
    )
Aguadef1.save()
Aguadef = LearningActivity( name = 'Agua', slug = 'Agua',
    uri = "/activity/Agua",
#   lom =
    parent = Aguadef1, root  = agua,
    post_condition_rule = "",

    flow = True,
    forward_only = True,
    choice = False,

    rollup_rule  = "",
    rollup_objective = True,
    rollup_progress = True,
    is_container = False,
    is_visible = True,
    order_in_container = 1
    )
Aguadef.save()
testaguadef = LearningActivity( name = 'test agua', slug = 'test agua',
    uri = "/test/testaguadef",
#   lom = ,
    parent = Aguadef1, root  = agua,

    pre_condition_rule = """if self.num_attempts == 0 :
 self.pre_condition = 'stopForwardTraversal'
else:
 self.pre_condition = 'hidden'""",
    post_condition_rule = "" ,

    rollup_rule  = "",
    rollup_objective = True,
    rollup_progress = True,

    flow = True,
    forward_only = True,
    choice = False,


    is_container = False,
    is_visible = True,
    order_in_container = 2
    )
testaguadef.save()


# cicloagua1 = LearningActivity( name = 'cicloAgua', slug = 'cicloAgua',
#     uri = "/activity/cicloagua1",
# #   lom =
#     parent = agua, root  = agua,
#     post_condition_rule = "",
#     pre_condition_rule = """if self.user.learningstyleinventory.age > 0 and self.user.learningstyleinventory.age < 18 :
# 	                  self.pre_condition = 'skip' """,
#     flow = True,
#     forward_only = False,
#     choice = False,
#
#     rollup_rule  = "",
#     rollup_objective = True,
#     rollup_progress = True,
#     is_container = True,
#     is_visible = False,
#     order_in_container = 2
#     )
# cicloagua1.save()
# cicloagua = LearningActivity( name = 'cicloAgua', slug = 'cicloAgua',
#     uri = "/activity/cicloagua",
# #   lom =
#     parent = cicloagua1, root  = agua,
#     post_condition_rule = "",
#
#     flow = True,
#     forward_only = False,
#     choice = False,
#
#     rollup_rule  = "",
#     rollup_objective = True,
#     rollup_progress = True,
#     is_container = False,
#     is_visible = False,
#     order_in_container = 1
#     )
# cicloagua.save()
# testcicloagua = LearningActivity( name = 'test', slug = 'test',
#     uri = "/test/testcicloagua",
# #   lom = ,
#     parent = cicloagua, root  = agua,
#
#     pre_condition_rule = """if self.num_attempts == 0 :
#  self.pre_condition = 'stopForwardTraversal'
# else:
#  self.pre_condition = 'hidden'""",
#     post_condition_rule = "" ,
#
#     rollup_rule  = "",
#     rollup_objective = True,
#     rollup_progress = True,
#     choice_exit = False,
#
#
#     is_container = False,
#     is_visible = False,
#     order_in_container = 2
#     )
# testcicloagua.save()
#
# cantidad1 = LearningActivity( name = 'cantidad', slug = 'cantidad',
#     uri = "/activity/cantidad1",
# #   lom =
#     parent = agua, root  = agua,
#     post_condition_rule = "",
#      pre_condition_rule = """if self.user.learningstyleinventory.age > 6 and self.user.learningstyleinventory.age < 18 :
# 	                  self.pre_condition = 'skip' """,
#     flow = True,
#     forward_only = False,
#     choice = False,
#
#     rollup_rule  = "",
#     rollup_objective = True,
#     rollup_progress = True,
#     is_container = True,
#     is_visible = False,
#     order_in_container = 3
#     )
# cantidad1.save()
# cantidad = LearningActivity( name = 'cantidad', slug = 'cantidad',
#     uri = "/activity/cantidad",
# #   lom =
#     parent = cantidad1, root  = agua,
#     post_condition_rule = "",
#
#     flow = True,
#     forward_only = False,
#     choice = False,
#
#     rollup_rule  = "",
#     rollup_objective = True,
#     rollup_progress = True,
#     is_container = False,
#     is_visible = False,
#     order_in_container = 1
#     )
# cantidad.save()
# testcantidad = LearningActivity( name = 'test', slug = 'test',
#     uri = "/test/testcantidad",
# #   lom = ,
#     parent = cantidad1, root  = agua,
#
#     pre_condition_rule = """if self.num_attempts == 0 :
#  self.pre_condition = 'stopForwardTraversal'
# else:
#  self.pre_condition = 'hidden'""",
#     post_condition_rule = "" ,
#
#     rollup_rule  = "",
#     rollup_objective = True,
#     rollup_progress = True,
#     choice_exit = False,
#
#
#     is_container = False,
#     is_visible = False,
#     order_in_container = 2
#     )
# testcantidad.save()

porciento1 = LearningActivity( name = 'porciento', slug = 'porciento',
    uri = "/activity/porciento1",
#   lom =
    parent = agua, root  = agua,
    post_condition_rule = "",
    pre_condition_rule = """if self.user.learningstyleinventory.age > 17:
 	                  self.pre_condition = 'skip' """,
    flow = True,
    forward_only = False,
    choice = False,

    rollup_rule  = "",
    rollup_objective = True,
    rollup_progress = True,
    is_container = True,
    is_visible = False,
    order_in_container = 2
    )
porciento1.save()
porciento = LearningActivity( name = 'porciento', slug = 'porciento',
    uri = "/activity/porciento",
#   lom =
    parent = porciento1, root  = agua,
    post_condition_rule = "",

    flow = True,
    forward_only = False,
    choice = False,

    rollup_rule  = "",
    rollup_objective = True,
    rollup_progress = True,
    is_container = False,
    is_visible = False,
    order_in_container = 1
    )
porciento.save()
testporciento = LearningActivity( name = 'test', slug = 'test',
    uri = "/test/testporciento",
#   lom = ,
    parent = porciento1, root  = agua,

    pre_condition_rule = """if self.num_attempts == 0 :
 self.pre_condition = 'stopForwardTraversal'
else:
 self.pre_condition = 'hidden'""",
    post_condition_rule = "" ,

    rollup_rule  = "",
    rollup_objective = True,
    rollup_progress = True,
    choice_exit = False,


    is_container = False,
    is_visible = False,
    order_in_container = 2
    )
testporciento.save()

energia1 = LearningActivity( name = 'energia', slug = 'energia',
    uri = "/activity/energia1",
#   lom =
    parent = agua, root  = agua,
    post_condition_rule = "",
    pre_condition_rule = """if self.user.learningstyleinventory.age < 18 :
 	                  self.pre_condition = 'skip' """,
    flow = True,
    forward_only = False,
    choice = False,

    rollup_rule  = "",
    rollup_objective = True,
    rollup_progress = True,
    is_container = True,
    is_visible = False,
    order_in_container = 3
    )
energia1.save()
energia = LearningActivity( name = 'energia', slug = 'energia',
    uri = "/activity/energia",
#   lom =
    parent = energia1, root  = agua,
    post_condition_rule = "",

    flow = True,
    forward_only = False,
    choice = False,

    rollup_rule  = "",
    rollup_objective = True,
    rollup_progress = True,
    is_container = False,
    is_visible = False,
    order_in_container = 1
    )
energia.save()
testenergia = LearningActivity( name = 'test', slug = 'test',
    uri = "/test/testenergia",
#   lom = ,
    parent = energia1, root  = agua,

    pre_condition_rule = """if self.num_attempts == 0 :
 self.pre_condition = 'stopForwardTraversal'
else:
 self.pre_condition = 'hidden'""",
    post_condition_rule = "" ,

    rollup_rule  = "",
    rollup_objective = True,
    rollup_progress = True,
    choice_exit = False,


    is_container = False,
    is_visible = False,
    order_in_container = 2
    )
testenergia.save()

salud1 = LearningActivity( name = 'salud', slug = 'salud',
    uri = "/activity/salud1",
#   lom =
    parent = agua, root  = agua,
    post_condition_rule = "",
    pre_condition_rule = """if self.user.learningstyleinventory.age < 18 :
 	                  self.pre_condition = 'skip' """,
    flow = True,
    forward_only = False,
    choice = False,

    rollup_rule  = "",
    rollup_objective = True,
    rollup_progress = True,
    is_container = True,
    is_visible = False,
    order_in_container = 4
    )
salud1.save()
salud = LearningActivity( name = 'salud', slug = 'salud',
    uri = "/activity/salud",
#   lom =
    parent = salud1, root  = agua,
    post_condition_rule = "",

    flow = True,
    forward_only = False,
    choice = False,

    rollup_rule  = "",
    rollup_objective = True,
    rollup_progress = True,
    is_container = False,
    is_visible = False,
    order_in_container = 1
    )
salud.save()
testsalud = LearningActivity( name = 'test', slug = 'test',
    uri = "/test/testsalud",
#   lom = ,
    parent = salud1, root  = agua,

    pre_condition_rule = """if self.num_attempts == 0 :
 self.pre_condition = 'stopForwardTraversal'
else:
 self.pre_condition = 'hidden'""",
    post_condition_rule = "" ,

    rollup_rule  = "",
    rollup_objective = True,
    rollup_progress = True,
    choice_exit = False,


    is_container = False,
    is_visible = False,
    order_in_container = 2
    )
testsalud.save()

materia1 = LearningActivity( name = 'materia', slug = 'materia',
    uri = "/activity/materia1",
#   lom =
    parent = agua, root  = agua,
    post_condition_rule = "",
    pre_condition_rule = """if self.user.learningstyleinventory.age > 17 :
 	                  self.pre_condition = 'skip' """,
    flow = True,
    forward_only = False,
    choice = False,

    rollup_rule  = "",
    rollup_objective = True,
    rollup_progress = True,
    is_container = True,
    is_visible = False,
    order_in_container = 5
    )
materia1.save()
materia = LearningActivity( name = 'materia', slug = 'materia',
    uri = "/activity/materia",
#   lom =
    parent = materia1, root  = agua,
    post_condition_rule = "",
#dfsdfdsfsd
    flow = True,
    forward_only = False,
    choice = False,

    rollup_rule  = "",
    rollup_objective = True,
    rollup_progress = True,
    is_container = False,
    is_visible = False,
    order_in_container = 1
    )
materia.save()
testmateria = LearningActivity( name = 'test', slug = 'test',
    uri = "/test/testmateria",
#   lom = ,
    parent = materia1, root  = agua,

    pre_condition_rule = """if self.num_attempts == 0 :
 self.pre_condition = 'stopForwardTraversal'
else:
 self.pre_condition = 'hidden'""",
    post_condition_rule = "" ,

    rollup_rule  = "",
    rollup_objective = True,
    rollup_progress = True,
    choice_exit = False,


    is_container = False,
    is_visible = False,
    order_in_container = 2
    )
testmateria.save()





##
##
##
## Example of two Users
##
##

User.objects.filter(username='ana').delete()
User.objects.filter(username='paul').delete()

j = User.objects.create_user('ana', 'lennon@thebeatles.com', '1234')
j.is_active = True
j.save()

p = User.objects.create_user('paul', 'paul@thebeatles.com', '1234')
p.is_active = True
p.save()

lsj=LearningStyleInventory(visual=12,verbal=11,aural=15,physical=9,logical=11,
                          social=9, solitary=10, age=5, aca_lvl=3, user = j)
lsj.save()

lsp=LearningStyleInventory(visual=12,verbal=11,aural=20,physical=9,logical=11,
                          social=9, solitary=7, age=15, aca_lvl=15, user = p)
lsp.save()

s = SimpleSequencing()

s = SimpleSequencing()
s.assignActivityTree(j,agua)
s.assignActivityTree(p,agua)


estudiantes = [
('edgar',          '1234',17,13,16,12,14,16,9, 25, 21),
('osuna',       '1234',15,12,14,18,14,19,8, 18, 4),
('malu',         '1234', 7,10, 4, 8,17,14,16, 18, 4),
('jose',        '1234',17, 6,16,13,14,11, 8, 18, 4),
('david',         '1234',15,10,13,14,17,15,11, 18, 4),
('juan',    '1234',11,13,11,10,13,18, 8, 18, 4),
('cota',              '1234',13, 7,18,14,12,10,13, 18, 4),
('omar',            '1234', 7, 3, 7,12,16,17, 6, 18, 4),
('santana',           '1234',10, 9,13,13,13,14,13, 18, 4),
('hector',  '1234', 1,11,11,11,18,13,13, 18, 4),
('edie',           '1234',14, 6,16,12,12,13,12, 18, 4),
('baby',      '1234',15,18,20,17,13,18,17, 18, 4),
('saul',            '1234',13,11,14,11,14,14,13, 18, 4),
('brenda',             '1234',17,13,20,12,14,11,16, 18, 4),
('samara',         '1234',14,15,13,12,15,16,12, 18, 4),
('daniel',      '1234', 9, 8,15,11,13,14,13, 18, 4),
('jorge',           '1234',17,12,14,17,19,18,14, 18, 4),
('mike',             '1234',15,16,17,18,18,13,11, 18, 4),
('luis',            '1234',11, 7,11,10,11,12, 6, 18, 4),
('anguiano.ae22@hotmail.com',       '1234',12,10,12,13,10,18,10, 18, 4),
('christian',       '1234',12,10,12,13,10,18,10, 18, 4),
('juancarlos',       '1234',12,10,12,13,10,18,10, 18, 4),
('diego',       '1234',12,10,12,13,10,18,10, 6, 2),
('xochilt',       '1234',12,10,12,13,10,18,10, 18, 4),
('cinthya',       '1234',12,10,12,13,10,18,10, 18, 4),
('claudia',       '1234',12,10,12,13,10,18,10, 25, 18),
('mario',       '1234',12,10,12,13,10,18,10, 25, 18),]

for e in estudiantes:
    User.objects.filter(username=e[0]).delete()
    u = User.objects.create_user(e[0],e[0], e[1])

    u.is_active = True
    u.save()
    lsu=LearningStyleInventory(visual=e[2],verbal=e[3],aural=e[4],physical=e[5],logical=e[6],
                          social=e[7], solitary=e[8], age=e[9], aca_lvl=e[10], user = u)

    lsu.save()
    ss = SimpleSequencing()
    ss.assignActivityTree(u,agua)


import os
#proot = UserLearningActivity.objects.filter(learning_activity = requested_activity.learning_activity.get_root() ,user = request.user )[0]
proot = LearningStyleInventory.objects.filter(user = User.objects.filter(username='edgar'))[0]
#.objects.filter(learning_activity = requested_activity.learning_activity.get_root() ,user = request.user )[0]


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "protoboard.settings")

##
##
## Assign Activity to both Users
##
##

#
# poo =UserLearningActivity.objects.filter(learning_activity__uri = "/activity/POO" ,user = User.objects.filter(username='paul')[0] )[0]
# ss = SimpleSequencing()


#
#
#a = ss.get_nav(poo)
#print ss.nav_to_xml(root=a)
#
#
#pre_j = UserLearningActivity.objects.filter(learning_activity__name = "Pretest" ,user = j )[0]
#s.set_current(pre_j)
#
#a = s.get_nav(root)
#print s.nav_to_xml(root=a)
#
#s.exit(pre_j, objective_measure = 0.20, objective_status = 'satisfied')
#
#a = s.get_nav(root)
#print s.nav_to_xml(root=a)

#
#s.set_current(j,remediation)
#s.exit(j,remediation, objective_measure = 0.80, objective_status = 'satisfied')
#a = s.get_nav(root)
#print s.nav_to_xml(root=a)
#
#
#s.set_current(j,general)
#s.exit(j,general, objective_measure = 0.80, objective_status = 'satisfied')
#a = s.get_nav(root)
#print s.nav_to_xml(root=a)


#root = UserLearningActivity.objects.filter(learning_activity__name = "Unit" ,user = j )[0]
#c = s.get_nav(root)
#print "-"*20
#print s.xml_children(root=c)
#
#s.set_current(j,general)
#s.exit(j, general, objective_measure = 0.80, objective_status = 'satisfied')
#root = UserLearningActivity.objects.filter(learning_activity__name = "Unit" ,user = j )[0]
#c = s.get_nav(root)
#print "-"*20
#print s.xml_children(root=c)
