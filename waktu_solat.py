import requests
import sys

waktu_solat_api = "https://waktu-solat-api.herokuapp.com/api/v1/prayer_times.json"

response = requests.get(waktu_solat_api)
data = response.json()

# for maklumat in data['data']['negeri'][0]['zon'][0]['waktu_solat']:
#     print(maklumat['time'])

def grab_api():
    waktu_solat_api = "https://waktu-solat-api.herokuapp.com/api/v1/prayer_times.json"
    response = requests.get(waktu_solat_api)
    data = response.json()
    return data

# def filter_results(data, negeri, daerah, waktu):
#     for info in data['data']['negeri']['zon']['waktu_solat']:
#         nama = info['name']
#         waktu = info['time']
#         if info['name'] == waktu_solat_api:
#             print(f'Waktu {nama} adalah pada: {waktu}')

def filter_results(data, waktu):
    for info in data['data']['negeri']['zon']['waktu_solat']:
        waktu = info['time']
        if waktu == "None":
            print(info)
        # elif daerah == NULL:
        #     print(data['data']['negeri'])
        # elif negeri == NULL:
        #     print(data['data'])
        # else: print(data['data'])

# def pilihan(pilih, daerahVar):
#     if pilih == negeri:
#         print("Sila masukkan nama daerah")
#         daerahVar = input()
        
#         print(data['data']['negeri'])


def get_input():
    negeri = sys.argv[1]
    daerah = sys.argv[2]
    waktu  = sys.argv[3]
    # print(f'Negeri: {negeri} Daerah: {daerah} Waktu: {waktu}')
    return str(negeri), str(daerah), str(waktu)

def main():
    # try:
        negeri, daerah, waktu = get_input()
        data = grab_api()
        filter_results()

    # except Exception as e:
    #     print("Tak jadi bro")

main()

'''
###############
# PSEUDO CODE #
###############

- grab_api()
    - ambik API
    - ambik "data" from .JSON
    - release "data"

- get_input()
    - input_1 = Negeri
    - input_2 = Daerah
    - input_3 = Waktu
    - release "Negeri", "Daerah", "Waktu"

- filter_result()
    - ambik data dari "data"
    - "Negeri", "Daerah", "Waktu" 
            - python waktu_solat.py Negeri Daerah Waktu
            - Print Waktu spesifik
    - "Negeri", "Daerah"          
            - python waktu_solat.py Negeri Daerah
            - Print Waktu seluruh "Daerah"
    - "Negeri"                    
            - python waktu_solat.py Negeri
            - "Sila tulis "Daerah"
            - input "Daerah"
            - Print Waktu seluruh "Daerah"
'''