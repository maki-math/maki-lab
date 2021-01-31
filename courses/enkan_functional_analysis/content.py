# -*- coding: utf-8 -*-

f = open('content.md', 'r')
flag=0
author=""
course_name=""
l=[]
s=""
for x in f:
    x=x.rstrip("\n")
    if len(x)!=0:
        if x[0] == "#":
            course_name=x
        else:
            if "." not in x:
                author=x
                print(author)
            if  "." in x:
                temp=x.split(".")
                chapter_number=temp[0]
                chapter_name=temp[1].strip()
                s=s+"<li>\n"+"<li><a onclick=\"find_html_short(" + str(chapter_number) +")\">"+  x +"</a></li>\n"+"</li>\n"
for item in l:
    print item
    
f = open("myfile.txt", "w")
f.write(s)
f.close

f = open("myfile.txt", "r")
print(f.read())
    

#<li>
#<li><a onclick="find_html_short(1)">2.1 Definition of Rings</a></li>
#</li>    