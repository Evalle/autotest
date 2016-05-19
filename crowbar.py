import sys
from splinter import Browser

browser = Browser('phantomjs')

errors = 0

url = "http://crowbar:crowbar@127.0.0.10:8080"
browser.visit(url)
if browser.is_text_present('2 nodes'):
    print("Yes, all 3 nodes are present")
else:
    print("No, nodes are not present")
    errors += 1 

browser.quit()
print("Errors:" + str(errors))
