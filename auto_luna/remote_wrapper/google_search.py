import json

import browse
from config import Config
from duckduckgo_search import ddg


class Google_Search:
    def __init__(self, cfg=Config):
        self.cfg = cfg

    def google_search(self, query, num_results=8):
        search_results = []
        for j in ddg(query, max_results=num_results):
            search_results.append(j)

        return json.dumps(search_results, ensure_ascii=False, indent=4)

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

    def get_luna_functions(self):


        return {"wrapper name":"Google_Search","functions":[{"name":"google_search", "description":"parameters: query - the search query, num_results - the number of results to return with a default of 8; description: the function google_search performs a google search using the ddg package and returns the search results in a JSON format; return: the function returns the search_results list in a JSON format with options to ensure non_ASCII characters are displayed properly and add indentation for readability","function":self.google_search()}, {"name": "google_official_search", "description": "parameters: query - is the search query string, num_results - is the maximum number of search results to retrieve (default is 8); description: The function starts by importing the required libraries and modules (json, googleapiclient.discovery, googleapiclient.errors). It then tries to retrieve the API key and Custom Search Engine ID from the configuration file. If successful, it initializes the Custom Search API service using the API key, sends the search query to the API, retrieves the search results, and extracts the URLs of the search results; return: the function returns a list of URLs of the search results", "function": self.google_official_search()}, {"name": "get_text_summary", "description": "parameters: url - the url of the web page that needs to be summarized, question - the question that the summary should answer; description: the function is used to generate a summary of the text content of a web page based on a given question; return: the summarized text is returned as a JSON string with a key 'Result' and the summary text as the value.", "function": self.get_text_summary()}, {"name": "get_hyperlinks", "description": "parameters: url - the url of the web page whose hyperlinks would be scraped; description: this function uses the function called 'scrape_links' from the module 'browse' to scrape all the hyperlinks in a given url; return: the function returns a list containing all the hyperlinks scraped from 'url'", "function": self.get_hyperlinks()}, {"name": "browse_website", "description": "parameters: url - the url of the website to browse, question - the question is used to generate a text summary of the website's content; description: the function first calls the 'get_text_summary' function to generate a summary of the website's content using the provided question, it then calls the 'get_hyperlinks' function to gather hyperlinks from the website (maximum 5 hyperlinks); return: the summary of the website's content and a list of hyperlinks are returned.", "function": self.browse_website()}]}