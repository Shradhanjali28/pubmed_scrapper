import argparse
from pubmed_scraper.fetch_pubmed import fetch_pubmed_ids, fetch_paper_details, process_papers, save_to_csv

def main():
    parser = argparse.ArgumentParser(description="Fetch PubMed research papers with non-academic authors.")
    parser.add_argument("query", type=str, help="Search query for PubMed")
    parser.add_argument("-f", "--file", type=str, help="Output CSV filename", default=None)
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode")
    
    args = parser.parse_args()
    
    paper_ids = fetch_pubmed_ids(args.query)
    if args.debug:
        print(f"Fetched paper IDs: {paper_ids}")
    
    papers = fetch_paper_details(paper_ids)
    processed_data = process_papers(papers)
    
    if args.file:
        save_to_csv(args.file, processed_data)
        print(f"Results saved to {args.file}")
    else:
        print(processed_data)

if __name__ == "__main__":
    main()
