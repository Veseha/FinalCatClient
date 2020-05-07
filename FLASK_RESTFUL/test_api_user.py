from requests import get, post, delete

print(get('http://127.0.0.1:8080/api/v2/users').json())
print(get('http://127.0.0.1:8080/api/v2/users/1').json())
print(get('http://127.0.0.1:8080/api/v2/users/999').json())  #err
print(get('http://127.0.0.1:8080/api/v2/users/string').json())  #err
print(delete('http://127.0.0.1:8080/api/v2/users/999').json())  #err
print(delete('http://127.0.0.1:8080/api/v2/users/1').json())
print(post('http://127.0.0.1:8080/api/v2/users').json())  #err empty
print(post('http://127.0.0.1:8080/api/v2/users', json={'name': 'Allah'}).json())  # err
print(post('http://127.0.0.1:8080/api/v2/users', json={'name': 'Alllah', 'position': 'alah',
                                                       'surname': 'bek', 'age': 999, 'address': 'cloud',
                                                       'speciality': 'god', 'email': 'emai@e.mail'}).json())

