import requests
from lxml import html

url = 'https://www.bangla-kobita.com/jasimuddin/post20160512033403/'
response = requests.get(url)
tree = html.fromstring(response.content)

# XPath expression to select all p elements within a div with the class 'post-content noselect'
xpath = "//div[@class='post-content noselect']/p"

# Use the XPath expression to find all matching elements
elements = tree.xpath(xpath)

# Extract the text content of each p element, replacing <br> tags with newlines
content = []
for element in elements:
    text = element.text_content()
    for br in element.xpath(".//br"):
        br.tail = "\n" + br.tail if br.tail else "\n"
    content.append(text)

# Ignore the last p element if it contains the specified text
if content and content[-1].strip() == 'কাব্যগ্রন্থ: রাখালী':
    content.pop()

# Print the scraped content
for text in content:
    print(text)

