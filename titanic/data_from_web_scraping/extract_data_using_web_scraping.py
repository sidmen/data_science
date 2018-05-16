import requests
from bs4 import BeautifulSoup

html_string = """<!doctype html>
<html lang="en">
<head>
  <title>Doing Data Science With Python</title>
</head>
<body>
  <h1 style="color:#F15B2A;">Doing Data Science With Python</h1>
  <p id="author">Author : Sidharth Menon</p>
  <p id="description">This course will help you to perform various data science activities using python.</p>

  <h3 style="color:#404040;">Modules</h3>
  <table id="module" style="width:100%">
    <tr>
      <th>Title</th>
      <th>Duration (In Minutes)</th>
    </tr>
    <tr>
      <td>Getting Started</td>
      <td>20</td>
    </tr>
    <tr>
      <td>Setting up the Environment</td>
      <td>40</td>
    </tr>
    <tr>
      <td>Extracting Data</td>
      <td>35</td>
    </tr>
    <tr>
      <td>Exploring and Processing Data - Part 1</td>
      <td>45</td>
    </tr>
    <tr>
      <td>Exploring and Processing Data - Part 2</td>
      <td>45</td>
    </tr>
    <tr>
      <td>Building Predictive Model</td>
      <td>30</td>
    </tr>
  </table>
</body>
</html>
"""
from IPython.core.display import display, html
display(HTML(html_string))


ps = BeautifulSoup(html_string)
# print(ps)
#
# body = ps.find(name="body")
# print(body)
#
# print(body.find(name="h1").text)
# print(body.find(name="p"))
# print(body.findAll(name="p"))   # to get all p tags
#
# for p in body.findAll(name="p"):
#     print(p.text)
#
# print(body.find(name='p', attrs={"id": "author"}))
# print(body.find(name='p', attrs={"id": "description"}))


#### WEB SCRAPING STARTS ###
body = ps.find(name="body")
module_table = body.find(name='table', attrs={"id": "module"})
for row in module_table.findAll(name='tr')[1:]:
    title = row.findAll(name='td')[0].text
    duration = int(row.findAll(name='td')[1].text)
    print(title, duration)
