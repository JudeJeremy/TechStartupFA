import smtplib
import csv
import ast
def read_csv_to_dict(file_path):
    full_group = []

    with open(file_path, mode='r', newline='') as file:
        csv_reader = csv.DictReader(file,delimiter=",")
        
        for row in csv_reader:
            # Convert the 'friends' field from a string to a list
            if 'friends' in row and row['friends']:
                row['friends'] = ast.literal_eval(row['friends'])

            # Convert the 'allergies' field to None if it is 'None'
            if 'allergies' in row and row['allergies'] == 'None':
                row['allergies'] = None

            full_group.append(row)

    return full_group

def calculate_total_satisfaction(profiles):
    members = []
    for i in profiles:
        if i == 0:
            pass
        else:
            members.append(i["name"])
    for profile in profiles:
        satisfaction = 0
        friends_list = profile.get('friends', [])
        for friend in friends_list:
            if friend in members:
                satisfaction += 1
            num_sat = satisfaction
        satisfaction = round(((satisfaction / len(members))*100),2)
        profile['total_satisfaction'] = f"{satisfaction}" + "%" + f" sat num: {num_sat}"
    return profiles

def group_people(profiles, num_groups):
    # Sort profiles by total_satisfaction in descending order
    sorted_profiles = sorted(profiles, key=lambda x: x['total_satisfaction'], reverse=True)
    
    # Initialize empty groups
    groups = [[] for _ in range(num_groups)]
    
    # Distribute people into groups
    for i, profile in enumerate(sorted_profiles):
        groups[i % num_groups].append(profile)
    
    return groups

def calculate_group_satisfaction(groups):
    for group in groups:
        group_satisfaction = 0
        for person in group:
            friends_list = person.get('friends', [])
            for friend in friends_list:
                # Check if the friend is in the same group
                if any(friend in p['name'] for p in group):
                    group_satisfaction += 1
        for person in group:
            person['group_satisfaction'] = group_satisfaction
    return groups      

# Example usage
file_path = 'temp.csv'
whole_group = read_csv_to_dict(file_path)
whole_group = calculate_total_satisfaction(whole_group)
num_groups = 3  # Example: Split into 3 groups
groups = group_people(whole_group, num_groups)
groups = calculate_group_satisfaction(groups)

# for group in groups:
#     for person in group:
#         print(person)
print(groups)
group_ex = []
i = 0
while i < len(groups[0]):
    group_ex.append(groups[0][i]['name'])
    print(group_ex)
    i += 1