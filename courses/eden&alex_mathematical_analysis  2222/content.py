# -*- coding: utf-8 -*-

f = open('content.md', 'r')
flag=0
author=""
course_name=""
l=[]
chapnum=0
s=""
il_open=False
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
                    s=s+"<li>\n<li><a onclick=\"find_html_short(" + str(chapter_number) +")\">"+  x +"</a></li>\n</li>\n"
            if flag==2:
                if "." not in x:
                    author=x
                else:
                    if il_open==True and x[0]!=" ":
                        s=s+"</ul> \n</li>\n"
                        il_open=False
                    if x[0]!=" ":
                        il_open=True
                        temp=x.split(".")
                        chapter_number=temp[0]
                        chapter_name=temp[1].strip()
                        s=s+"<li>\n<a href=\"Chap"+chapter_number+"\" data-toggle=\"collapse\" aria-expanded=\"false\" class=\"dropdown-toggle\">Chap. "+x+"</a>\n<ul class=\"collapse list-unstyled\" id=\"Chap"+chapter_number+"\">\n"
                    else:
                        x=x.strip()
                        temp=x.split(".")
                        section_number=temp[0]
                        section_name=temp[1].strip()                        
                        s=s+"<li><a onclick=\"find_html("+chapter_number+", "+section_number+")\">"+chapter_number +"."+x+"</a></li>\n"
                        #<li><a onclick="find_html(1, 1)">1.1 Definition of Groups</a></li>
                        
            if x.strip()=="小课":
                flag=1
            if x.strip()=="大课":
                flag=2
if flag==2:
    s=s+"</ul> \n</li>\n"

#<li>
    #<a href="#Chap1" data-toggle="collapse" aria-expanded="false" class="dropdown-toggle">Chap. 1 Groups</a>
    #<ul class="collapse list-unstyled" id="Chap1">
      #<li><a onclick="find_html(1, 1)">1.1 Definition of Groups</a></li>
      #<li><a onclick="find_html(1, 2)">1.2 More Examples of Groups</a></li>
      #<li><a onclick="find_html(1, 3)">1.3 Subgroups and Cosets</a></li>
      #<li><a onclick="find_html(1, 4)">1.4 Normalizer and Centralizer</a></li>
      #<li><a onclick="find_html(1, 5)">1.5 Normal Subgroup and Quotient Group</a></li>
      #<li><a onclick="find_html(1, 6)">1.6 Homomorphisms</a></li>
      #<li><a onclick="find_html(1, 7)">1.7 The Fundamental Theorem of Homomorphisms</a></li>
      #<li><a onclick="find_html(1, 8)">1.8 Cyclic Groups</a></li>
    #</ul>
#<li>

  #<li>
    #<a href="#Chap2" data-toggle="collapse" aria-expanded="false" class="dropdown-toggle">Chap. 2 Rings</a>
    #<ul class="collapse list-unstyled" id="Chap2">
      #<li><a onclick="find_html(2, 1)">2.1 Definition of Rings</a></li>
    #</ul>
  #</li>
  
  
  
  
  #<li>
  #<li><a onclick="find_html_short(1)">2.1 Definition of Rings</a></li>
  #</li>    
  
  
f = open("content.txt", "w")
f.write(s)
f.close

f = open("content.txt", "r")
print(f.read())
    
