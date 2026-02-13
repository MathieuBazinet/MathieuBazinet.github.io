import requests
import bibtexparser
with open("./files/my_bibtex.txt", "r") as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

list_of_paper_ids = [entry['ID'] for entry in bib_database.entries]

for paperId in list_of_paper_ids:
    url = f"http://api.semanticscholar.org/graph/v1/paper/{paperId}"

    query_params = {"fields": "title,year,abstract,citationCount,authors"}
    response = requests.get(url, params=query_params)

    if response.status_code == 200:
        response_data = response.json()
        print(response_data['title'], response_data['citationCount'])
    else:
        print(f"Error with code :{response.status_code}")

