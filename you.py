# To install: pip install tavily-python
from tavily import TavilyClient
# client = TavilyClient("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")
# response = client.search(
#     query="Who is ZHudi"
# )
# print(response.keys())

def web_search(
        query:str
    ):
    client = TavilyClient("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")
    response = client.search(
        query=query
    )
    if 'results' not in response.keys():
        if self.filter_date is not None:
                raise Exception(
                    f"No results found for query: '{query}' with filtering on date={self.filter_date}. Use a less restrictive query or do not filter on year."
                )
        else:
                raise Exception(
                    f"No results found for query: '{query}'. Use a less restrictive query."
                )


    web_snippets={}
    if 'results' in response.keys():
        for idx,page in enumerate(response['results']):
            redacted_version = {
                    "title": page["title"],
                    "url": page["url"],
                }
            if "date" in page:
                    redacted_version["date"] = page["date"]

            if "source" in page:
                    redacted_version["source"] = page["source"]

            if "content" in page:
                    redacted_version["snippet"] = page["content"]
            
            if "score" in page:
                  
                    redacted_version['score'] = page['score']

            if "snippet_highlighted_words" in page:
                    redacted_version["snippet_highlighted_words"] = list(
                        set(page["snippet_highlighted_words"])
                    )

            web_snippets[idx] = redacted_version
        return web_snippets


    
web_snippets = web_search('recent advances direct speech-to-text translation')
print(web_snippets)