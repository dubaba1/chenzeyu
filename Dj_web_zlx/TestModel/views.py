# -*- coding: utf-8 -*-

from django.shortcuts import render
from TestModel.models import Test, emo_test, popular_type,price_amount ,shop1,shop2,shop3,shop4,shop5,shop6,shop7,shop8,shop9
from django.core import serializers
import json
def index(request):
    list = emo_test.objects.all()
    list1 = popular_type.objects.all()
    list2 =price_amount.objects.all()
    return render(request, 'index.html', {"data2": serializers.serialize('json', list2),"data1": serializers.serialize('json', list1),"data": list,"data3":list1,})
def sp1(request):
    s1=shop1.objects.all()
    return render(request, "shop1.html", {"shop1": serializers.serialize('json', s1),})
def sp2(request):
    s2=shop2.objects.all()
    return render(request, "shop2.html", {"shop2": serializers.serialize('json', s2),})
def sp3(request):
    s3=shop3.objects.all()
    return render(request, "shop3.html", {"shop3": serializers.serialize('json', s3),})
def sp4(request):
    s4=shop4.objects.all()
    return render(request, "shop4.html", {"shop4": serializers.serialize('json', s4),})
def sp5(request):
    s5=shop5.objects.all()
    return render(request, "shop5.html", {"shop5": serializers.serialize('json', s5),})
def sp6(request):
    s6=shop6.objects.all()
    return render(request, "shop6.html", {"shop6": serializers.serialize('json', s6),})
def sp7(request):
    s7=shop7.objects.all()
    return render(request, "shop7.html", {"shop7": serializers.serialize('json', s7),})
def sp8(request):
    s8=shop8.objects.all()
    return render(request, "shop8.html", {"shop8": serializers.serialize('json', s8),})
def sp9(request):
    s9=shop9.objects.all()
    return render(request, "shop9.html", {"shop9": serializers.serialize('json', s9),})