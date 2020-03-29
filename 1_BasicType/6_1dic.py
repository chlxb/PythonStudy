# 4_1 字典示例

# 一个简单的数据库
# 一个将人名用作键的字典。每个人用一个字典表示，
# 字典包含键‘phone’ 和 'addr', 他们分别与电话号码和地址相关联
people = {
    'Alice': {
        'phone': '2341',
        'addr': 'Foo drive 23'
    },
    'Beth': {
        'phone': '9102',
        'addr': 'Bar street 42'
    },
    'Cecil': {
        'phone': '3158',
        'addr': 'Baz avenue 90'
    }
}

# 电话号码和地址的描述性标签，打印输出时使用
labels = {
    'phone': 'phone number',
    'addr': 'address'
}

name = input('Name: ')

# 要查找电话号码还是地址？
request = input('Phone number (p) or address (a)? ')

# 使用正确的键：
if request == 'p': key = 'phone'
if request == 'a': key = 'addr'

if name in people: print("{}'s {} is {}.".format(name, labels[key], people[name][key]))
else: print("'{}' is not in dic".format(name))


# 将字符串格式设置功能用于字典
print('======== 将字符串格式设置功能用于字典 ========')
phonebook = {'Cecil': '9102', 'Alice': '2341', 'Beth': '3258'}
print("Cecil's phone number is {Cecil}.".format_map(phonebook))

template = '''<html>
<head><title>{title}</title></head>
<body>
<h1>{title}</h1>                    
<p>{text}</p>
</body>'''

data = {'title': 'My Home Page', 'text': 'Welcome to my home page!'}
print(template.format_map(data))
