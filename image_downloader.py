from openpyxl import load_workbook as lwb
from google_images_download import google_images_download 
import concurrent.futures

# creating object 
response = google_images_download.googleimagesdownload() 

wb=lwb("List of Dishes based on Cuisines.xlsx")
ws=wb["Final"]
categories=list(a[0].value for a in list(ws["A313:A418"]))
print(categories)
print(len(categories))
 
#global output,limit,cd
output=r"D:\Food_imgs_download\\"
limit=1500
cd=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
def downloadimages(category): 
    # keywords is the search query 
    # format is the image file format 
    # limit is the number of images to be downloaded 
    # print urs is to print the image file url 
    # size is the image size which can 
    # be specified manually ("large, medium, icon") 
    # aspect ratio denotes the height width ratio 
    # of images to download. ("tall, square, wide, panoramic") 
    arguments = {"keywords": category, 
                "format": "jpg", 
                "limit":limit, 
                "print_urls":False, 
                "size": "large",
                "aspect_ratio":"square",
                "output_directory":output,
                "chromedriver":cd,
                "silent_mode":True} 
    try: 
        response.download(arguments) 
     
    # Handling File NotFound Error     
    except FileNotFoundError: 
        arguments = {"keywords":category, 
                    "format": "jpg", 
                    "limit":limit, 
                    "print_urls":False, 
                    "size": "large",
                    "aspect_ratio":"square",
                    "output_directory":output,
                    "chromedriver":cd,
                "silent_mode":True} 
                     
        # Providing arguments for the searched query 
        try: 
            # Downloading the photos based 
            # on the given arguments 
            response.download(arguments) 
        except: 
            pass
 
# Driver Code 
#single threaded
# for category in categories: 
#     downloadimages(category,limit) 
#multithreaded downloading 
with concurrent.futures.ThreadPoolExecutor() as executor:
    for category in zip(categories, executor.map(downloadimages, categories)):
        print()

