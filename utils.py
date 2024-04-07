

def group_items(lst, n=2):
    return [lst[i:i + n] for i in range(0, len(lst), n)]

def normalize_data(data):
    if 'experience' in data and data['experience']['items'] and len(data['experience']['items']) > 0:
        data['experience']['items'] = group_items(data['experience']['items'], 2)
    
    return data
