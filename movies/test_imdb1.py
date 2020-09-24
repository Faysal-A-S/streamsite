import requests
from bs4 import BeautifulSoup

movie_url = input("Enter your Movie IMDB URL: ")
page = requests.get(movie_url)

print(page)

soup = BeautifulSoup(page.content, 'html.parser')
# print(soup)
#main_top = soup.find(id='main_top')
# print(main_top)


full_content = soup.find(id="wrapper")
# Main content
title_bar = full_content.find(class_="title_wrapper")
# full title bar content
rating_content = full_content.find(class_='ratings_wrapper')
# all rating info
plot_summary = full_content.find(class_='plot_summary')
#plot_summary = plot_summary_wrapper.find(class_='plot_summary')
# print(plot_summary)
story_line = full_content.find(id='titleStoryLine')
inline_canwrap = story_line.find(class_='inline canwrap')


'''**********************Title and rating ***********************************'''
# Movie title related all info start:
video_title = title_bar.find('h1').get_text()
# show video title  and publish year
video_info = title_bar.find(class_='subtext')
# print(video_info)
# video extra info
video_length = video_info.find('time').get_text()
# show Total Video Length


release_date = video_info.find(title="See more release dates").get_text()
# Movie title related all info end:

'''*******************************Rating ******************************************'''
rating = rating_content.find(itemprop='ratingValue').get_text()
best_rating = rating_content.find(itemprop='bestRating').get_text()
rating_count = rating_content.find(itemprop='ratingCount').get_text()

'''******************************* Description ****************************************'''
# Extra info Movie:
description = inline_canwrap.find('span').get_text()
# Show Description

director_info = plot_summary.find_all(class_='credit_summary_item')[0]
director = director_info.find('a').get_text()
# show director info

writer_info = plot_summary.find_all(class_='credit_summary_item')[1]
writer = writer_info.find('a').get_text()
# show Writter info

stars_info = plot_summary.find_all(class_='credit_summary_item')[2]
#stars = stars_info.find('a').get_text()
length_stars_name = len(stars_info.find_all('a'))
# show stars info


'''********************************Show All extract Info********************************* '''
# all print function goes here
print("Movie Name and Publish Year:", video_title)
print("Total Video Length:", video_length)
length_movie_type = len(video_info.find_all('a'))
#print("test:", length_movie_type)
for i in range(length_movie_type-1):
    # video type
    print("Movie Type:", video_info.find_all('a')[i].get_text())

print("Release Date:", release_date)
print("Rating:", rating)
print("Height Rating:", best_rating)
print("Rating Count:", rating_count)
print("Description:", description)
print("Director:", director)
print("Writer:", writer)

#print("Stars:", length_stars_name)

for j in range(length_stars_name-1):
    print("Stars:", stars_info.find_all('a')[j].get_text())
