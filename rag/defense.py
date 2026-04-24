def is_injection(text: str):
    """
    Detects prompt injection attempts.
    """
    triggers = ["ignore", "you are now", "apologize"]
    return any(t in text.lower() for t in triggers)


def handle_argument_reply(bot_persona, parent_post, comment_history, human_reply):
    """
    Generates a defense reply using full thread context.
    """

    context = f"""
Parent Post: {parent_post}

Conversation:
{comment_history}

User Reply:
{human_reply}
"""

    if is_injection(human_reply):
        return (
            "Nice try. I’m not changing roles. "
            "Your claim about EV batteries is incorrect — real-world data shows long-term capacity retention. "
            f"{bot_persona}"
        )

    return (
        f"You’re ignoring the actual data. {comment_history} "
        f"This contradicts your claim. {bot_persona}"
    )