from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404
import datetime

# Create your views here.
from Remote_User.models import review_Model,ClientRegister_Model,appdetails_model,share_Model


def login(request):


    if request.method == "POST" and 'submit1' in request.POST:

        username = request.POST.get('username')
        password = request.POST.get('password')
        try:

            enter = ClientRegister_Model.objects.get(username=username, password=password)
            request.session["userid"] = enter.id
            return redirect('ViewAllAppDetails')
        except:
            pass

    return render(request,'RUser/login.html')



def Register1(request):

    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phoneno = request.POST.get('phoneno')
        country = request.POST.get('country')
        state = request.POST.get('state')
        city = request.POST.get('city')
        ClientRegister_Model.objects.create(username=username, email=email, password=password, phoneno=phoneno,
                                            country=country, state=state, city=city)

        return render(request, 'RUser/Register1.html')
    else:

        return render(request,'RUser/Register1.html')


def ViewYourProfile(request):
    userid = request.session['userid']
    obj = ClientRegister_Model.objects.get(id= userid)
    return render(request,'RUser/ViewYourProfile.html',{'object':obj})

def Review(request,pk):
    userid = request.session['userid']
    userObj = ClientRegister_Model.objects.get(id=userid)
    username = userObj.username

    objs = appdetails_model.objects.get(id=pk)
    tname = objs.names

    datetime_object = datetime.datetime.now()

    result = ''
    pos = []
    neg = []
    oth = []
    se = 'se'
    if request.method == "POST":
        uname = request.POST.get('uname')
        tname1 = request.POST.get('tname')
        used = request.POST.get('used')
        cmd = request.POST.get('review')


        if '#' in cmd:
            startingpoint = cmd.find('#')
            a = cmd[startingpoint:]
            endingPoint = a.find(' ')
            title = a[0:endingPoint]
            result = title[1:]
        # return redirect('')

        for f in cmd.split():
            if f in ('good', 'nice', 'better', 'best', 'excellent', 'extraordinary', 'happy', 'won', 'love', 'greate',):
                pos.append(f)
            elif f in ('worst', 'waste', 'poor', 'error', 'imporve', 'bad', 'ridicules'):
                neg.append(f)
            else:
                oth.append(f)
        if len(pos) > len(neg):
            se = 'positive'
        elif len(neg) > len(pos):
            se = 'negative'
        else:
            se = 'neutral'
        review_Model.objects.create(uname=uname , ureview=cmd,sanalysis=se,dt=datetime_object,tname=tname1 ,suggestion=used)

    return render(request,'RUser/Review.html', {'objc':username,'objc1':tname,'result': result, 'se': se})

def Share(request,pk):
    userid = request.session['userid']
    userObj = ClientRegister_Model.objects.get(id=userid)
    username = userObj.username

    objs = appdetails_model.objects.get(id=pk)
    appname = objs.names

    if request.method == "POST":
        username1 = request.POST.get('uname')
        appname = request.POST.get('appname')
        loc = request.POST.get('loc')
        usefull = request.POST.get('usefull')

        datetime_object = datetime.datetime.now()

        share_Model.objects.create( usefull=usefull, uname1=username1,loc=loc, dt=datetime_object, appname=appname)

    return render(request,'RUser/Share.html', {'objc':username,'objc1':appname})


def ViewAllAppDetails(request):
    userid = request.session['userid']
    obj = appdetails_model.objects.all()

    return render(request,'RUser/ViewAllAppDetails.html',{'list_objects': obj})

def Viewreviews(request):

    obj = review_Model.objects.all()

    return render(request,'RUser/Viewreviews.html',{'list_objects': obj})




def ratings(request,pk):
    vott1, vott, neg = 0, 0, 0
    objs = appdetails_model.objects.get(id=pk)
    unid = objs.id
    vot_count = appdetails_model.objects.all().filter(id=unid)
    for t in vot_count:
        vott = t.ratings
        vott1 = vott + 1
        obj = get_object_or_404(appdetails_model, id=unid)
        obj.ratings = vott1
        obj.save(update_fields=["ratings"])
        return redirect('ViewAllAppDetails')

    return render(request,'RUser/ratings.html',{'objs':vott1})


def dislikes(request,pk):
    vott1, vott, neg = 0, 0, 0
    objs = appdetails_model.objects.get(id=pk)
    unid = objs.id
    vot_count = appdetails_model.objects.all().filter(id=unid)
    for t in vot_count:
        vott = t.dislikes
        vott1 = vott - 1
        obj = get_object_or_404(appdetails_model, id=unid)
        obj.dislikes = vott1
        obj.save(update_fields=["dislikes"])
        return redirect('ViewAllAppDetails')
    return render(request,'RUser/dislikes.html',{'objs':vott1})

def ViewTrending(request):
    topic = appdetails_model.objects.values('names').annotate(dcount=Count('names')).order_by('-dcount')
    return render(request, 'RUser/ViewTrending.html', {'objects': topic})

def viewallappshared_details(request):
    obj = share_Model.objects.all()

    return render(request, 'RUser/viewallappshared_details.html', {'list_objects': obj})

def likes(request,pk):
    vott1, vott, neg = 0, 0, 0
    objs = appdetails_model.objects.get(id=pk)
    unid = objs.id
    vot_count = appdetails_model.objects.all().filter(id=unid)
    for t in vot_count:
        vott = t.likes
        vott1 = vott + 1
        obj = get_object_or_404(appdetails_model, id=unid)
        obj.likes = vott1
        obj.save(update_fields=["likes"])
        return redirect('ViewAllAppDetails')

    return render(request,'RUser/likes.html',{'objs':vott1})

