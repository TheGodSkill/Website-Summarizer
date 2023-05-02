import requests
from sumy.parsers.html import HtmlParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.utils import get_stop_words
import nltk

nltk.download('punkt')


def summarize_website(url):

    response = requests.get(url)
    html = response.content.decode('utf-8')


    parser = HtmlParser.from_string(html, url, Tokenizer('english'))  # Language


    summarizer = LsaSummarizer()
    summarizer.stop_words = get_stop_words('english')


    summary = []
    for sentence in summarizer(parser.document, 3):  # 3 is the number of sentences to summarize
        summary.append(str(sentence))
    return '\n'.join(summary)


url = input("Enter the URL of the website to summarize: ")


summary = summarize_website(url)
print(summary)


save_file = input("Do you want to save the summary to a file? (y/n) ")

if save_file.lower() == 'y':

    filename = url.replace("http://", "").replace("https://", "").replace(".", "_").replace("/", "") + ".txt"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(summary)
    print(f"The summary has been saved to {filename}.")
else:
    print("The summary has not been saved.")
