import requests
import csv
import re
from typing import List, Dict, Any

PUBMED_API_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
PUBMED_SUMMARY_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"

def fetch_pubmed_ids(query: str) -> List[str]:
    """Fetch paper IDs from PubMed based on the query."""
    params = {"db": "pubmed", "term": query, "retmode": "json", "retmax": 10}
    response = requests.get(PUBMED_API_URL, params=params)
    response.raise_for_status()
    data = response.json()
    return data.get("esearchresult", {}).get("idlist", [])

def fetch_paper_details(paper_ids: List[str]) -> List[Dict[str, Any]]:
    """Fetch paper details from PubMed using paper IDs."""
    if not paper_ids:
        return []
    
    params = {"db": "pubmed", "id": ",".join(paper_ids), "retmode": "json"}
    response = requests.get(PUBMED_SUMMARY_URL, params=params)
    response.raise_for_status()
    data = response.json()
    result_data = data.get("result", {})
    
    return [result_data[pid] for pid in paper_ids if pid in result_data]

def is_non_academic(name: str) -> bool:
    """Determine if an author is non-academic based on heuristic keywords."""
    academic_keywords = ["university", "institute", "academy", "research lab"]
    company_keywords = ["Inc.", "Ltd.", "Biotech", "Pharma", "Corporation"]

    if any(word.lower() in name.lower() for word in company_keywords):
        return True
    if any(word.lower() in name.lower() for word in academic_keywords):
        return False
    return True

def fetch_corresponding_email(doi: str) -> str:
    """Fetch the corresponding author's email using the DOI lookup."""
    if not doi:
        return "N/A"
    
    doi_url = f"https://doi.org/{doi}"
    
    try:
        response = requests.get(doi_url, timeout=10, allow_redirects=True)
        response.raise_for_status()

        if "mailto:" in response.text:
            match = re.search(r"mailto:([\w\.-]+@[\w\.-]+)", response.text)
            if match:
                return match.group(1)
    except requests.RequestException:
        return "N/A"

    return "N/A"

def process_papers(papers: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Process the list of papers to extract relevant details."""
    processed_data = []
    
    for paper in papers:
        authors = paper.get("authors", [])
        non_academic_authors = []
        doi = None

        for id_entry in paper.get("articleids", []):
            if id_entry["idtype"] == "doi":
                doi = id_entry["value"]
                break
        
        for author in authors:
            if isinstance(author, dict) and "name" in author:
                author_name = author["name"]
                if is_non_academic(author_name):
                    non_academic_authors.append(author_name)

        if non_academic_authors:
            processed_data.append({
                "PubmedID": paper.get("uid"),
                "Title": paper.get("title", "Unknown"),
                "Publication Date": paper.get("pubdate", "Unknown"),
                "Non-academic Authors": ", ".join(non_academic_authors),
                "Company Affiliations": ", ".join(non_academic_authors),
                "Corresponding Author Email": fetch_corresponding_email(doi) if doi else "N/A"
            })

    return processed_data

def save_to_csv(filename: str, data: List[Dict[str, Any]]):
    """Save results to a CSV file."""
    if not data:
        print("No data to save.")
        return
    
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
