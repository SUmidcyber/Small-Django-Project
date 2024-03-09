from django.shortcuts import render

abaut_list = [
    {
        'name': 'Baskets with',
        'title': 'Your right',
        'abaut': 'Hello, welcome, I wish you have fun and have a good Sunday, thank you for choosing us.',
        'days' : 'Yesterday',

    }
]

index_list = [
    {
        'title': 'Cyber Security Sales Store',
        'abaut': 'Hello, this is a cyber security sales store. If you want, you can click on the basket button and look at the sales products of our page. Best regards.',


    }
]




def index(request):
    data =  { 
        "abaut_list": abaut_list,
        "index_list": index_list

    }
    return render(request, "index.html", data)

