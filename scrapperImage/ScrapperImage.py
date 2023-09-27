
# import os
# import urllib.request
# import requests
# from bs4 import BeautifulSoup as bs

# class ScrapperImage:
    
#     def __init__(self, search_term, download_folder='./static'):
#         self.search_term = search_term
#         self.download_folder = download_folder
       

#     def create_image_url(self):
#         search_term = '+'.join(self.search_term.split())
#         web_url = f"https://unsplash.com/s/photos/{search_term}"
#         return web_url
    
#     def scrap_html_data(self, url):
#         try:
#             request = urllib.request.Request(url, headers=self.header)
#             response = urllib.request.urlopen(request)
#             responseData = response.read()
#             html = bs(responseData, 'html.parser')
#             return html
#         except Exception as e:
#             print(f"Error fetching HTML: {e}")
#             return None
    
#     def get_image_url_list(self, raw_html):
#         img_tags = raw_html.find_all("img")
#         imageUrlList = [img["srcset"] for img in img_tags if img.get("srcset")]
#         return imageUrlList
    
#     def download_images_from_url(self, image_url_list):
#         try:
#             os.makedirs(self.download_folder, exist_ok=True)
#             image_counter = 0

#             for img in image_url_list:
#                 try:
#                     urllib.request.urlretrieve(img, os.path.join(self.download_folder, f"{self.search_term}_{image_counter}.jpg"))
#                     print(f"Downloaded image {image_counter}")
#                     image_counter += 1
#                 except Exception as e:
#                     print(f"Image download failed: {e}")
#         except Exception as e:
#             print(f"Error creating download folder: {e}")

# def main():
#     search_term = input("Enter the search term: ")
#     scraper = ScrapperImage(search_term)

#     url = scraper.create_image_url()
#     raw_html = scraper.scrap_html_data(url)

#     if raw_html:
#         image_url_list = scraper.get_image_url_list(raw_html)
#         if image_url_list:
#             scraper.download_images_from_url(image_url_list)
#         else:
#             print("No image URLs found in the HTML.")
#     else:
#         print("Failed to fetch HTML content.")

# if __name__ == "__main__":
#     main()



from bs4 import BeautifulSoup as bs
import os
import json
import urllib.request
import urllib.parse
import urllib.error
from urllib.request import urlretrieve
import requests

class ScrapperImage:
    
    ## Create  Image URl
    def createImageUrl(searchterm):
        searchterm=searchterm.split()
        searchterm="+".join(searchterm)
        web_url="https://unsplash.com/s/photos/" + searchterm
        return web_url
    
    
    # get Raw HTML
    def scrap_html_data(url,header):
        request=urllib.request.Request(url,headers=header)
        response = urllib.request.urlopen(request)
        responseData = response.read()
        html = bs(responseData, 'html.parser')
        return html
    
    # contains the link for Large original images, type of  image
    def getimageUrlList(rawHtml):
        imageUrlList = []
        
        #for a in rawHtml.find_all("div", {"class": "rg_meta"}):
        #    link, imageExtension = json.loads(a.text)["ou"], json.loads(a.text)["ity"]
        #    imageUrlList.append((link, imageExtension))
        
        img_tags = rawHtml.find_all("img")
        imageUrlList = [img["src"] for img in img_tags if img.get("src")]
        
        #scripts = rawHtml.find_all("script", type="application/ld+json")
        #for script in scripts:
        #    try:
                # Extract JSON data from the script tag
          #       data = json.loads(script.string)
    
                # Find image URLs in the JSON data
        #        if "@type" in data and data["@type"] == "ImageObject" and "url" in data:
        #            image_url = data["url"]
    
                    # Append the image URL to the list
        #            imageUrlList.append(image_url)
        #    except json.JSONDecodeError:
        #        pass
    
        #query = f'site:{url}'
        #api_key = 'AIzaSyDLa6fAUbjv-IrGzZ9Hwer_NgB4vzZsD5M'
        #cx = '6009f1e09d703458d'  

        # Set the API endpoint URL
        #url = f"https://www.googleapis.com/customsearch/v1?q={query}&cx={cx}&searchType=image&key={api_key}"

        #try:
            # Send a GET request to the API endpoint
        #    response = requests.get(url)
        #    response.raise_for_status()
    
            # Parse the JSON response
        #    data = response.json()
    
            # Extract image URLs from the JSON response
        #    imageUrlList = [item['link'] for item in data.get('items', [])]
    
        #except requests.exceptions.RequestException as e:
        #    print(f"Error: {e}")


        print("there are total", len(imageUrlList), "images")
        return imageUrlList
    
    def downloadImagesFromURL(imageUrlList,image_name, header):
        masterListOfImages = []
        count=0
        ###print images
        imageFiles = []
        imageTypes = []
        image_counter=0
        for i, img in enumerate(imageUrlList):
            try:
                if (count > 5):
                    break
                else:
                    count = count + 1
                req = urllib.request.Request(img, headers=header)
                try:
                    urllib.request.urlretrieve(img,"./static/"+image_name+str(image_counter)+".jpg")
                    image_counter=image_counter+1
                except Exception as e:
                    print("Image write failed:  ",e)
                    image_counter = image_counter + 1
                respData = urllib.request.urlopen(req)
                raw_img = respData.read()
                # soup = bs(respData, 'html.parser')

                imageFiles.append(raw_img)
                

            except Exception as e:
                print("could not load : " + img)
                print(e)
                count = count + 1
        masterListOfImages.append(imageFiles)


        return masterListOfImages
    
    def delete_downloaded_images(self,list_of_images):
        for self.image in list_of_images:
            try:
                os.remove("./static/"+self.image)
            except Exception as e:
                print('error in deleting:  ',e)
        return 0
    
   
    
    
    
    