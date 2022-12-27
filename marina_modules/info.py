
import json


def get_info(host):

    headers = {
        'User-Agent': 'MARINA 2.0'
    }

    shodan_data = requests.get("http://192.168.0.3/marina-shodan.php?ip={}".format(host), headers=headers)

    return json.loads(shodan_data.text)

    
