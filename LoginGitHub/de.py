from lxml import etree

html = etree.parse('./demo.html', etree.HTMLParser())
name = html.xpath('//*[@id="user_profile_name"]/@value')
email = html.xpath('//*[@id="user_profile_email"]/option[3]/@value')
print(name, email)