# -*- coding: utf-8 -*-

f = open('content.md', 'r')
flag=0
author=""
course_name=""
l=[]
s=""
flag=-1
for x in f:
    x=x.rstrip("\n")
    if len(x)!=0:
        if x[0] == "#":
            course_name=x
        else:
            if flag==1:
                if "." not in x:
                    author=x
                else:
                    temp=x.split(".")
                    chapter_number=temp[0]
                    chapter_name=temp[1].strip()
                    s=s+"<li>\n"+"<li><a onclick=\"find_html_short(" + str(chapter_number) +")\">"+  x +"</a></li>\n"+"</li>\n"
            if flag==2:
                if "." not in x:
                    author=x
                else:
                    print(x)
            if x.strip()=="小课":
                flag=1
            if x.strip()=="大课":
                flag=2

f = open("content.txt", "w")
f.write(s)
f.close

f = open("content.txt", "r")
print(f.read())
    

#<li>
#<li><a onclick="find_html_short(1)">2.1 Definition of Rings</a></li>
#</li>    