"""
Scripts file -> This file write a script to fetch the data from urls and save data in our database model.
"""
# third party import
import requests
from bs4 import BeautifulSoup
# local import
from .models import Article


def scrape_and_save_article(url):
    # Send an HTTP GET request to the URL
    response = requests.get(url)

    if response.status_code == 200:
        try:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.content, 'html.parser')

            # Extract the Title
            title = soup.find('h1', class_='heading-title').text.strip()

            pubmed_identifier = soup.find('span', class_='identifier pubmed')

            # Extract the PMID
            if pubmed_identifier:
                pmid = pubmed_identifier.find('strong', class_='current-id').text
            else:
                pmid = ""

            # Extract the Abstract
            abstract = soup.find('div', class_='abstract-content').text.strip()
            abstract = abstract.replace('\n', '')

            # Find all text within the <div> with class "abstract"
            abstract_text = soup.find('div', class_='abstract').get_text()

            # Locate the "Keywords:" text within the abstract
            keywords_start = abstract_text.find("Keywords:")
            if keywords_start != -1:
                # Extract the text following "Keywords:" and split it into individual keywords
                keywords_text = abstract_text[keywords_start + len("Keywords:"):].strip()
                keywords = keywords_text.split(';')
                keywords = [keyword.strip() for keyword in keywords]
                keywords = '; '.join(keywords)
            else:
                keywords = ""

            # Extract the Full Text Link
            full_text_link_tag = soup.find('div', class_='full-text-links')
            if full_text_link_tag:
                full_text_link = full_text_link_tag.find('a', class_='link-item')['href']
            else:
                full_text_link = ""

            # Create a new Article instance
            article = Article(
                title=title,
                pmid=pmid,
                abstract=abstract,
                keywords=keywords,
                full_text_link=full_text_link
            )

            # Save the Article instance to the database
            article.save()
            return {"status": "success", "message": "Article saved to the database."}

        except Exception as e:
            return {"status": "error", "message": f'An error occurred: {str(e)}'}

    else:
        return {"status": "error", "message": f'Failed to retrieve the page. Status code: {response.status_code}'}

















