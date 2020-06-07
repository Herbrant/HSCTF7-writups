import jwt

public = open('public.pem', 'r').read()
print(public)


val = jwt.encode({"auth":"admin"}, key=public, algorithm='HS256')

print(val)