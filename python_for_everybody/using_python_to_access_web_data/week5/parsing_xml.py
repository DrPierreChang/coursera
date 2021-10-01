import xml.etree.ElementTree as ET

data = '''<person>
    <name>Andrey</name>
    <phone type="intl">
        +1 734 303 4456
    </phone>
    <email hide="yes"/>
    </person>'''

tree = ET.fromstring(data)
print(tree)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))