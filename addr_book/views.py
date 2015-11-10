from django.shortcuts import render_to_response
from django.template import Context
from addr_book.models import *

# Create your views here.
# hehe
def total(lists):
    counter = 0
    for temp in lists:
        counter = counter + 1
    return counter

def add(request):
    if request.POST:
        post=request.POST
        
        Author = author(
                AuthorID=post['authorid'],
                Name = post['name'],
                Age = post['age'],
                Country = post['country'])
        Author.save()
        new_book=book(
            Title=post["title"],
            Publisher=post["publisher"],
            PublishDate=post["publishdate"],
            Price=post["price"],
            ISBN=post["isbn"])
            
        new_book.Author = Author
        new_book.save()
    return render_to_response('add.html')

def look(request):
    book_list=book.objects.all()
    c=Context({"book_list":book_list,})
    return render_to_response("look.html",c)

def delete(request):
    isbn = request.GET['isbn']
    book.objects.filter(ISBN=isbn).delete()
    book_list=book.objects.all()
    if total(book_list) > 0:
        c=Context({"book_list":book_list,})
        return render_to_response("look.html",c)
    else:
        return render_to_response('look.html')
        
def search_author(request):
    if request.POST:
        name_au=request.POST['author']
        book_list=book.objects.all()
        c=Context({"book_list":book_list,"name_au":name_au,})
        return render_to_response("search_author.html",c)
    return render_to_response("search_author.html")

def information(request):
    isbn = request.GET['isbn']
    book_list = book.objects.get(ISBN=isbn)
    c=Context({"book_list":book_list,})
    return render_to_response("information.html",c)
    

    



    

    