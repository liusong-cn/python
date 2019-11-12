import sys

def try_exception():
    try:
        print(sys.argv[0])
    except Exception as e:
        print('myname')
        print(e.args,e.strerror)
try_exception()