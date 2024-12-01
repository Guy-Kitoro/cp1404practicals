import wikipedia
import warnings
from bs4 import GuessedAtParserWarning

# Suppress BeautifulSoup parser warnings
warnings.filterwarnings("ignore", category=GuessedAtParserWarning)


def main():
    """Interact with the Wikipedia API to fetch page details."""
    while True:
        search = input("Enter page title: ").strip()
        if not search:
            print("Thank you.")
            break
        try:
            # Attempt to fetch the page
            page = wikipedia.page(search)
            print(f"\n{page.title}")
            print(f"{page.summary[:500]}...\n")  # Limit summary length for readability
            print(page.url)
        except wikipedia.PageError:
            print(f"\nPage id \"{search}\" does not match any pages. Try another id!\n")
        except wikipedia.DisambiguationError:
            # Treat disambiguation as page not found
            print(f"\nPage id \"{search}\" does not match any pages. Try another id!\n")


if __name__ == "__main__":
    main()




