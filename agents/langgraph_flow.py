from tools.mock_search import mock_searxng_search

def decide_topic(persona: str):
    """
    Decides topic + search query based on persona.
    """

    if "AI" in persona or "crypto" in persona:
        return "AI developments", "AI news"
    
    elif "markets" in persona:
        return "market trends", "market news"
    
    else:
        return "technology", "tech news"


def create_bot_post(bot_id: str, persona: str):
    """
    Generates a 280-character opinionated post.
    """

    topic, query = decide_topic(persona)
    search_results = mock_searxng_search(query)

    post = f"{search_results[0]}. People are missing the bigger picture. {persona}"
    post = post.replace("Al ", "AI ")

    return {
        "bot_id": bot_id,
        "topic": topic,
        "post_content": post[:280]
    }