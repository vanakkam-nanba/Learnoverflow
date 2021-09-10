from selenium import webdriver
from bs4 import BeautifulSoup
import json

def playlist_id_from_link(playlist_link):
    return playlist_link.split('=')[-1]

def playlist_scraper_from_link(playlist_id):
    driver = webdriver.Firefox()
    driver.get('https://www.youtube.com/playlist?list={}'.format(playlist_id))
    content = driver.page_source.encode('utf-8').strip()

    soup = BeautifulSoup(content, 'lxml')

    video_count = soup.find('div', id='stats').span.text
    
    playlist_title = soup.find('a', class_='yt-simple-endpoint style-scope yt-formatted-string').text

    playlist_description = soup.find('yt-formatted-string', id='description').text

    playlist_thumbnail = soup.find('img', id='img')['src']

    videos = soup.findAll('a', id='video-title')
    video_urls = []
    video_titles = []

    for video in videos:
        video_urls.append(video['href'])
        video_titles.append(video.text.strip())

    del(videos)

    pubisher_name = soup.find('yt-formatted-string', class_='style-scope ytd-channel-name').a.text

    pubisher_channel_link = soup.find('yt-formatted-string', class_='style-scope ytd-channel-name').a['href']

    videos = soup.findAll('span', class_='style-scope ytd-thumbnail-overlay-time-status-renderer')
    video_durations = []
    for video in videos:
        video_durations.append(video.text.strip())

    del(videos)
    
    playlist_dict = dict()

    playlist_dict['video_count'] = video_count
    playlist_dict['playlist_title'] = playlist_title
    playlist_dict['playlist_description'] = playlist_description
    playlist_dict['playlist_thumbnail'] = playlist_thumbnail
    playlist_dict['video_titles'] = video_titles
    playlist_dict['video_urls'] = video_urls
    playlist_dict['video_durations'] = video_durations
    playlist_dict['pubisher_name'] = pubisher_name
    playlist_dict['pubisher_channel_link'] = pubisher_channel_link

    # with open('data/{} -> {}.json'.format(pubisher_name, playlist_title), 'w') as j:
    #     json.dump(playlist_dict, j, indent=4)

    return playlist_dict


if __name__ == '__main__':
    playlist_scraper_from_link(playlist_id_from_link('https://www.youtube.com/playlist?list=PLzMcBGfZo4-nK0Pyubp7yIG0RdXp6zklu')) 
    playlist_scraper_from_link(playlist_id_from_link('https://www.youtube.com/playlist?list=PLQkwcJG4YTCQcFEPuYGuv54nYai_lwil_'))