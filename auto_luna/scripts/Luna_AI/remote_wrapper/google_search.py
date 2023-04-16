import json

import browse
from config import Config
from duckduckgo_search import ddg


class Google_Search:
    def __init__(self, query, url, question, num_results=8):
        self.cfg = Config() #Vanish - not sure about this one
        self.query = query
        self.num_results = num_results
        self.url = url
        self.question = question


    def google_search(self, query, num_results=8):
        search_results = []
        for j in ddg(query, max_results=num_results):
            search_results.append(j)

        return json.dumps(search_results, ensure_ascii=False, indent=4) #Highly respectable lazy conversion

    def google_official_search(self, query, num_results=8):
        import json

        from googleapiclient.discovery import build
        from googleapiclient.errors import HttpError



        try:
            # Get the Google API key and Custom Search Engine ID from the config file
            api_key = self.cfg.google_api_key #Vanish - put self here
            custom_search_engine_id = self.cfg.custom_search_engine_id #Vanish - put self here

            # Initialize the Custom Search API service
            service = build("customsearch", "v1", developerKey=api_key)
            
            # Send the search query and retrieve the results
            result = service.cse().list(q=query, cx=custom_search_engine_id, num=num_results).execute()

            # Extract the search result items from the response
            search_results = result.get("items", [])
            
            # Create a list of only the URLs from the search results
            search_results_links = [item["link"] for item in search_results]

        except HttpError as e:
            # Handle errors in the API call
            error_details = json.loads(e.content.decode())
            
            # Check if the error is related to an invalid or missing API key
            if error_details.get("error", {}).get("code") == 403 and "invalid API key" in error_details.get("error", {}).get("message", ""):
                return "Error: The provided Google API key is invalid or missing."
            else:
                return f"Error: {e}"

        # Return the list of search result URLs
        return search_results_links



    def get_text_summary(self, url, question):
        text = browse.scrape_text(url)
        summary = browse.summarize_text(text, question)
        return """ "Result" : """ + summary

    def get_hyperlinks(self, url):
        link_list = browse.scrape_links(url)
        return link_list

        
    def browse_website(self, url, question):
        summary = self.get_text_summary(url, question)
        links = self.get_hyperlinks(url)

        # Limit links to 5
        if len(links) > 5:
            links = links[:5]

        result = f"""Website Content Summary: {summary}\n\nLinks: {links}"""

        return result