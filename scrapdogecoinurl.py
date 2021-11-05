from serpapi import GoogleSearch
import jsonreader

params = {
  "engine": "duckduckgo",
  "q": "dogecoin",
  "api_key": "8c7c399e3c04b2e69beb33e6154a63f6c138fe01278994140d3ea4416b879d04"
}

search = GoogleSearch(params)
results = search.get_dict()
organic_results = results['organic_results']

amounts = [a['link'] for a in organic_results]
print(amounts)