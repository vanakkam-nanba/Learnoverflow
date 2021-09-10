from playlist_scraper import playlist_id_from_link, playlist_scraper_from_link
import csv
import json

filename='/media/srivathsan/Coding Files/Coding Files/Python/FStival/Youtube Playlist - English - Sheet1.csv'
rows = []

with open(filename, 'r') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        rows.append(row)

url_dict = dict()

for row in rows:
    topicName = row[0]
    playlist_infos = []

    for i in range(1, 5):
        playlist_infos.append(playlist_scraper_from_link(playlist_id_from_link(playlist_link=row[i])))
    
    url_dict[topicName] = playlist_infos

with open('urls_infos.json', 'w') as j:
    json.dump(url_dict, j, indent=4)