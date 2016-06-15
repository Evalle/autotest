import sys
from splinter import Browser

class Colors:

    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'

# colors
blue = Colors.BLUE
green = Colors.GREEN
yellow = Colors.YELLOW
red = Colors.RED
end = Colors.END

browser = Browser('phantomjs')

errors = 0

url = "http://crowbar:crowbar@127.0.0.10:3000"
browser.visit(url)

def check_text(text):

    global errors

    if browser.is_text_present(text):
        print(text + ' test ' + green + 'PASSED' + end)
    else:
        print(text + ' test ' + red + 'FAILED' + end)
        errors += 1 


print("1st group of tests")
print('=========')

check_text('3 nodes')
check_text('crowbar')
check_text('dashboard')

print()
print('=======')
print("Errors: " + str(errors))
