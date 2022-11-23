from from_json import read_json as rj
def get_users_from_country(data:dict, country:str)->list:
    """Gets all users from a country from the data
    Args:
        data (dict): The data from the JSON file
        country (str): The country to get users from
    Returns:
        list: A list of users
    """
    a=[]
    for i in data['users']:
        if i['country']==country:
            a.append(i)
    return a 
data = rj('users.json')
print(get_users_from_country(data,'Norway'))