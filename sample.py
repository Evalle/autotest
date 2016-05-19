from splinter import Browser

browser = Browser('phantomjs')

url = "https://google.com"
browser.visit(url)
browser.fill('q', 'yandex russian company')
# Find and click the 'search' button
button = browser.find_by_name('btnG')
# Interact with elements
button.click()
if browser.is_text_present('yandex.com'):
    print("Yes, the official website was found!")
else:
    print("No, it wasn't found... We need to improve our SEO techniques")

