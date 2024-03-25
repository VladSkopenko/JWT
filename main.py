from jose import jwt


payload = {"sub": "0631934048", "name": "Skopenko Vladislav"}

secret_key = "Some key"
encoded = jwt.encode(payload, secret_key, algorithm='HS256')
print(encoded)

# перевірка токена
decoded = jwt.decode(encoded, secret_key, algorithms=['HS256'])
print(decoded)
