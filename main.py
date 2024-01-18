import requests
from collections import Counter
from html.parser import HTMLParser

class HTMLStructureParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.structure = []
        self.current_tag = None
        self.common_structure = None
        self.opening_tags = []

    def handle_starttag(self, tag, attrs):
        self.structure.append(tag)
        self.current_tag = tag
        self.opening_tags.append(self.get_starttag_text())

    def handle_endtag(self, tag):
        self.structure.append(f"/{tag}")

    def find_most_common_structure(self):
        # Find the most common structure
        self.common_structure, _ = Counter(self.structure).most_common(1)[0]

        # Find the opening tag corresponding to the most common structure
        common_opening_tags = [tag for tag in self.opening_tags if tag.startswith(self.common_structure)]
        common_opening_tag = common_opening_tags[0] if common_opening_tags else None

        return common_opening_tag

def find_repeating_structure(url):
    try:
        # Send an HTTP request and get the HTML content
        response = requests.get(url)
        html_content = response.text

        # Use a custom HTML parser to extract the structure
        parser = HTMLStructureParser()
        parser.feed(html_content)
        common_opening_tag = parser.find_most_common_structure()

        return common_opening_tag

    except Exception as e:
        print(f"Error finding repeating structure on {url}: {str(e)}")
        return None

# Example usage
url_to_scrape = 'https://www.boohoo.com/womens/tops'
repeating_structure = find_repeating_structure(url_to_scrape)

if repeating_structure:
    print(f"Repeating structure found on {url_to_scrape}:\n{repeating_structure}")
else:
    print(f"No repeating structure found on {url_to_scrape}")