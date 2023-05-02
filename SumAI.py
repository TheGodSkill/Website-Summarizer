import requests
from sumy.parsers.html import HtmlParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.utils import get_stop_words
import nltk

nltk.download('punkt')

# Define a function to summarize a website
def summarize_website(url):
    # Fetch the website content
    response = requests.get(url)
    html = response.content.decode('utf-8')

    # Parse the HTML content
    parser = HtmlParser.from_string(html, url, Tokenizer('english'))

    # Initialize the LSA Summarizer and get the stop words
    summarizer = LsaSummarizer()
    summarizer.stop_words = get_stop_words('english')

    # Summarize the content and join the sentences
    summary = []
    for sentence in summarizer(parser.document, 3):  # 3 is the number of sentences to summarize
        summary.append(str(sentence))
    return '\n'.join(summary)

# Get the website URL from the user
url = input("Enter the URL of the website to summarize: ")

# Summarize the website and print the result
summary = summarize_website(url)
print(summary)

# Ask the user if they want to save the summary to a file
save_file = input("Do you want to save the summary to a file? (y/n) ")

if save_file.lower() == 'y':
    # Create a file with the name of the website
    filename = url.replace("http://", "").replace("https://", "").replace(".", "_").replace("/", "") + ".txt"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(summary)
    print(f"The summary has been saved to {filename}.")
else:
    print("The summary has not been saved.")
