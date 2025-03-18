import argparse
from scraper import fetch_website_content
from indexer import DocumentIndexer
from search import answer_query

def main():
    parser = argparse.ArgumentParser(description="AI Q&A Agent")
    parser.add_argument("--url", required=True, help="Help website URL")
    args = parser.parse_args()

    content = fetch_website_content(args.url)
    if not content:
        print("[-] Failed to retrieve content. Exiting.")
        return

    indexer = DocumentIndexer()
    indexer.index_documents([content])

    print("Ready! Ask your questions:")
    while True:
        query = input("> ")
        if query.lower() in ["exit", "quit"]:
            break
        response = answer_query(query, indexer)
        print("\n[Agent] " + response + "\n")

if __name__ == "__main__":
    main()
