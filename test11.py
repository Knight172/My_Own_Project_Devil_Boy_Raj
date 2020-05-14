#Web Scraping Tutorial using Python and BeautifulSoup 
_______________________________________________________________
#Testing Website Link: https://www.codewithharry.com/
_______________________________________________________________________

import requests
from bs4 import BeautifulSoup                                                              #h1
a_d = "https://www.codewithharry.com/"                                                     #p 
a_b = requests.get(a_d).text                                         
# soup = BeautifulSoup(a_b,"html.parser")                            
# print(soup.title)                                                                        #div
# soup_text = BeautifulSoup(a_b,"html.parser")                                             #a
# print(soup_text.title.string)                                                            #br
# soup_body = BeautifulSoup(a_b,"html.parser")                                             #b
# print(soup_body.body)                                              
# soup_body_text = BeautifulSoup(a_b,"html.parser")
# print(soup_body_text.body.string)
#>>h1 tag:
# soup_p_tag = BeautifulSoup(a_b,"html.parser")
# print(soup_p_tag.body.h1) 
#>>h1 class:
# soup_h1_class = BeautifulSoup(a_b,"html.parser")
# print(soup_h1_class.h1["class"])
#>>p tag 
# soup_p = BeautifulSoup(a_b,"html.parser")
# print(soup_p.p)
#>>p class 
# soup_p = BeautifulSoup(a_b,"html.parser")
# print(soup_p.p["class"]) 
#>>p class text
# soup_class_p_text = BeautifulSoup(a_b,"html.parser")
# print(soup_class_p_text.p.get_text())
#>>p all find tag 
# p_all_tage_find = BeautifulSoup(a_b,"html.parser")
# print(p_all_tage_find.find_all("p"))
#>>p all find tag line by line design
# soup_p_find_all_design = BeautifulSoup(a_b,"html.parser")
# for x in soup_p_find_all_design.find_all("p"):
#     print(x)
#>>p all find href="/blog"
# P_href_blog = BeautifulSoup(a_b,"html.parser")
# print(P_href_blog.find_all(href="/blog"))
#>>div tag 
# soup_div = BeautifulSoup(a_b,"html.parser")
# print(soup_div.div)
#>>a tag 
# a_tag = BeautifulSoup(a_b,"html.parser")
# print(a_tag.a)
#>>a tag all 
# a_tag_all = BeautifulSoup(a_b,"html.parser")
# print(a_tag_all.find_all("a"))
#>>a tag all line by line print
# a_tag_all = BeautifulSoup(a_b,"html.parser")
# for x in a_tag_all('a'):
#     print(x)
#>>a tag all href line print and # remove
# a_tag_href = BeautifulSoup(a_b,"html.parser")
# for x in a_tag_href.find_all('a'):
#     if(x.get('href')!="#"):
#        print(x.get('href'))
#>>set link golo link kora 
# a_set = set()
# a_u = BeautifulSoup(a_b,"html.parser")
# for x in a_u.find_all('a'):
#     if(x.get('href')!="#"):
#       linktext = "https://www.codewithharry.com" + x.get('href')
#       a_set.add(x)
#       print(linktext)
#>>br tag 
# a_br_tag = BeautifulSoup(a_b,'html.parser')
# print(a_br_tag.br)
# #>>b tag 
# p_br_tag = BeautifulSoup(a_b,'html.parser')
# print(p_br_tag.b)
