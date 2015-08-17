# __author__ = 'frank'
# import numpy as np
#
#
# def svar(X):
#     n = float(len(X))
#     svar=(sum([(x-np.mean(X))**2 for x in X]) / n)* n/(n-1.)
#     return svar
#
#
# def CronbachAlpha(itemscores):
#     itemvars = [svar(item) for item in itemscores]
#     tscores = [0] * len(itemscores[0])
#     for item in itemscores:
#        for i in range(len(item)):
#           tscores[i]+= item[i]
#     nitems = len(itemscores)
#     #print "total scores=", tscores, 'number of items=', nitems
#
#     Calpha=nitems/(nitems-1.) * (1-sum(itemvars)/ svar(tscores))
#
#     return Calpha
#
# ###########Test################
# itemscores1 = [[2,5,5,4,5,5,4,5,5,5],
#                 [4,5,4,5,5,5,5,5,4,5],
#                 [5,5,5,5,4,5,4,4,5,5],
#                 [3,5,5,3,5,4,4,5,5,5]]
# itemscores =  [[5,5,4,5,5,5,4,5,5,4,4],
#                # [5,5,4,4,4,5,5,4,5,3,5],
#                # [3,5,4,5,5,4,3,5,5,5,5],
#                # [2,4,5,3,4,5,5,5,5,4,5],
#                 [5,4,5,5,3,5,5,5,5,4,3],
#                 [5,5,5,5,5,5,3,5,5,4,5],
#                 [5,5,4,5,4,5,4,5,4,3,5],
#                [5,5,4,5,5,5,5,5,5,3,5]]
# itemscores3 = [[ 4,14,3,3],
#               [ 5,14,4,3]]
#
# print "Cronbach alpha = ", CronbachAlpha(itemscores)
import sqlite3

conn = sqlite3.connect('kinect.db')
uss = ["a21","a22","a23","a24","a25","a26","a27","a28","a29","a30","a31","a32","a33","a34","a35","a36","a37","a38","a39","a40"]
c=conn.cursor()
lista = [[0] * 36 for i in range(20)]

for x in range(20):
    t=(uss[x],)
    c.execute("SELECT COUNT(*) FROM kinect WHERE user = ? and engage = 'Yes' and activity = '/activity/videojuego'", t)
    aa11=c.fetchone()
    lista[x][0]=aa11[0]
    c.execute("SELECT COUNT(*) FROM kinect WHERE user = ? and engage = 'Maybe' and activity = '/activity/videojuego'", t)
    bb11=c.fetchone()
    lista[x][1]=bb11[0]
    c.execute("SELECT COUNT(*) FROM kinect WHERE user = ? and engage = 'No' and activity = '/activity/videojuego'", t)
    cc11=c.fetchone()
    lista[x][2]=cc11[0]
    c.execute("SELECT COUNT(*) FROM kinect WHERE user = ? and engage = 'Unknown' and activity = '/activity/videojuego'", t)
    dd11=c.fetchone()
    lista[x][3]=dd11[0]
    c.execute("SELECT COUNT(*) FROM kinect WHERE user = ? and happy = 'Yes' and activity = '/activity/videojuego'", t)
    aa12=c.fetchone()
    lista[x][4]=aa12[0]
    c.execute("SELECT COUNT(*) FROM kinect WHERE user = ? and happy = 'Maybe' and activity = '/activity/videojuego'", t)
    bb12=c.fetchone()
    lista[x][5]=bb12[0]
    c.execute("SELECT COUNT(*) FROM kinect WHERE user = ? and happy = 'No' and activity = '/activity/videojuego'", t)
    cc12=c.fetchone()
    lista[x][6]=cc12[0]
    c.execute("SELECT COUNT(*) FROM kinect WHERE user = ? and happy = 'Unknown' and activity = '/activity/videojuego'", t)
    dd12=c.fetchone()
    lista[x][7]=dd12[0]
    c.execute("SELECT COUNT(*) FROM kinect WHERE user = ? and lookingaway = 'Yes' and activity = '/activity/videojuego'", t)
    aa13=c.fetchone()
    lista[x][8]=aa13[0]
    c.execute("SELECT COUNT(*) FROM kinect WHERE user = ? and lookingaway = 'Maybe' and activity = '/activity/videojuego'", t)
    bb13=c.fetchone()
    lista[x][9]=bb13[0]
    c.execute("SELECT COUNT(*) FROM kinect WHERE user = ? and lookingaway = 'No' and activity = '/activity/videojuego'", t)
    cc13=c.fetchone()
    lista[x][10]=cc13[0]
    c.execute("SELECT COUNT(*) FROM kinect WHERE user = ? and lookingaway = 'Unknown' and activity = '/activity/videojuego'", t)
    dd13=c.fetchone()
    lista[x][11]=dd13[0]
    c.execute("SELECT COUNT(*) FROM kinect WHERE user = ? and engage = 'Yes' and activity = '/activity/cine'", t)
    aa21=c.fetchone()
    lista[x][12]=aa21[0]
    c.execute("SELECT COUNT(*) FROM kinect WHERE user = ? and engage = 'Maybe' and activity = '/activity/cine'", t)
    bb21=c.fetchone()
    lista[x][13]=bb21[0]
    c.execute("SELECT COUNT(*) FROM kinect WHERE user = ? and engage = 'No' and activity = '/activity/cine'", t)
    cc21=c.fetchone()
    lista[x][14]=cc21[0]
    c.execute("SELECT COUNT(*) FROM kinect WHERE user = ? and engage = 'Unknown' and activity = '/activity/cine'", t)
    dd21=c.fetchone()
    lista[x][15]=dd21[0]
    c.execute("SELECT COUNT(*) FROM kinect WHERE user = ? and happy = 'Yes' and activity = '/activity/cine'", t)
    aa22=c.fetchone()
    lista[x][16]=aa22[0]
    c.execute("SELECT COUNT(*) FROM kinect WHERE user = ? and happy = 'Maybe' and activity = '/activity/cine'", t)
    bb22=c.fetchone()
    lista[x][17]=bb22[0]
    c.execute("SELECT COUNT(*) FROM kinect WHERE user = ? and happy = 'No' and activity = '/activity/cine'", t)
    cc22=c.fetchone()
    lista[x][18]=cc22[0]
    c.execute("SELECT COUNT(*) FROM kinect WHERE user = ? and happy = 'Unknown' and activity = '/activity/cine'", t)
    dd22=c.fetchone()
    lista[x][19]=dd22[0]
    c.execute("SELECT COUNT(*) FROM kinect WHERE user = ? and lookingaway = 'Yes' and activity = '/activity/cine'", t)
    aa23=c.fetchone()
    lista[x][20]=aa23[0]
    c.execute("SELECT COUNT(*) FROM kinect WHERE user = ? and lookingaway = 'Maybe' and activity = '/activity/cine'", t)
    bb23=c.fetchone()
    lista[x][21]=bb23[0]
    c.execute("SELECT COUNT(*) FROM kinect WHERE user = ? and lookingaway = 'No' and activity = '/activity/cine'", t)
    cc23=c.fetchone()
    lista[x][22]=cc23[0]
    c.execute("SELECT COUNT(*) FROM kinect WHERE user = ? and lookingaway = 'Unknown' and activity = '/activity/cine'", t)
    dd23=c.fetchone()
    lista[x][23]=dd23[0]
    c.execute("SELECT COUNT(*) FROM kinect WHERE user = ? and boca = 'Yes' and activity = '/activity/cine'", t)
    aa24=c.fetchone()
    lista[x][24]=aa24[0]
    c.execute("SELECT COUNT(*) FROM kinect WHERE user = ? and boca = 'Maybe' and activity = '/activity/cine'", t)
    bb24=c.fetchone()
    lista[x][25]=bb24[0]
    c.execute("SELECT COUNT(*) FROM kinect WHERE user = ? and boca = 'No' and activity = '/activity/cine'", t)
    cc24=c.fetchone()
    lista[x][26]=cc24[0]
    c.execute("SELECT COUNT(*) FROM kinect WHERE user = ? and boca = 'Unknown' and activity = '/activity/cine'", t)
    dd24=c.fetchone()
    lista[x][27]=dd24[0]
    c.execute("SELECT COUNT(*) FROM kinect WHERE user = ? and boca = 'Yes' and activity = '/activity/videojuego'", t)
    aa25=c.fetchone()
    lista[x][28]=aa25[0]
    c.execute("SELECT COUNT(*) FROM kinect WHERE user = ? and boca = 'Maybe' and activity = '/activity/videojuego'", t)
    bb25=c.fetchone()
    lista[x][29]=bb25[0]
    c.execute("SELECT COUNT(*) FROM kinect WHERE user = ? and boca = 'No' and activity = '/activity/videojuego'", t)
    cc25=c.fetchone()
    lista[x][30]=cc25[0]
    c.execute("SELECT COUNT(*) FROM kinect WHERE user = ? and boca = 'Unknown' and activity = '/activity/videojuego'", t)
    dd25=c.fetchone()
    lista[x][31]=dd25[0]
    c.execute("SELECT COUNT(*) FROM kinect WHERE user = ? and activity = '/activity/videojuego'", t)
    cvideo=c.fetchone()
    lista[x][32]=cvideo[0]
    c.execute("SELECT COUNT(*) FROM kinect WHERE user = ? and activity = '/activity/cine'", t)
    ccine=c.fetchone()
    lista[x][33]=ccine[0]
    c.execute("SELECT COUNT(*) FROM kinect WHERE user = ? ", t)
    ccine=c.fetchone()
    lista[x][34]=ccine[0]
    lista[x][35]=uss[x]

#for x in range(36):
#    for y in range (21):
for r in range (20):
    print lista[r]
#    print "next----------------------------------------"