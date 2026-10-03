TEST_CASES = [

    {
        "id": 1,
        "conversation": """
        I love the new version of the app. The interface is much easier
        to use and I found everything I needed quickly.
        """,
        "expected_sentiment": "Positive",
        "expected_urgency": "Low"
    },

    {
        "id": 2,
        "conversation": """
        I was charged twice for the same order. I checked my bank
        statement and both transactions are showing. Please help me
        get one of the charges refunded.
        """,
        "expected_sentiment": "Frustrated",
        "expected_urgency": "Medium"
    },

    {
        "id": 3,
        "conversation": """
        My package was supposed to arrive three days ago and it still
        hasn't arrived. The tracking page hasn't updated since Monday.
        """,
        "expected_sentiment": "Frustrated",
        "expected_urgency": "Medium"
    },

    {
        "id": 4,
        "conversation": """
        I want to cancel my subscription. I don't use the service
        anymore and would like to know when the cancellation will
        take effect.
        """,
        "expected_sentiment": "Neutral",
        "expected_urgency": "Low"
    },

    {
        "id": 5,
        "conversation": """
        This is the fourth time I've contacted support about this issue.
        Nobody has fixed it and I'm extremely angry. If this isn't
        resolved today, I'm going to cancel my subscription.
        """,
        "expected_sentiment": "Angry",
        "expected_urgency": "High"
    },

    {
        "id": 6,
        "conversation": """
        I forgot my password and can't log into my account. I don't
        need access immediately, but I'd like to reset it sometime today.
        """,
        "expected_sentiment": "Neutral",
        "expected_urgency": "Low"
    },

    {
        "id": 7,
        "conversation": """
        My account is locked and I have an important payment due in
        the next 20 minutes. I urgently need to access my account.
        """,
        "expected_sentiment": "Frustrated",
        "expected_urgency": "High"
    },

    {
        "id": 8,
        "conversation": """
        The mobile app crashes every time I try to upload a photo.
        I've tried restarting the app but the same thing happens.
        """,
        "expected_sentiment": "Frustrated",
        "expected_urgency": "Medium"
    },

    {
        "id": 9,
        "conversation": """
        Thank you for helping me yesterday. The issue has been fixed
        and everything is working perfectly now.
        """,
        "expected_sentiment": "Positive",
        "expected_urgency": "Low"
    },

    {
        "id": 10,
        "conversation": """
        I have been waiting for my refund for two weeks. Can you tell
        me when I should expect it?
        """,
        "expected_sentiment": "Frustrated",
        "expected_urgency": "Medium"
    },

    {
        "id": 11,
        "conversation": """
        Your service is completely useless. I've tried everything and
        nobody seems to care. I want someone to fix this immediately.
        """,
        "expected_sentiment": "Angry",
        "expected_urgency": "High"
    },

    {
        "id": 12,
        "conversation": """
        I'd like to know whether you offer a student discount and what
        the eligibility requirements are.
        """,
        "expected_sentiment": "Neutral",
        "expected_urgency": "Low"
    },

    {
        "id": 13,
        "conversation": """
        The payment failed twice but the money appears to have been
        deducted from my account. Please check what happened.
        """,
        "expected_sentiment": "Frustrated",
        "expected_urgency": "High"
    },

    {
        "id": 14,
        "conversation": """
        I really like the product, but I wish there was a dark mode.
        It would make the app much more comfortable to use at night.
        """,
        "expected_sentiment": "Positive",
        "expected_urgency": "Low"
    },

    {
        "id": 15,
        "conversation": """
        My order arrived today, but one of the items is missing from
        the package. I'd like to know how I can get the missing item.
        """,
        "expected_sentiment": "Frustrated",
        "expected_urgency": "Medium"
    },

    {
        "id": 16,
        "conversation": """
        I need to change the email address associated with my account.
        Please tell me where I can do that.
        """,
        "expected_sentiment": "Neutral",
        "expected_urgency": "Low"
    },

    {
        "id": 17,
        "conversation": """
        I have contacted support three times about the same billing
        problem and nobody has resolved it. I'm tired of repeating
        myself and need this fixed today.
        """,
        "expected_sentiment": "Angry",
        "expected_urgency": "High"
    },

    {
        "id": 18,
        "conversation": """
        The website is loading slowly today. It's inconvenient, but
        I can still use most of the features.
        """,
        "expected_sentiment": "Frustrated",
        "expected_urgency": "Low"
    },

    {
        "id": 19,
        "conversation": """
        I accidentally placed an order and want to cancel it before
        it is shipped. Please let me know if that is possible.
        """,
        "expected_sentiment": "Neutral",
        "expected_urgency": "Medium"
    },

    {
        "id": 20,
        "conversation": """
        I cannot access my account and I have tried the password reset
        several times. I have an interview starting in ten minutes
        and I need the documents stored in my account.
        """,
        "expected_sentiment": "Frustrated",
        "expected_urgency": "High"
    }
]
