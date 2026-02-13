from bs4 import BeautifulSoup

new_message = "# Mon CV \n For an english version, see my [website](https://mathieubazinet.github.io/eng/cv/). \n"

with open("./_pages/cv_fr.md", 'r') as f:
  html_cv = f.read()

soup_cv = BeautifulSoup(html_cv, 'lxml')

for section in soup_cv.find_all('section'):
    if section.find("h2").get_text() in ['Éducation', 'Distinctions académiques']:
      new_message += str(section) + "\n"
 
with open("./_pages/publications_fr.html", 'r') as f:
    html_publications = f.read()

soup_pub = BeautifulSoup(html_publications, 'lxml')

for section in soup_pub.find_all('section'):
  new_message += "<section>\n" + str(section.find("h2")) + "\n"
  for my_soup in section.find_all('article'):
    new_message += "<article>\n" + str(my_soup.find("h3")) + "\n" + "<p>"

    new_message += str(my_soup.find("p", class_='authors')).replace('<p class="authors">', '').replace("</p>", '').rstrip() + "\n<br>"
    if my_soup.find("p", class_='conference') is not None:
      new_message += "Publié dans la conférence " + my_soup.find("p", class_='conference').get_text() + "\n<br>"
    elif my_soup.find("p", class_='journal') is not None:
      new_message += "Publié dans le journal " + my_soup.find("p", class_='journal').get_text() + "\n<br>"
    elif my_soup.find("p", class_='venue') is not None:
      new_message += my_soup.find("p", class_='venue').get_text() + "\n<br>"
    
    if my_soup.find("p", class_='note') is not None:
      new_message += str(my_soup.find("p", class_='note')).replace('<p class="note">', '').replace("</p>", '').rstrip() + "\n<br>"

    if my_soup.find("div", class_='links') is not None:
      new_message += str(my_soup.find("div", class_='links')).replace('<div class="links">', '').replace("</div>", '') +"</p>" +"\n"
    new_message += "</article>\n"

  new_message += "</section>\n\n"

with open("./_pages/contributions_fr.html", 'r') as f:
    html_cont = f.read()

soup_cont = BeautifulSoup(html_cont, 'lxml')

for section in soup_cont.find_all('section'):
    new_message += str(section) + "\n"


with open("./_pages/experience_fr.md", 'r') as f:
    html_exp = f.read()

soup_exp = BeautifulSoup(html_exp, 'lxml')

for section in soup_exp.find_all('section'):
    new_message += str(section) + "\n"

for section in soup_cv.find_all('section'):
    if section.find("h2").get_text() in ['Formations', 'Compétences particulières']:
      new_message += str(section) + "\n"

with open("./files/github_read_me.md", 'w') as f:
   f.write(new_message)