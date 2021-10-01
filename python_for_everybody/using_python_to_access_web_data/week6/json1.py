import json

data = '''{
"name" : "Chuck",
"phone" : {
    "type" : "intl",
    "number" : "89144509812"
    },
    "email" : {
        "hide" : "yes"
        }
}'''

info = json.loads(data)
print(info)
print('Name:', info['name'])
print('Hide', info['email']['hide'])
print('Phone', info['phone']['number'])
