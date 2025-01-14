from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Author


@login_required
def author_list(request):
    if request.user.role != 1:
        return redirect("home")
    authors = Author.objects.all()
    return render(request, "authors/list.html", {"authors": authors})

@login_required
def create_author(request):

    if request.user.role != 1:
        return redirect("home")

    if request.method == "POST":
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        patronymic = request.POST.get("patronymic")
        books_id = request.POST.getlist("books")

        if name:
            Author.objects.create(name=name, surname=surname, patronymic=patronymic)
            return redirect("author_list")
    return render(request, "authors/create.html")

@login_required
def delete_author(request, author_id):
    if request.user.role != 1:
        return redirect("home")
    author = Author.objects.filter(id=author_id).first()
    if author:
        if not author.books.exists():
            author.delete()
            return redirect("author_list")
        else:
            return render(request, "authors/cannot_delete.html", {"author": author})

    return redirect("author_list")