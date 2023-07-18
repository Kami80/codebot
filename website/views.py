from django.shortcuts import render
from django.contrib import messages
# Create your views here.
def home(request):
    lan_list = ["html", "markup", "css", "clike", "javascript", "c", "csharp", "cpp", "dart", "django", "go", "java", "markup-templating", "matlab", "mongodb", "objectivec", "perl", "php", "powershell", "python", "r", "jsx", "regex", "ruby", "rust", "sass", "scala", "sql", "swift"]
    lan_list.sort()
    
    if request.method == "POST":
        code = request.POST['code']
        lan = request.POST['lan']
        if lan == "Select Programming Language":
            messages.success(request, "Hey! Please Pick a Programing Language")
            context = {"lan_list":lan_list, "code":code, "lan":lan}  
            return render(request, 'home.html', context)
        context = {"lan_list":lan_list, "code":code, "lan":lan}  
        return render(request, 'home.html', context)

    context = {"lan_list":lan_list, "code":code, "lan":lan}  
    return render(request, 'home.html', context)

