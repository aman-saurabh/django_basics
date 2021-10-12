from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
import random

# Function to display Hello World on the screen
def hello(request):
    return HttpResponse("Hello World!")

# Function to demonstrate how to use templates in django
def hello_template(request):
    return render(request, 'template_hello_world.html')

# Function to demonstrate how to pass some value from view to template in django
def dynamic_template(request):
    data = {"name": "Aman"}
    return render(request, 'template_dynamic_content.html', data)

# Function to demonstrate how to fetch and use querystring parameters value in django
"""In querystring data is passed in URL as - http://localhost:8000/query_param/?id=9&name=Geetika
To test it enter this URL in your browser - http://localhost:8000/query_param/?id=5&name=Saurabh"""
def query_param_data(request):
    # To get all query parameters in dictionary form
    query_param = request.GET
    # Here we are using 'GET' since it is a 'GET' request.Use 'POST' inplace of 'GET' for 'POST' requests.
    print(query_param)

    # To get a particular parameter from the query string
    param_name = request.GET.get('name')
    data = {"name": param_name}
    return render(request, 'template_dynamic_content.html', data)

# Function to demonstrate how to pass data in URL and use them in django
"""In this approach data is passed in URL as - http://localhost:8000/9/Geetika
Here also note that in this approach we can get fields values in variables with that name only, which we
declared in 'path' in urls.py file.We can't get value of those fields in variables with other name.
Like here we are fetching values in variables 'id' and 'name'.We can't fetch them with any other variable name."""
def data_with_url(request, _id, name):
    print(_id)
    print(name)
    data = {"name": name}
    return render(request, 'template_dynamic_content.html', data)

# Function to demonstrate how to redirect from one page to another page in django
"""Such redirects are beneficial in cases like you want user to stay on the same page in case of unsuccessful
login attempt but want him/her to redirect to home page if login credentials gets verified."""
def redirect_another_page(request):
    return HttpResponseRedirect('/query_param/?id=9&name=Geetika')
    # Notes :-
    # 1.) Here we can also use "redirect()" function of "django.shortcuts" module inplace of "HttpResponseRedirect()"
    # i.e i.e we can write return statement as :- return redirect('/query_param/?id=9&name=Geetika')
    # 2.) Here applying forward slash(i.e "/") at the beginning of the desired URL(i.e 'query_param' in this case)
    # is mandatory. As without applying "/" at the beginning, it will redirect to the following address.
    # http://localhost:8000/redirect/query_param/?id=9&name=Geetika
    # Which is not our desired URL actually it should have redirected it to following address.
    # http://localhost:8000/query_param/?id=9&name=Geetika

# Function to demonstrate how to redirect from one page to another page on click of some button.For example -
"""Suppose we want a button(or link) on 'profile' page.when a user click that he/she should be redirected to 'home' page.
Such buttons(or links) are also known as navigator."""
def redirect_button_click(request):
    return render(request, 'template_button_redirect.html')

# Function to demonstrate how to use forms in Django.
"""Here we are using same function to render the form for filling and to submit the form.
The only difference is we have to use GET method for rendering form and POST method for submitting form."""
def simple_form(request):
    data = {
        'id': random.randint(101, 999) if request.method == 'POST' else None,
        'name': request.POST.get('name'),
        'location': request.POST.get('city')
    }
    print(data)
    return render(request, 'template_simple_form.html', data)
