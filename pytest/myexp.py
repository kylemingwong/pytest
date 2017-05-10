import logging

def foo(s):
    return 10/int(s)

def bar(s):
    return foo(s)*2

def main():
    try:
        bar('a')
    except Exception as e:
        logging.exception(e)
    finally:
        print 'Finally...'


main()
print 'END'