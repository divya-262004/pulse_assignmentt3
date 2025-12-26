import argparse
import json
from crawler import crawl_site
from extractor import extract_modules

def main(urls):
    all_pages = crawl_site(urls)
    result = extract_modules(all_pages)

    print(json.dumps(result, indent=4))

    with open("sample_output.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=4)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Module Extraction AI Agent")
    parser.add_argument("--urls", nargs="+", required=True, help="Documentation URLs")
    args = parser.parse_args()

    main(args.urls)
