from ast import If
from  django.shortcuts import render,redirect
from polls.models import Products
from django.contrib import messages
from polls.serializers import POLLSerializer 
from categories.models import Categories
from categories.serializers import CategoriesSerializer
from Size.models import Size
from Size.serializers import SizeSerializer
from colors.models import Colors
from colors.serializers import ColorsSerializer
from sub_categories.models import SUBCategories
from sub_categories.serializers import SUBCategoriesSerializer



def showAdminPage(request):
    showpage = Products.objects.all()
    serializer = POLLSerializer(showpage,many=True)
    return render(request,'polls/starter.html',{"data":serializer.data})

def show(request):
    showall = Products.objects.filter(isactive=True) 
    print("show all data:",showall)
    serializer = POLLSerializer(showall,many=True)  
    data = serializer.data
    
    for i in range(len(data)):
        product = Products.objects.filter(id=data[i]['id']).first()
        data[i]['categories'] = product.categories.__str__()
        data[i]['color'] = product.color.__str__()
        data[i]['size'] = product.size.__str__()
        data[i]['sub_categories'] = product.sub_categories.__str__()
   
    return render(request,'polls/product_list.html',{"data":data})


def insert(request):
    data = {}
    if request.method == "POST":
        print('POST',id)
        data['categories'] = request.POST.get('categories')
        data['sub_categories'] = request.POST.get('sub_categories')
        data['color'] = request.POST.get('color')
        data['size'] = request.POST.get('size')
        data['title'] = request.POST.get('title')
        data['price'] = request.POST.get('price')
        data['sku_number'] = request.POST.get('sku_number')
        data['product_details'] = request.POST.get('product_details')
        data['quantity'] = request.POST.get('quantity')

        form = POLLSerializer(data=data)
        print(form)
        if form.is_valid():
            print('form after valid:',form)
            print("error of form:",form.errors)
            form.save()
            
            messages.success(request, "Record Updated Successfully...!:)")
            return redirect("polls:show")
        else:
            print('form not valid')
            print(form.errors)
    if request.method == "GET":
        print('POST',id)
        category_dict = Categories.objects.filter(isactive=True)
        category = CategoriesSerializer(category_dict, many=True)
        sub_category_dict = SUBCategories.objects.filter(isactive=True)
        sub_category = SUBCategoriesSerializer(sub_category_dict,many=True)
        color_dict = Colors.objects.filter(isactive=True)
        color = ColorsSerializer(color_dict,many=True)
        size_dict = Size.objects.filter(isactive=True)
        size = SizeSerializer(size_dict,many=True)
        hm = {"context": category.data,"sub_context":sub_category.data,"color_context":color.data,"size_context":size.data}
        return render(request, "polls/product_insert.html", hm)
 



def update(request,id):
    if request.method == 'GET':
        print('GET',id)
        edit_clothes = Products.objects.filter(id=id).first()
        s= POLLSerializer(edit_clothes)
        return render(request,'polls/product_edit.html',{"Products":s.data})
    else:
        print('POST',id)
        update_clothes = {}
        
        d = Products.objects.filter(id=id).first()
        if d:
            update_clothes['Categories']=request.POST.get('Categories')
            update_clothes['sub_categories']=request.POST.get('sub_categories')
            update_clothes['lastname']=request.POST.get('lastname')
            update_clothes['Color']=request.POST.get('Color')
            update_clothes['Size']=request.POST.get('Size')
            update_clothes['image']=request.POST.get('image')
            update_clothes['title']=request.POST.get('title')
            update_clothes['sku_number']=request.POST.get('sku_number')
            update_clothes['prod_details']=request.POST.get('prod_details')
            update_clothes['quantity']=request.POST.get('quantity')
        # Updateemp = EmpModel.objects.get(id=id)
            #print(Updateemp)
            form = POLLSerializer(d,data=update_clothes)
            if form.is_valid():
                form.save()
                # print("hkjk",form.data)
                messages.success(request,'Record Updated Successfully...!:)')
                return redirect('polls:showemp')
            else:
                print(form.errors)




# def updateemp(request,id):
#     # Updateemp = {}
#     # if request.method=='POST':
#     #     data = EmpModel.objects.get(id=id)
#     #     if data:
#     #         Updateemp['firstname']=request.POST.get('firstname')
#     #         Updateemp['middlename']=request.POST.get('middlename')
#     #         Updateemp['lastname']=request.POST.get('lastname')
#     #         Updateemp['department']=request.POST.get('department')
#     #         Updateemp['designation']=request.POST.get('designation')
#     #         Updateemp['status']=request.POST.get('status')
#     #         Updateemp['salary']=request.POST.get('salary')
#     #         Updateemp['gender']=request.POST.get('gender')
#     #     # Updateemp = EmpModel.objects.get(id=id)
#     #         #print(Updateemp)
#     #         form = CRUDSerializer(data,data=Updateemp)
#     #         if form.is_valid():
#     #             form.save()
#     #             messages.success(request,'Record Updated Successfully...!:)')
#     #             return render(request,'Edit.html',{"EmpModel":Updateemp})
#     # return render(request,'Edit.html',Updateemp)


# def Delemp(request,id):
#     delemployee = Products.objects.get(id=id)
#     Delemp={}
#     #Delemp['isactive']=False
#     form = POLLSerializer(delemployee,data=Delemp)
#     if form.is_valid():
#         form.save()
#         messages.success(request,'Record Deleted Successfully...!:)')
#         return redirect('app1:showemp')
#     else:
#         print("sfsdrf",form.errors)
#         return redirect('app1:showemp')

def delete(request,id):
    deleteclothes = Products.objects.all(id=id)
    delclothes = {}
    delclothes['isactive']=False
    form = POLLSerializer(deleteclothes,data=delclothes)
    if form.is_valid():
        form.save()
        return redirect('polls:show')
    else:
        return redirect('polls:show')
    

