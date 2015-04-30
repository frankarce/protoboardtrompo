if __name__ == "__main__":
    import os
    print "####### DJANGO SETTINGS"
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "protoboard.settings")
import time
import datetime
import redis
import psycopg2
from activitytree.interaction_handler import SimpleSequencing
from activitytree.models import LearningStyleInventory, LearningActivity, Course, UserLearningActivity, UserAffectiveData
import datetime
q=redis.Redis("localhost")
w=redis.Redis("localhost")
usuario="users" \
        "---" \
        "" \
        "" \
        "" \
        "" \
        "" \
        "" \
        "11"
actividad=q.get(usuario)
actividad2=actividad

happy=0
engage=0
away=0

while actividad!="/activity/POO":
    print "entre aqui"
    d=[]
    happy="No"
    engage="No"
    away="No"
    time.sleep(1) # delays for 1 seconds
    print actividad
    while actividad==actividad2:
        print "entre aca"
        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        actividad2=q.get(usuario)
        print actividad, actividad2
        time.sleep(1) # delays for 1 seconds
        a=w.get("01")

        b=a.split("\n")

        b.remove("")
        for x in range(len(b)):
            c=b[x]
            d.append(c.split(":"))

        happy=d[0][1]
        engage= d[1][1]
        away=d[7][1]
        #print "entre", actividad2, engage
        namedict={"user":usuario, "activity":actividad,"happy_count":happy, "engage_count":engage,"away_count":away}
        datos=UserAffectiveData(user=usuario,activity=actividad,engage_count=engage,happy_count=happy,away_count=away, time=int(round(time.time())),timestamp=st)
        datos.save()
        #print namedict
    actividad=q.get(usuario)

    #try:
    #executemany("""INSERT INTO activitytree_useraffectivedata(user,activity , engage_count, happy_count, away_count) VALUES (%(user)s, %(actiivity)s,%(engage_count)s,%(happy_count)s,%(away_count)s)""", namedict)
    #    datos=UserAffectiveData(user="ana",activity=actividad,engage_count=engage,happy_count=happy,away_count=away)
    #    datos.save()
    #except:
    #    print "I can't SAVE"#

#rows = cur.fetchall()
print "termine"
#for row in rows:
#    print "   ", row[4-

# #namedict={"user":"ana", "activity":actividad,"happy_count":happy, "engage_count":engage,"away_count":away}
#try:
#    conn = psycopg2.connect("dbname='protoboard' user='django' host='localhost' password='******'")
#except:
#    print "I am unable to connect to the database."
#    cur = conn.cursor()




####################################Contando los yes#################################################
#while actividad!="/test/test":
#    print "entre aqui"
#    d=[]
##    happy=0
#    engage=0
#    away=0
#    time.sleep(1) # delays for 1 seconds
#    print actividad, actividad2
 #   while actividad==actividad2:
 #       print "entre aca"
#        actividad2=q.get("ana")
#        print actividad2
#        time.sleep(1) # delays for 1 seconds
#        a=w.get("1")

#        b=a.split("\n")

#        b.remove("")

#        for x in range(len(b)):
#            c=b[x]
 #           d.append(c.split(":"))
#        if d[0][1]==" Yes":
#            print "conte1"
#            happy=happy+1
#        if d[1][1]==" Yes":
#            print "conte2"
#            engage=engage+1
#        if d[7][1]==" Yes":
#            print "conte3"
#            away=away+1

 #   print "entre", actividad2, engage
 #   namedict={"user":"ana", "activity":actividad,"happy_count":happy, "engage_count":engage,"away_count":away}
#    actividad=q.get("ana")
#    print namedict
#    try:
    #executemany("""INSERT INTO activitytree_useraffectivedata(user,activity , engage_count, happy_count, away_count) VALUES (%(user)s, %(actiivity)s,%(engage_count)s,%(happy_count)s,%(away_count)s)""", namedict)
#        datos=UserAffectiveData(user="ana",activity=actividad,engage_count=engage,happy_count=happy,away_count=away)
#        datos.save()
#    except:
 #       print "I can't SAVE"#

#rows = cur.fetchall()
#print "termine"
#for row in rows: