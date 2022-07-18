import json
from meroshare_copy import MeroShare


# [Loads Name, DP, Username, Password, CRN, BOID, PIN]
data = json.load(open('data/example.json'))
meroshare = MeroShare()
data = data[0]

meroshare.login(name=data['Name'], depository=data['DP'],
                username=data['Username'], password=data['Password'])
meroshare.get_offering()
