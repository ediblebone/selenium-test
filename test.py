from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from searchbyimage import searchbyimage
from compare import compareImage
import json

# read configs from file
config_file_path = './config.json'

try:
    with open(config_file_path, 'r', encoding='utf-8') as file:
        config_data = json.load(file)
        visitResult = config_data.get('VISIT_RESULT', '1')  # default value is '1'
except FileNotFoundError:
    print(f"error：file {config_file_path} was not found!")
except json.JSONDecodeError:
    print(f"error could not decode {config_file_path}'s data。")
except Exception as e:
    print(f"there is an error: {e}")

# initialize webdriver
chrome_options = Options()
chrome_options.binary_location = '/Users/jackxia/Downloads/chrome-mac-x64/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing'
driver = webdriver.Chrome(options=chrome_options)

# initialize lcoal path and searched image name
localPath = '/Users/jackxia/picture/'
image = 'cat'

# call method to search image
screenshot = searchbyimage(visitResult, localPath, image,driver)

# comparing screenshot and image, then get the similar value
simi_value = compareImage(localPath + image + '.png', screenshot)

# validate if there is relations
if simi_value >= 0.6:
    print("The saved picture similar with original image!")
else:
    print("There is no connections between saved picture and original image!")