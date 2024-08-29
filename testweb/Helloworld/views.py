from django.shortcuts import render ,HttpResponse,redirect
from .models import Person

# Create your views here.
def index(request):
    # 查询出Person对象信息，也就是数据表中的所有数据
    # 一行数据就是一个对象，一个格子的数据就是一个对象的一个属性值
    objs = Person.objects.all()

    # locals函数可以将该函数中出现过的所有变量传入到展示页面中，即index.html文件中
    # return render(request, 'index.html', locals())
    print(locals())
    return HttpResponse(content = locals())
def user_list(request):
    from Helloworld.models import Person
    if request.method == 'GET':
        all_data = Person.objects.all()

        return render(request, 'user_list.html', context={"user_list":all_data})
    if request.method =='POST':
        post_data = request.POST
        col = post_data.get("which_col")
        Person.objects.filter(id=col).delete()  # 删除表中id为2的删除
        all_data = Person.objects.all()
        return render(request, 'user_list.html', context={"user_list":all_data})


def user_add(request):
    from Helloworld.models import Person
    if request.method == 'GET':
        return render (request,'login.html',{"msg":"点击添加信息"})
    if request.method == "POST":

        all_data = request.POST

        if "button0" in all_data:
            return render(request, 'login.html', )
        else:
            post_data = request.POST

            Person.objects.create(name = post_data.get("username"), age = post_data.get("userage"), score =  post_data.get("userscore"), sex = post_data.get ("usersex"))
            return redirect("http://127.0.0.1:8000/user/")


def user_update(request):
    from Helloworld.models import Person
    global id_update
    if request.method == 'GET':
        return render (request,'update.html',{"msg":"点击修改信息"})
    if request.method == "POST":
        all_data = request.POST

        if "button1" in all_data:
            id_update = all_data.get("which_col_to_update")
            return render(request, 'update.html', {"msg": "点击修改信息"})
        else:

            post_data = request.POST
            Person.objects.filter(id=id_update).update(name = post_data.get("username"), age = post_data.get("userage"), score =  post_data.get("userscore"), sex = post_data.get ("usersex"))
            return redirect("http://127.0.0.1:8000/user/")
def user_filter(request):
    from Helloworld.models import Person
    global id_filter
    if request.method == 'GET':
        return render(request, 'filter.html', {"user": "点击修改信息"})
    if request.method == "POST":
        all_data = request.POST
        if "button2" in all_data:
            id_filter = all_data.get("which_col_to_filter")
            user = Person.objects.filter(id=id_filter).first()
            return render(request, 'filter.html', {"user": user})
        else:
            post_data = request.POST
            Person.objects.filter(id=id_filter)
            return redirect("http://127.0.0.1:8000/user/")