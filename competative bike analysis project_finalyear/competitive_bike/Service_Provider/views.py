
from django.db.models import  Count, Avg
from django.shortcuts import render, redirect
from django.db.models import Count
import datetime

# Create your views here.
from Remote_User.models import appdetails_model,ClientRegister_Model,review_Model,share_Model


def serviceproviderlogin(request):
    if request.method  == "POST":
        admin = request.POST.get('username')
        password = request.POST.get('password')
        if admin == "SProvider" and password =="SProvider":
            return redirect('Upload_Apps')


    return render(request,'SProvider/serviceproviderlogin.html')

def Upload_Apps(request):
    

    result = ''
    pos = []
    neg = []
    oth = []
    se = 'se'
    if request.method == "POST":
        appname = request.POST.get('appname')
        mos = request.POST.get('mos')
        memoryr = request.POST.get('memoryr')
        spacen = request.POST.get('spacen')
        uses = request.POST.get('uses')
        cmd = request.POST.get('appdesc')

        datetime_object = datetime.datetime.now()

        if '#' in cmd:
            startingpoint = cmd.find('#')
            a = cmd[startingpoint:]
            endingPoint = a.find(' ')
            title = a[0:endingPoint]
            result = title[1:]
        # return redirect('')

        for f in cmd.split():
            if f in ('good', 'nice', 'beteer', 'best', 'excellent', 'extraordinary', 'happy', 'won', 'love', 'greate',):
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
            se = 'nutral'
            appdetails_model.objects.create(names=appname ,App_desc=cmd ,App_Uses=uses, Memory_Required=memoryr, Mobile_OS=mos,Space_Needed=spacen, sanalysis=se,
                                        DT=datetime_object,senderstatus='process')

    return render(request,'SProvider/Upload_Apps.html', {'result': result, 'se': se})



def viewtreandingquestions(request,chart_type):
    dd = {}
    pos,neu,neg =0,0,0
    poss=None
    topic = appdetails_model.objects.values('ratings').annotate(dcount=Count('ratings')).order_by('-dcount')
    for t in topic:
        topics=t['ratings']
        pos_count=appdetails_model.objects.filter(topics=topics).values('names').annotate(topiccount=Count('ratings'))
        poss=pos_count
        for pp in pos_count:
            senti= pp['names']
            if senti == 'positive':
                pos= pp['topiccount']
            elif senti == 'negative':
                neg = pp['topiccount']
            elif senti == 'nutral':
                neu = pp['topiccount']
        dd[topics]=[pos,neg,neu]
    return render(request,'SProvider/viewtreandingquestions.html',{'object':topic,'dd':dd,'chart_type':chart_type})

def Positivereviews(request):

    rtype='Positive'
    #obj = review_Model.objects.all()

    obj = review_Model.objects.all().filter(sanalysis=rtype)

    return render(request,'SProvider/Positivereviews.html',{'list_objects': obj})

def Negativereviews(request):

    rtype='Negative'
    #obj = review_Model.objects.all()

    obj = review_Model.objects.all().filter(sanalysis=rtype)

    return render(request,'SProvider/Negativereviews.html',{'list_objects': obj})

def Neutralreviews(request):

    rtype='Neutral'
    #obj = review_Model.objects.all()

    obj = review_Model.objects.all().filter(sanalysis=rtype)

    return render(request,'SProvider/Neutralreviews.html',{'list_objects': obj})


def viewallclients(request):
    obj=ClientRegister_Model.objects.all()
    return render(request,'SProvider/viewallclients.html',{'objects':obj})

def ViewTrendings(request):
    topic = appdetails_model.objects.values('names').annotate(dcount=Count('names')).order_by('-dcount')
    return  render(request,'SProvider/ViewTrendings.html',{'objects':topic})

def negativechart(request,chart_type):
    dd = {}
    pos, neu, neg = 0, 0, 0
    poss = None
    topic = appdetails_model.objects.values('ratings').annotate(dcount=Count('ratings')).order_by('-dcount')
    for t in topic:
        topics = t['ratings']
        pos_count = appdetails_model.objects.filter(topics=topics).values('names').annotate(topiccount=Count('ratings'))
        poss = pos_count
        for pp in pos_count:
            senti = pp['names']
            if senti == 'positive':
                pos = pp['topiccount']
            elif senti == 'negative':
                neg = pp['topiccount']
            elif senti == 'nutral':
                neu = pp['topiccount']
        dd[topics] = [pos, neg, neu]
    return render(request,'SProvider/negativechart.html',{'object':topic,'dd':dd,'chart_type':chart_type})


def charts(request,chart_type):
    chart1 = appdetails_model.objects.values('names').annotate(dcount=Avg('ratings'))
    return render(request,"SProvider/charts.html", {'form':chart1, 'chart_type':chart_type})

def dislikeschart(request,dislike_chart):
    charts = appdetails_model.objects.values('names').annotate(dcount=Avg('dislikes'))
    return render(request,"SProvider/dislikeschart.html", {'form':charts, 'dislike_chart':dislike_chart})

def likeschart(request,like_chart):
    charts = appdetails_model.objects.values('names').annotate(dcount=Avg('likes'))
    return render(request,"SProvider/likeschart.html", {'form':charts, 'like_chart':like_chart})





def View_AllApps_Details(request):
    obj = appdetails_model.objects.all()
    return render(request, 'SProvider/View_AllApps_Details.html', {'list_objects': obj})

def viewallpostsreviews(request):

        obj = review_Model.objects.all()

        return render(request, 'SProvider/Viewallpostsreviews.html', {'list_objects': obj})


def viewallappshared(request):
    obj = share_Model.objects.all()

    return render(request, 'SProvider/viewallappshared.html', {'list_objects': obj})





