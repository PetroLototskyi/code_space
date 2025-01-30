from django.shortcuts import render
import markdown2
import random
from django.contrib import messages

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def md_to_html(title):
    text  = util.get_entry(title)
    markdown_instance = markdown2.Markdown()
    if text == None:
        return None
    else:
        return markdown_instance.convert(text)


def entry(request, title):
    html = md_to_html(title)
    # print("Title get from entry: ", title)
    if html == None:
        return render (request, "encyclopedia/error.html", {
            "error_message": f" The '{title}' requested page was not found."
        })
    else:
        return render (request, "encyclopedia/entry.html", {
            "title" : title,
            "content": html
        })

def search(request):
    if request.method =="POST":
        query = request.POST['q']
        html = md_to_html(query)
        if html:
            return render(request, "encyclopedia/entry.html", {
                "title": query,
                "content": html
            })

        all_entries = util.list_entries()
        recommendations = [entry for entry in all_entries if query.lower() in entry.lower()]
        """"for entry in all_entries:
                if query.lower() in entry.lower():
                    recommendations.append(entry)"""
        return render(request, "encyclopedia/search.html", {
            "recommendations": recommendations
            })

def create_new_page(request):
    if request.method == "GET":
        return render(request, "encyclopedia/new.html")

    title =request.POST['title']
    content= request.POST['content']

    # Check if the entry already exists
    if util.get_entry(title):
        return render(request, "encyclopedia/error.html", {
            "error_message": f"The '{title}' entry page already exists"
        })

    # Save the new entry
    util.save_entry(title, content)
    html =md_to_html(title)

    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": html
    })


def edit_page(request):
    if request.method == 'POST':
        title = request.POST['entry_title']
        content =util.get_entry(title)

        return render(request, "encyclopedia/edit.html", {
            "title": title,
            "content": content
        })

def save_edit(request):
    if request.method =='POST':
        title = request.POST['title']
        content = request.POST['content']
        util.save_entry(title, content)
        html=md_to_html(title)
        return render(request, "encyclopedia/entry.html", {
            "title":title,
            "content":html
        })

def random_page(request):
    all_entries =util.list_entries()
    # print(allEntries)
    rand_entry =random.choice(all_entries)
    html = md_to_html(rand_entry)
    return render(request, "encyclopedia/entry.html", {
        "title": rand_entry,
        "content": html
    })

def delete(request):
     if request.method =='POST':
        title = request.POST['entry_title']
        util.del_entry(title)
        messages.success(request, f"The entry '{title}' was deleted.") # message
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries()
        })
