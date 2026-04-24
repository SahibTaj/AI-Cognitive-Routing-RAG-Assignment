def mock_searxng_search(query: str):
    """
    Simulated search tool returning mock headlines.
    """

    if "AI" in query:
        return ["OpenAI releases model that may replace junior developers"]
    
    elif "crypto" in query:
        return ["Bitcoin hits all-time high after ETF approvals"]
    
    elif "market" in query:
        return ["Stock market reacts to interest rate changes"]
    
    return ["Latest developments in technology"]