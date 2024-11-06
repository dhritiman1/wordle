import requests
from bs4 import BeautifulSoup
import os

url = "https://www.mit.edu/~ecprice/wordlist.10000"

response = requests.get(url)
if response.status_code != 200:
    print("Failed to retrieve the webpage.")
    exit()

soup = BeautifulSoup(response.text, 'html.parser')
words = soup.get_text().splitlines()

five_letter_words = [word.lower() for word in words if len(word) == 5]

output_file_path = os.path.join(os.getcwd(), 'five_letter_words.txt')

with open(output_file_path, "w") as f:
    f.write(",".join(five_letter_words))

print(f"Successfully saved {len(five_letter_words)} 5-letter words to five_letter_words.txt.")
