from requests import get, post, delete

print(get('http://localhost:8080/api/jobs').json())

print(get('http://localhost:8080/api/jobs/1').json())

print(get('http://localhost:8080/api/jobs/q').json())

print(get('http://localhost:8080/api/jobs/999').json())
