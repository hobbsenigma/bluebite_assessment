from django.shortcuts import render        
from django.db import transaction
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse, HttpResponseNotFound
from rest_framework.decorators import api_view
import json
from jsonschema import validate
from assessment.models import Batch, Object, Data

@transaction.atomic()
def write_batch(batch_json):    
    batch = Batch(batch_alpha_id=batch_json["batch_id"])
    batch.save()
    
    for json_object in batch_json["objects"]:
        object = Object(batch = batch, object_alpha_id = json_object["object_id"])
        object.save()
        for json_data in json_object["data"]:
            data = Data(object = object, key=json_data["key"], value=json_data["value"])
            data.save()


@api_view(['POST'])
def submit_json(request):
    
    f = open('files/schema.json',)    
    schema = json.load(f)
    f.close()

    try:
        json_body = json.loads(request.body)        
        validate(json_body, schema=schema)        
        write_batch(json_body)        
        return HttpResponse()
    except Exception as e:
        return HttpResponseBadRequest(str(e))

# return an object based on its ID
@api_view(['GET'])
def get_object_by_id(request):    
    if not request.GET.get("id"):
        return HttpResponseBadRequest()
    
    object = Object.objects.filter(object_alpha_id = request.GET["id"]).first()
    if not object:
        return HttpResponseNotFound()
    
    object_data = Data.objects.filter(object=object.id)
    
    data = []
    for d in object_data:
        data.append({"key": d.key, "value": d.value})
    json = {"object_id": object.object_alpha_id, "data": data}
    return JsonResponse(json, safe=False)

# for any objects with matching keys/values, return those objects with all key value pairs
@api_view(['GET'])
def get_object_by_data(request):    
    
    # handle all cases of presence/absence of query parameters
    data = None
    if request.GET.get("key") and request.GET.get("value"):
        data = Data.objects.filter(key = request.GET["key"], value = request.GET["value"])
    elif request.GET.get("key"):
        data = Data.objects.filter(key = request.GET["key"])
    elif request.GET.get("value"):
        data = Data.objects.filter(value = request.GET["value"])
    else:
        return HttpResponseBadRequest()
    
    if not data:
        return HttpResponseNotFound()
    
    # use a set to avoid returning the same object multiple times
    objects = set()
    for d in data:
        object = Object.objects.filter(id = d.object_id).first()
        objects.add(object)

    object_list = []
    for o in objects:
        object_data = Data.objects.filter(object=o.id)
    
        return_data = []
        for d in object_data:
            return_data.append({"key": d.key, "value": d.value})
        object_list.append({"object_id": o.object_alpha_id, "data": return_data})

    json = {"matching_objects": object_list}
    return JsonResponse(json)
