__author__ = 'frank'
import sqlite3

conn = sqlite3.connect('kinect.db')
#uss = ["u0","u1","u2","u3","u4","u5","u6","u7","u8","u9"]
c=conn.cursor()
#lista = [[0] * 28 for i in range(10)]
for  row in c.execute("""SELECT user,engage,activity, COUNT(*)
             FROM kinect
             GROUP BY user,engage,activity
             ORDER BY user,engage,activity"""):
    print row






# for x in range(10):
#     t=(uss[x],)
#     c.execute("SELECT COUNT(*) FROM kinect WHERE user = ? and engage = 'Yes' and activity = '/activity/videojuego'", t)
#     aa11=c.fetchone()
#     lista[x][0]=aa11[0]
#     c.execute("SELECT COUNT(*) FROM kinect WHERE user = ? and engage = 'Maybe' and activity = '/activity/videojuego'", t)
#     bb11=c.fetchone()
#     lista[x][1]=bb11[0]
#     c.execute("SELECT COUNT(*) FROM kinect WHERE user = ? and engage = 'No' and activity = '/activity/videojuego'", t)
#     cc11=c.fetchone()
#     lista[x][2]=cc11[0]
#     c.execute("SELECT COUNT(*) FROM kinect WHERE user = ? and engage = 'Unknown' and activity = '/activity/videojuego'", t)
#     dd11=c.fetchone()
#     lista[x][3]=dd11[0]
#     c.execute("SELECT COUNT(*) FROM kinect WHERE user = ? and happy = 'Yes' and activity = '/activity/videojuego'", t)
#     aa12=c.fetchone()
#     lista[x][4]=aa12[0]
#     c.execute("SELECT COUNT(*) FROM kinect WHERE user = ? and happy = 'Maybe' and activity = '/activity/videojuego'", t)
#     bb12=c.fetchone()
#     lista[x][5]=bb12[0]
#     c.execute("SELECT COUNT(*) FROM kinect WHERE user = ? and happy = 'No' and activity = '/activity/videojuego'", t)
#     cc12=c.fetchone()
#     lista[x][6]=cc12[0]
#     c.execute("SELECT COUNT(*) FROM kinect WHERE user = ? and happy = 'Unknown' and activity = '/activity/videojuego'", t)
#     dd12=c.fetchone()
#     lista[x][7]=dd12[0]
#     c.execute("SELECT COUNT(*) FROM kinect WHERE user = ? and lookingaway = 'Yes' and activity = '/activity/videojuego'", t)
#     aa13=c.fetchone()
#     lista[x][8]=aa13[0]
#     c.execute("SELECT COUNT(*) FROM kinect WHERE user = ? and lookingaway = 'Maybe' and activity = '/activity/videojuego'", t)
#     bb13=c.fetchone()
#     lista[x][9]=bb13[0]
#     c.execute("SELECT COUNT(*) FROM kinect WHERE user = ? and lookingaway = 'No' and activity = '/activity/videojuego'", t)
#     cc13=c.fetchone()
#     lista[x][10]=cc13[0]
#     c.execute("SELECT COUNT(*) FROM kinect WHERE user = ? and lookingaway = 'Unknown' and activity = '/activity/videojuego'", t)
#     dd13=c.fetchone()
#     lista[x][11]=dd13[0]
#     c.execute("SELECT COUNT(*) FROM kinect WHERE user = ? and engage = 'Yes' and activity = '/activity/cine'", t)
#     aa21=c.fetchone()
#     lista[x][12]=aa21[0]
#     c.execute("SELECT COUNT(*) FROM kinect WHERE user = ? and engage = 'Maybe' and activity = '/activity/cine'", t)
#     bb21=c.fetchone()
#     lista[x][13]=bb21[0]
#     c.execute("SELECT COUNT(*) FROM kinect WHERE user = ? and engage = 'No' and activity = '/activity/cine'", t)
#     cc21=c.fetchone()
#     lista[x][14]=cc21[0]
#     c.execute("SELECT COUNT(*) FROM kinect WHERE user = ? and engage = 'Unknown' and activity = '/activity/cine'", t)
#     dd21=c.fetchone()
#     lista[x][15]=dd21[0]
#     c.execute("SELECT COUNT(*) FROM kinect WHERE user = ? and happy = 'Yes' and activity = '/activity/cine'", t)
#     aa22=c.fetchone()
#     lista[x][16]=aa22[0]
#     c.execute("SELECT COUNT(*) FROM kinect WHERE user = ? and happy = 'Maybe' and activity = '/activity/cine'", t)
#     bb22=c.fetchone()
#     lista[x][17]=bb22[0]
#     c.execute("SELECT COUNT(*) FROM kinect WHERE user = ? and happy = 'No' and activity = '/activity/cine'", t)
#     cc22=c.fetchone()
#     lista[x][18]=cc22[0]
#     c.execute("SELECT COUNT(*) FROM kinect WHERE user = ? and happy = 'Unknown' and activity = '/activity/cine'", t)
#     dd22=c.fetchone()
#     lista[x][19]=dd22[0]
#     c.execute("SELECT COUNT(*) FROM kinect WHERE user = ? and lookingaway = 'Yes' and activity = '/activity/cine'", t)
#     aa23=c.fetchone()
#     lista[x][20]=aa23[0]
#     c.execute("SELECT COUNT(*) FROM kinect WHERE user = ? and lookingaway = 'Maybe' and activity = '/activity/cine'", t)
#     bb23=c.fetchone()
#     lista[x][21]=bb23[0]
#     c.execute("SELECT COUNT(*) FROM kinect WHERE user = ? and lookingaway = 'No' and activity = '/activity/cine'", t)
#     cc23=c.fetchone()
#     lista[x][22]=cc23[0]
#     c.execute("SELECT COUNT(*) FROM kinect WHERE user = ? and lookingaway = 'Unknown' and activity = '/activity/cine'", t)
#     dd23=c.fetchone()
#     lista[x][23]=dd23[0]
#     c.execute("SELECT COUNT(*) FROM kinect WHERE user = ? and activity = '/activity/videojuego'", t)
#     cvideo=c.fetchone()
#     lista[x][24]=cvideo[0]
#     c.execute("SELECT COUNT(*) FROM kinect WHERE user = ? and activity = '/activity/cine'", t)
#     ccine=c.fetchone()
#     lista[x][25]=ccine[0]
#     c.execute("SELECT COUNT(*) FROM kinect WHERE user = ? ", t)
#     ccine=c.fetchone()
#     lista[x][26]=ccine[0]
#     lista[x][27]=uss[x]
#
# for x in range(28):
#     for y in range (10):
#         print lista [y][x]
#     print "next--------