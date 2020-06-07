import jwt
# eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9
# {"typ":"JWT","alg":"RS256"}
# eyJpc3MiOiJodHRwOlwvXC9kZW1vLnNqb2VyZGxhbmdrZW1wZXIubmxcLyIsImlhdCI6MTUwNDAwNzg3NCwiZXhwIjoxNTA0MDA3OTk0LCJkYXRhIjp7ImhlbGxvIjoid29ybGQifX0
# {"iss":"http:\/\/demo.sjoerdlangkemper.nl\/","iat":1504007874,"exp":1504007994,"data":{"hello":"world"}}

public = open('public.pem', 'r').read()
print(public)


val = jwt.encode({"auth":"admin"}, key=public, algorithm='HS256')



print(val)

decoded = jwt.decode(val, public)["auth"] == "admin"


print(decoded)
