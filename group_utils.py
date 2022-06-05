import json

filename = "Data/groups.json"

def add_permission(group, permission):
    data = read_json()
    data['Groups'][group]['Permissions'].append(permission)
    write_json(data)

def remove_permission(group, permission):
    data = read_json()
    data['Groups'][group]['Permissions'].remove(permission)
    write_json(data)

def read_permissions(group):
    data = read_json()
    return data['Groups'][group]['Permissions']

def read_json():
    with open(filename, "r") as jsonfile:
        return json.load(jsonfile)

def write_json(data):
    with open(filename, "w") as jsonfile:
        json.dump(data, jsonfile)
    return

def has_permission(user, permission):
    for group in get_groups():
        if in_group(user, group):
            for perm in group_permissions(group):
                if perm == permission:
                    return True
    return False

def create_group(group):
    data = read_json()
    data['Groups'][group]={"Permissions": [], "Users": []}
    write_json(data)

def join_group(group, user):
    data = read_json()
    data['Groups'][group]['Users'].append(user)
    write_json(data)

def leave_group(group, user):
    data = read_json()
    data['Groups'][group]['Users'].remove(user)
    write_json(data)

def remove_group(group):
    data = read_json()
    del data['Groups'][group]
    write_json(data)

def in_group(user, group):
    users = read_json()['Groups'][group]['Users']
    if users.count(user) > 0:
        return True
    else:
        return False

def group_permissions(group):
    permissions = read_json()['Groups'][group]['Permissions']
    return permissions

def get_groups():
    group_list = []
    groups = read_json()['Groups']
    for group in groups:
        group_list.append(group)
    return group_list