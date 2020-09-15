from django.shortcuts import render
from .models import dbb
import random

# Create your views here.
def si(request):
    return render(request, 'index.html')
def sav(request):
    k = 0
    dict = {'bug': k}
    return render(request, 'loginpage.html', dict)
def imp(request):
    if request.method == 'POST':
        if (dbb.objects.filter(p=request.POST['passcode']).exists() and dbb.objects.filter(em=request.POST['emailaddress']).exists()):
            print("authenticated ssssssssssssssssssssssssssssssssss")
            if (dbb.objects.get(em = request.POST['emailaddress']).food != ''):
                print("authenticated11111 ssssssssssssssssssssssssssssssssss")
                dbbb2 = dbb.objects.all()
                dbbb3 = dbb.objects.get(em = request.POST['emailaddress'])
                l = []
                l1 = []
                s = [] #for sorting
                ss = [] #for sorting
                k=0
                b=0
                for i in dbbb2:
                    print("authenticated22222 ssssssssssssssssssssssssssssssssss", i)
                    if dbbb3.em != i.em:
                        c = 0
                        print("authenticated2.5 sssssssssssssssssss", dbbb3.em, c)
                        if ((dbbb3.place).lower()).replace(" ","") == ((i.place).lower()).replace(" ",""):
                            c = c+1
                            print(c, "cccccccccc111")
                        if ((dbbb3.game).lower()).replace(" ","") == ((i.game).lower()).replace(" ",""):
                            c = c+1
                            print(c, "cccccccccc222")
                        if ((dbbb3.food).lower()).replace(" ","") == ((i.food).lower()).replace(" ",""):
                            c = c+1
                            print(c, "cccccccccc333")
                        if ((dbbb3.movie).lower()).replace(" ","") == ((i.movie).lower()).replace(" ",""):
                            c = c+1
                            print(c, "cccccccccc444")
                        if ((dbbb3.actor).lower()).replace(" ","") == ((i.actor).lower()).replace(" ",""):
                            c = c+1
                            print(c, "cccccccccc555")
                        if ((dbbb3.song).lower()).replace(" ","") == ((i.song).lower()).replace(" ",""):
                            c = c+1
                            print(c, "cccccccccc666")
                        if ((dbbb3.sports).lower()).replace(" ","") == ((i.sports).lower()).replace(" ",""):
                            c = c+1
                            print(c, "cccccccccc777")
                        if ((dbbb3.sportsman).lower()).replace(" ","") == ((i.sportsman).lower()).replace(" ",""):
                            c = c+1
                            print(c, "cccccccccc888")
                        if ((dbbb3.person).lower()).replace(" ","") == ((i.person).lower()).replace(" ",""):
                            c = c+1
                            print(c, "cccccccccc999")
                        if ((dbbb3.enter).lower()).replace(" ","") == ((i.enter).lower()).replace(" ",""):
                            c = c+1
                            print(c, "cccccccccc101010")
                        if c > 0:
                            k = 1
                            r = "#{:06x}".format(random.randint(0, 0xFFFFFF))
                            print("authenticated333 ssssssssssssssssss", c)
                            cc = c * 10, i, i.place, i.game, i.food, i.movie, i.actor, i.song, i.sports, i.sportsman, i.person, i.enter, i.contact, i.about, i.n, r
                            l.append(cc)
                print(k, "kkkkkkkkkkkkkkkkkkkkkkS")
                cc = dbbb3, dbbb3.n, dbbb3.place, dbbb3.game, dbbb3.food, dbbb3.movie, dbbb3.actor, dbbb3.song, dbbb3.sports, dbbb3.sportsman, dbbb3.person, dbbb3.enter, dbbb3.contact, dbbb3.about
                l1.append(cc)
                if k == 0:
                    l2 = { 'edit': l1 , 'list':None}
                    return render(request, 'main.html', l2)
                for i in l:
                    s.append(i[0])
                s.sort(reverse=True)
                for i in s:
                    x = 0
                    for j in l:
                        if i == j[0]:

                            if k != 32:
                                k = k+1
                                if b == 1:
                                    for z in ss:
                                        if z == j:
                                            x = 1
                                if x == 0:
                                    b = 1
                                    ss.append(j)
                ll = { 'edit': l1, 'list': ss}
                print('lllllllllllllllllll', ll)
                return render(request, 'main.html', ll)
            else:
                temp = {'dict': request.POST['emailaddress']}
                return render(request, 'mainfile.html', temp)
        else:
            invalid = {'invalid':0}
            return render(request, 'loginpage.html',invalid)
def file(request):
    if request.method=='POST':
        dbbb = dbb()
        dbbb.n = request.POST['username']
        dbbb.em = request.POST['emailaddress']
        dbbb.p = request.POST['passcode']
        dbbb.save()
        temp = {'dict': request.POST['emailaddress']}
        return render(request, 'mainfile.html', temp)
def score(request,temp):
    if request.method == 'POST':
        dbbb2 = dbb(em = temp)
        print("ppppppppppppp111",dbbb2)
        dbbb2.n = dbb.objects.get(em=temp).n
        dbbb2.p = dbb.objects.get(em=temp).p
        dbbb2.place = request.POST['place']
        print("pppppppppppp222",request.POST['place'])
        dbbb2.game = request.POST['game']
        dbbb2.food = request.POST['food']
        dbbb2.movie = request.POST['movie']
        dbbb2.actor = request.POST['actor']
        dbbb2.song = request.POST['song']
        dbbb2.sports = request.POST['sports']
        dbbb2.sportsman = request.POST['sportsman']
        dbbb2.person = request.POST['person']
        dbbb2.enter = request.POST['entertainment']
        dbbb2.contact = request.POST['contact']
        dbbb2.about = request.POST['aboutu']
        dbbb2.save()
        k = 1
        dict = {'bug': k}
        print("ppppppppppppp333",dbbb2)
        print("ssssssssssssssssssssmmmmmmmmmmmmaaaaaaaaaassssssshhh")
        return render(request, 'loginpage.html', dict)
def edit(request,temp):
    t = temp.split()
    t1 = t[1]
    t2 = t1[:-2]
    lst = []
    l = dbb.objects.get(em=t2), dbb.objects.get(em=t2).n, dbb.objects.get(em=t2).place, dbb.objects.get(em=t2).game, dbb.objects.get(em=t2).food, dbb.objects.get(em=t2).movie, dbb.objects.get(em=t2).actor, dbb.objects.get(em=t2).song, dbb.objects.get(em=t2).sports, dbb.objects.get(em=t2).sportsman, dbb.objects.get(em=t2).person, dbb.objects.get(em=t2).enter, dbb.objects.get(em=t2).contact, dbb.objects.get(em=t2).about
    l1 = dbb.objects.get(em=t2).em
    lst.append(l)
    dict = {'edit': lst, 'edit1': l1}
    return render(request, 'mainfileedit.html', dict)
def handler500(request):
    return render(request, '500.html', status=500)
