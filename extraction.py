import requests as req
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup

import re 






# Load environment variables from .env file
load_dotenv()

# List of lecture topics
dictionary = [
    "introduction",
    "capabilities",
    "harms-1",
    "harms-2",
    "data",
    "security",
    "legality",
    "modeling",
    "training",
    "parallelism",
    "scaling-laws",
    "selective-architectures",
    "adaptation",
    "environment"
]

base_lecture_url = os.getenv('lecture_url')

# Ensure base_lecture_url is not None
if base_lecture_url:
    for topic in dictionary:
        lecture_url = f"{base_lecture_url}{topic}"
        try:
            # Make the GET request
            res = req.get(lecture_url)

            # Check the response status code
            if res.status_code == 200:
                print(f"Successfully fetched the lecture notes for {topic}.")
                
                # Parse the response text with BeautifulSoup
                soup = BeautifulSoup(res.text, 'html.parser')
                
                # Extract the main content
                content_div = soup.find("div", class_="main-content-wrap")
                if content_div:
                    # Do something with the content, e.g., print or store it
                    print("Done!")
                else:
                    print(f"Could not find the main content for {topic}.")
            else:
                print(f"Failed to fetch the lecture notes for {topic}. Status code: {res.status_code}")
        except req.RequestException as e:
            print(f"An error occurred while fetching the lecture notes for {topic}: {e}")
else:
    print("No URL provided in the environment variable 'lecture_url'.")


def clean_text(content_div):
  """
  This function removes HTML tags from the provided content using regular expressions.

  Args:
      content_div (bs4.element.Tag): The HTML content as a Beautiful Soup Tag object.

  Returns:
      str: The cleaned text without HTML tags.
  """

  # Extract text content from the Tag object
  text_content = content_div.get_text(separator=" ")  # Extract text with spaces as separator

  # Apply regular expression for cleaning
  clean_text = re.sub(r'<.*?>', '', text_content)

  return clean_text

# Example usage (assuming content_div is a Beautiful Soup Tag object)
cleaned_text = clean_text(content_div)