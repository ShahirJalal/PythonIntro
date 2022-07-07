import sys
import requests

def get_api():
    waktu_solat_api = "https://waktu-solat-api.herokuapp.com/api/v1/prayer_times.json"
    response = requests.get(waktu_solat_api)
    data = response.json()
    return data

def get_input():
    input_negeri = sys.argv[1]
    input_zon    = sys.argv[2]
    input_waktu  = sys.argv[3]
    return input_negeri, input_zon, input_waktu

def data_filter(input_negeri, input_zon, input_waktu, data):
    for arkib in data['data']['negeri']:
        nama1 = arkib['nama']
        if input_negeri == nama1:
            for info in arkib['zon']:
                nama2 = info['nama']
                if input_zon == nama2:
                    for maklumat in info['waktu_solat']:
                        nama3 = maklumat['name']
                        if input_waktu == nama3:
                            print(maklumat)

def main():

    try:
        data = get_api()
        input_negeri, input_zon, input_waktu = get_input()
        data_filter(input_negeri, input_zon, input_waktu, data)

    except Exception as e:
        print("Input salah")

main()