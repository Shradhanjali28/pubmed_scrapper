# 🏥 PubMed Scraper

A Python-based command-line tool to fetch research papers from PubMed, extract details about non-academic authors, and save results to a CSV file.

## 📂 Project Structure

```
pubmed_scraper/
│\── pubmed_scraper/         # Python module
│   ├── __init__.py         # Module initialization
│   ├── fetch_pubmed.py     # Contains functions to fetch and process PubMed data
│\── cli.py                  # Command-line script to use the module
│\── setup.py                # Packaging configuration for PyPI
│\── requirements.txt        # List of dependencies
│\── README.md               # Project documentation
│\── dist/                   # Distribution files for PyPI
│\── tests/                  # Unit tests
```

---

## 🛠️ **Installation and Setup**

### **1️⃣ Install Dependencies**
Make sure you have Python **3.7+** installed.  
Then, install required dependencies using:

```bash
pip install -r requirements.txt
```

---

### **2️⃣ Install from TestPyPI (Optional)**
If you uploaded the package to **TestPyPI**, install it using:

```bash
pip install --index-url https://test.pypi.org/simple/ --no-deps pubmed_scraper
```

---

## 🚀 **Usage**

### **Command-line Execution**
To search for **PubMed** research papers, run:

```bash
python cli.py "COVID-19 vaccine" -f results.csv
```
- Replace `"COVID-19 vaccine"` with your search term.
- The results will be saved in `results.csv`.

**Debug mode:**
```bash
python cli.py "AI in healthcare" -f output.csv -d
```
This will display additional logs.

---

## 🔍 **How It Works**
1. **Fetch Paper IDs** → Searches PubMed for relevant papers.
2. **Extract Details** → Retrieves metadata (authors, affiliations, DOI).
3. **Identify Non-Academic Authors** → Uses a heuristic to flag corporate affiliations.
4. **Save Results** → Outputs extracted data into a structured CSV file.

---

## 📚 **Tools & Libraries Used**
- **Requests** ([Docs](https://docs.python-requests.org/)) – Fetches data from the PubMed API.
- **argparse** ([Docs](https://docs.python.org/3/library/argparse.html)) – Handles command-line arguments.
- **re (Regex)** ([Docs](https://docs.python.org/3/library/re.html)) – Extracts author emails from full-text sources.
- **csv** ([Docs](https://docs.python.org/3/library/csv.html)) – Saves extracted data into a CSV file.

---

## 🛠 **Development & Contribution**
### 🧪 **Run Tests**
If you have `tests/` written, run:
```bash
pytest tests/
```

### 🔧 **Contribute**
1. Fork the repo.
2. Clone your fork:
   ```bash
   git clone https://github.com/shradhanjali28/pubmed_scraper.git
   ```
3. Create a feature branch:
   ```bash
   git checkout -b new-feature
   ```
4. Commit and push:
   ```bash
   git commit -m "Added new feature"
   git push origin new-feature
   ```
5. Open a pull request!

### ✨ **Author**
Developed by **[Shradhanjali Behera]**  
GitHub: [shradhanjali28](https://github.com/shradhanjali28)  


---

