import re

list_pageviews=[]
list_broken_url=[]
log = open('devops.log', 'r')
for line in log.readlines():
    status_code= map(''.join, re.findall(r'\"(.*?)\"|\[(.*?)\]|(\S+)', line))[5]
    clint_url=map(''.join, re.findall(r'\"(.*?)\"|\[(.*?)\]|(\S+)', line))[0]
    if str(status_code) == '200':
        print status_code
        print clint_url
        list_pageviews.append(clint_url)
    elif str(status_code) is not '200':
        print status_code
        list_broken_url.append(clint_url)


print 'Clints'
print list(set(list_pageviews))
print 'Broken'
print list(set(list_broken_url))