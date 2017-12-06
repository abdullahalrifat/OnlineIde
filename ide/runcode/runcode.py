import subprocess
import sys
import os


class RunCCode(object):
    def __init__(self, code=None, input=None):
        self.code = code
        self.input=input
        self.compiler = "gcc"
        if not os.path.exists('running'):
            os.mkdir('running')

    def _compile_c_code(self, filename, fileinput, prog="./running/a.out"):
        cmd = [self.compiler, filename, fileinput, "-Wall", "-o", prog]
        p = subprocess.Popen(cmd,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result = p.wait()
        a, b= p.communicate()
        self.stdout, self.stderr = a.decode("utf-8"), b.decode("utf-8")
        return result

    def _run_c_prog(self, cmd="./running/a.out"):
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE )
        result = p.wait()
        a, b = p.communicate()
        self.stdout, self.stderr= a.decode("utf-8"), b.decode("utf-8")
        return result

    def run_c_code(self, code=None,input=None):
        filename = "./running/test.c"
        fileinput = "./running/testc.in"
        if not code:
            code = self.code
        if not input:
            input = self.input

        result_run = "No run done"

        with open(filename, "w") as f:
            f.write(code)

        with open(fileinput, "w") as ff:
            ff.write(input)

        res = self._compile_c_code(filename,fileinput)
        result_compilation = self.stdout + self.stderr
        if res == 0:
            self._run_c_prog()
            result_run = self.stdout + self.stderr
        return result_compilation, result_run , input


class RunCppCode(object):
    def __init__(self, code=None,input=None):
        self.code = code
        self.input=input
        self.compiler = "g++"
        if not os.path.exists('running'):
            os.mkdir('running')

    def _compile_cpp_code(self, filename, prog="./running/a.out"):
        cmd = [self.compiler, filename, "-Wall", "-o", prog]
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result = p.wait()
        a, b = p.communicate()
        self.stdout, self.stderr = a.decode("utf-8"), b.decode("utf-8")
        return result

    def _run_cpp_prog(self,fileinput, cmd="./running/a.out"):
        p = subprocess.Popen(cmd,  shell=True,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        with open(fileinput, 'r') as content_file:
            content = content_file.read()
        p.stdin.write(content.encode("utf-8"))
        p.stdin.flush()
        """result = p.wait()"""

        a, b= p.communicate()

        self.stdout, self.stderr = a.decode("utf-8"), b.decode("utf-8")
        self.stdin=content
        return p.stdout



    def run_cpp_code(self, code=None, input=None):
        filename = "./running/test.cpp"
        fileinput= "./running/testcpp.in"
        if not code:
            code = self.code
        if not input:
            input=self.input
        result_run = "No run done"
        with open(filename, "w") as f:
            f.write(code)

        with open(fileinput, "w") as ff:
            ff.write(input)

        res = self._compile_cpp_code(filename)
        result_compilation = self.stdout + self.stderr
        if res == 0:
            self._run_cpp_prog(fileinput)
            result_run = self.stdout + self.stderr
        return result_compilation, result_run


class RunPyCode(object):
    def __init__(self, code=None):
        self.code = code
        if not os.path.exists('running'):
            os.mkdir('running')

    def _run_py_prog(self, cmd="a.py"):
        cmd = [sys.executable, cmd]
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result = p.wait()
        a, b = p.communicate()
        self.stdout, self.stderr = a.decode("utf-8"), b.decode("utf-8")
        return result

    def run_py_code(self, code=None):
        filename = "./running/a.py"
        if not code:
            code = self.code

        with open(filename, "w") as f:
            f.write(code)
        self._run_py_prog(filename)
        return self.stderr, self.stdout