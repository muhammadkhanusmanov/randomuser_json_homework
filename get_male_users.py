from from_json import read_json as rj
def get_male_users(data:dict)->list:
    """Gets all male users from the data
    Args:
        data (dict): The data from the JSON file
    Returns:
        list: A list of users
    """
    a=[]
    for i in data['users']:
        if i['gender']=='male':
            a.append(i)
    return a 
data=rj('users.json')
print(get_male_users(data))
