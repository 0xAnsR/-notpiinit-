import requests
from bs4 import BeautifulSoup
from openai import OpenAI

# Your OpenAI API key (use environment variables in production)
OPENAI_API_KEY = "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"

# List of URLs to visit
URLS = [
"https://www.ppsc.gop.pk/(S(oxicsm3utyrfa3nfxn0c3tws))/jobs.aspx"
]

def fetch_page_content(url):
    """Fetch content from the given URL."""
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def extract_text(html_content):
    """Extract readable text from HTML using BeautifulSoup."""
    soup = BeautifulSoup(html_content, "html.parser")
    return soup.get_text(separator="\n", strip=True)

def filter_with_ai(text):
    """Use OpenAI to filter and summarize the text."""
    client = OpenAI(api_key=OPENAI_API_KEY)
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": f"Summarize and filter useful updates from this text:\n{text}"}]
    )
    return completion.choices[0].message.content

def main():
    """Fetch, process, and display updates from all URLs."""
    for url in URLS:
        print(f"\nFetching updates from: {url}")
        html_content = fetch_page_content(url)
        if html_content:
            extracted_text = extract_text(html_content)
            filtered_info = filter_with_ai(extracted_text)
            print("\nFiltered Update:\n", filtered_info)

if __name__ == "__main__":
    main()
