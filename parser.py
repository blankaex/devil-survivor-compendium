import json

# http://wikinavi.net/dsoc/index.php?%E4%BB%B2%E9%AD%94%2F%E7%A8%AE%E6%97%8F%E5%88%A5
with open('dump', 'r') as dump:
    dics = list()
    for line in dump:
        arr = line.split('|')
        dic = {
            "name": arr[3].strip("''"),
            "race": arr[2],
            "level": int(arr[1]),
            "unique": True if "''" in arr[3] else False,
            "HP": int(arr[4]),
            "MP": int(arr[5]),
            "st": int(arr[6]),
            "ma": int(arr[7]),
            "vi": int(arr[8]),
            "ag": int(arr[9]),
            "phys": arr[10].replace('−', 'ー'),
            "fire": arr[11].replace('−', 'ー'),
            "ice": arr[12].replace('−', 'ー'),
            "elec": arr[13].replace('−', 'ー'),
            "force": arr[14].replace('−', 'ー'),
            "mystic": arr[15].replace('−', 'ー'),
            "commands": [x.replace('−', 'ー') for x in arr[16].split(',')],
            "passives": [x.replace('−', 'ー') for x in arr[17].split(',')],
            "racial": arr[18]
        }
        dics.append(dic)
    with open('demons.json', 'w') as demons:
        json.dump(dics, demons, ensure_ascii=False, indent=4)
