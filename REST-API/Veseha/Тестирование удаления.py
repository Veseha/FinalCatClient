from requests import get, delete

print(delete('http://localhost:5000/api/jobs/1').json())  # ok
print(delete('http://localhost:5000/api/jobs/999').json())  # no jobs
print(delete('http://localhost:5000/api/jobs/what').json())  # what?
print(get('http://localhost:5000/api/jobs').json())