from django.http import JsonResponse
from django.shortcuts import render

from calorie.models import count

# Create your views here.
def add_data(request):
    food1=request.GET.get('food')
    value1=request.GET.get('value')
    data=count.objects.filter(food=food1)
    if len(data)>0:
        return JsonResponse('Item Already Added to list ',safe=False)
    object=count(food=food1,value=value1)
    object.save()
    return JsonResponse("ITEM ADDED SUCCESSFULLY",safe=False)

def user_entry(request):
    string=request.GET.get('list')
    list1=string.split(',')
    result=0
    j={}
    for i in list1:
        data=count.objects.filter(food=i)
        if len(data)==0:
            continue
        answer=data[0].value
        j[i]=answer
        result+=answer
    return JsonResponse('list is \n'+str(j)+'\n and final calorie count is '+str(result),safe=False)
            
