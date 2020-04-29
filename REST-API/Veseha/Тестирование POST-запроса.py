from requests import get, post, delete

print(get('http://localhost:8080/api/jobs').json())

print(get('http://localhost:8080/api/jobs/1').json())

print(get('http://localhost:8080/api/jobs/q').json())

print(get('http://localhost:8080/api/jobs/999').json())


print(post('http://localhost:8080/api/jobs',
           json={'id': 399, 'job': 'coding', 'team_leader': 1, 'work_size': 5,
                 'collaborators': '2, 3', 'category': 1, 'is_finished': True}).json())  # стопэ, такого айди нету

print(post('http://localhost:8080/api/jobs',
           json={'id': 3, 'team_leader': 1, 'work_size': 5,
                 'collaborators': '2, 3', 'category': 1, 'is_finished': True}).json())  # чет нехватает

print(post('http://localhost:8080/api/jobs',
           json={'id': 1, 'job': 'coding', 'team_leader': 1, 'work_size': 5,
                 'collaborators': '2, 3', 'category': 1, 'is_finished': True}).json())  # усе четко

print(post('http://localhost:8080/api/jobs',
           json={}).json())  # ну и где?
