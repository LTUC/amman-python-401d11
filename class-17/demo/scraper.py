import requests
from  bs4 import BeautifulSoup
import json


URL = 'https://www.reddit.com/'
page = requests.get(URL)
# print(page.content)

soup = BeautifulSoup(page.content,'html.parser')
# print(soup)
all_posts = soup.find_all('div', class_="_1poyrkZ7g36PawDueRza-J")
# # print(all_posts)
# all_cleaned_obj=[]
# for post in all_posts:

#     title = post.find('h3', class_="_eYtD2XCVieq6emjKBH3m").text.strip()
#     # print(title)
#     comments = post.find('span', class_="FHCV02u6Cp2zYL0fhQPsO").text
#     # print(comments)

#     likes = post.find('div', class_="_1rZYMD_4xY3gRcSS3p8ODO").text
#     # print(likes)
#     image_url = post.find('img')['src']
#     # print(image_url)


#     cleand_post={
#         "title" :title,
#         "comments" : comments,
#         "likes" : likes,
#         "image_url" : image_url

#     }

    # all_cleaned_obj.append(cleand_post)

### Refactoring 
def clean_scraper(post):
    title = post.find('h3', class_="_eYtD2XCVieq6emjKBH3m").text.strip()
    comments = post.find('span', class_="FHCV02u6Cp2zYL0fhQPsO").text
    likes = post.find('div', class_="_1rZYMD_4xY3gRcSS3p8ODO").text
    image_url = post.find('img')['src']

    return {
        "title" :title,
        "comments" : comments,
        "likes" : likes,
        "image_url" : image_url

    }

#list comprehension
cleand_posts = [clean_scraper(post) for post in all_posts]

# print(cleand_posts)

data = json.dumps(cleand_posts)
with open ('result.json','w') as file:
    file.write(data)
    
    