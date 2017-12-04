from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
# Create your views here.
from django.views import generic

from ide.runcode import runcode

default_c_code = """#include <stdio.h>
int main(int argc, char **argv)
{
    printf("Hello C World!!\\n");
    return 0;
}    
"""

default_cpp_code = """#include <iostream>
using namespace std;
int main(int argc, char **argv)
{
    cout << "Hello C++ World" << endl;
    return 0;
}
"""

default_py_code = """import sys
import os
if __name__ == "__main__":
    print ("Hello Python World!!")
"""

default_rows = "15"
default_cols = "60"

class ide(generic.ListView):
    template_name = 'base.html'
    def get_queryset(self):
        return None


def runc(request):
    inputs = ''
    if request.method == 'POST':
        code = request.POST['code']
        inputs = request.POST['input']
        run = runcode.RunCCode(code)
        rescompil, resrun = run.run_c_code()
        if not resrun:
            resrun = 'No result!'
    else:
        code = default_c_code
        resrun = 'No result!'
        rescompil = ''
        inputs=''
    return render(request, 'main.html', {
        "code": code,
        "target": "runc",
        "resrun": resrun,
        "rescomp": rescompil,
        "rows": default_rows,
        "cols": default_cols,
        "input":inputs
    })



def runcpp(request):
    inputs=''
    if request.method == 'POST':
        code = request.POST['code']
        inputs = request.POST['input']
        run = runcode.RunCppCode(code)
        rescompil, resrun = run.run_cpp_code()
        if not resrun:
            resrun = 'No result!'
    else:
        code = default_cpp_code
        resrun = 'No result!'
        rescompil = ''
        inputs=''
    return render(request, 'main.html', {
        "code" :code,
        "target" : "runcpp",
        "resrun" : resrun,
        "rescomp" : rescompil,
        "rows" : default_rows,
        "cols" :default_cols,
        "input":inputs
        })



def runpy(request):
    inputs=''
    if request.method == 'POST':
        code = request.POST['code']
        inputs = request.POST['input']
        run = runcode.RunPyCode(code)
        rescompil, resrun = run.run_py_code()
        if not resrun:
            resrun = 'No result!'
    else:
        code = default_py_code
        inputs=''
        resrun = 'No result!'
        rescompil = "No compilation for Python"

    return render(request, 'main.html', {
        "code": code,
        "target": "runpy",
        "resrun": resrun,
        "rescomp": rescompil,
        "rows": default_rows,
        "cols": default_cols,
        "input":inputs
    })