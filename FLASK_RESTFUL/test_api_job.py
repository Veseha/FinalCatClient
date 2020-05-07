from requests import get, post, delete

print(get('http://127.0.0.1:8080/api/v2/jobs').json())
print(get('http://127.0.0.1:8080/api/v2/jobs/1').json())
print(get('http://127.0.0.1:8080/api/v2/jobs/999').json())  #err
print(get('http://127.0.0.1:8080/api/v2/jobs/string').json())  # err
print(delete('http://127.0.0.1:8080/api/v2/jobs/999').json())  # err
print(delete('http://127.0.0.1:8080/api/v2/jobs/11').json())
print(post('http://127.0.0.1:8080/api/v2/jobs').json())  # err
print(post('http://127.0.0.1:8080/api/v2/jobs', json={'job': 'catclient'}).json())  # не все поля
print(post('http://127.0.0.1:8080/api/v2/jobs', json={'job': 'catclient', 'work_size': 264,
                                                      'team_leader': 1, 'collaborators': '2, 3',
                                                      'is_finished': False}).json())

