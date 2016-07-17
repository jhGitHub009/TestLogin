from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

from customers.models import *
import json
import base64

# Create your views here.
def index(request):
	# return HttpResponse("Star WooChang Customer management")
    return render (request, 'customers/login.html')

#데코레이터 함수: need_auth
def need_auth(functor):
    def try_auth(request, *args, **kwargs):
        if 'HTTP_AUTHORIZATION' in request.META:
            basicauth = request.META['HTTP_AUTHORIZATION']
            user = None
            try:
                b64key = basicauth.split(' ')[1]
                key = base64.decodestring(b64key)
                (username,pw) = key.split(':')
        
                user = authenticate(username=username,password=pw)
            except:
                pass

            if user is not None:
                login(request, user)
                request.META['user'] = user
                return functor(request, *args, **kwargs)

        logout(request)
        response = HttpResponse()
        response.status_code = 401
        response['WWW-Authenticate'] = 'Basic realm="WooChang Material Control Service"'
        return response
    return try_auth


def toJSON(objs, status=200):
	json_str = json.dumps(objs, ensure_ascii=False)
	return HttpResponse(json_str, status=status, content_type='application/json; charset=utf-8')

# def serialize(objs):
# 	return map(lambda x:x.serialize(), objs)

def serialize(objs):
	serialized = []
	for obj in objs:
		serialized.append(obj.serialize())
	return serialized

@need_auth
def setpassword_view(request):
    try:
        password = request.POST.get('password')
        if password:
            request.user.set_password(password)
            request.user.save()
            return toJSON({'status':'ok'})
    except:
        pass
    return toJSON({'status':'no'})
         
@need_auth
def checkpassword_view(request):
    try:
        password = request.POST.get('password')
        if request.user.check_password(password):
            return toJSON({'status':'ok'})
    except:
        pass
    return toJSON({'status':'no'})

@need_auth
def customer_view(request):
	return HttpResponse('login Service')

# def user_view(request, method):
#     if method == 'create' and request.method == 'POST':
#         return HttpResponse('OK')
#     else:
#         return HttpResponse('bad request', status = 400)
# def user_view(request, method):
#     if method == 'create' and request.method =='POST':
#         # try:
#         username = 'testuser1'
#         password = 'a123456789'
#         # username = request.POST.get('username')
#         # password = request.POST.get('password')
#         if User.objects.filter(username__exact=username).count():
#             return toJSON({'status':'duplicate id'}, 400)
#         user = User.objects.create_user(username,password=password)
#         user.save()
#         return toJSON({'status':'create success'})
#         # except:
#         #     return toJSON({'status':'create fail'}, 400)

def user_view(request, method):
    if method == 'create' and request.method == 'POST':
        try:
            username = 'testuser1'
            password = 'a123456789'
            # username = request.POST.get('username')
            # password = request.POST.get('password')
            if User.objects.filter(username__exact=username).count():
                return toJSON({'status':'duplicate id'}, 400)
            user = User.objects.create_user(username,password=password)
            # user.first_name = request.POST.get('name','')
            user.save()
            profile = Customer()
            profile.아이디 = user
            profile.회사명 = 'TEST_Co.Ltd'
            # profile.회사명 = request.POST.get('회사명','')
            profile.save()
            return toJSON({'status':'create success'})
        except:
            return toJSON({'staus':'create fail'}, 400)
    if method == 'update' and request.method == 'POST':
        try:
            username = 'testuser1'
            password = 'a123456789'
            newpassword = 'a1234567'
            # username = request.POST.get('username')
            # password = request.POST.get('oldpassword')
            # newpassword = request.POST.get('newpassword')
            user = User.objects.get(username__exact=username)
            if user.check_password(password) is False:
                return toJSON({'status':'wrong password'}, 400)
            else:
                user.set_password(newpassword)
                # user.first_name = request.POST.get('name',user.first_name)
                # user.save()
        except:
            return toJSON({'status':'bad request'}, 400)
        return toJSON({'status':'updated'})

    if method == 'list':
        users = Customer.objects.all()
        return toJSON(serialize(users))
        # serialized = []
        # for u in users:
        #     serialized.append(u.serialize())
        # return toJSON(serialized)
        


@need_auth
def name_view(request):
    if request.method == 'GET':
        data = {
            '회사명' : reques.Customer.회사명,
        }
        return toJSON(data)
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            reques.Customer.회사명 = name
            request.Customer.save() 
            return toJSON({'status':'updated'})
        except:
            return toJSON({'status':'bad request'}, 400)

@need_auth
def profile_view(request, username=None):
    if username == None:
        username = request.user

    if request.method == 'GET':
        try:
            return toJSON(User.objects.get(username=username).userprofile.serialize())
        except:
            return toJSON({'status':'not found'}, 400)

    elif request.method == 'POST':
        profile = request.user.userprofile
        profile.회사명 = request.POST.get('회사명', profile.회사명)
        profile.담당자 = request.POST.get('담당자', profile.담당자)
        profile.회사번호_1 = request.POST.get('회사번호_1', profile.회사번호_1)
        profile.휴대폰번호 = request.POST.get('휴대폰번호', profile.휴대폰번호)
        # ignores = request.POST.get('ignore',None)
        # if ignores:
        #     ignores = json.loads(ignores)
        #     profile.set_ignorelist(ignores)

        profile.save()

        return toJSON({'status':'updated'})

# @need_auth
def login_view(request):
    return toJSON({'status':'ok',
                    'user':request.user.userprofile.serialize()})
