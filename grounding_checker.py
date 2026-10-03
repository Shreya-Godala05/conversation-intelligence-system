import os
import json

from dotenv import load_dotenv
from google import genai


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found.")

client = genai.Client(api_key=api_key)


def check_grounding(conversation, suggested_action):
    """
    Check whether the suggested action is supported
    by the information explicitly provided in the conversation.
    """

    prompt = f"""
You are evaluating an AI-generated customer support recommendation.

CUSTOMER CONVERSATION:
{conversation}

SUGGESTED NEXT ACTION:
{suggested_action}

Determine whether the suggested action is grounded in the
information explicitly provided by the customer.

Return ONLY valid JSON:

{{
    "grounded": true,
    "reason": ""
}}

IMPORTANT RULES:

1. The recommendation must be supported by facts in the conversation.

2. Do NOT assume that the support team has capabilities,
tools, permissions, systems, or access that were not mentioned.

3. If the recommendation proposes a specific operational action
that requires an unstated capability, mark it as grounded = false.

4. General advice such as "investigate the issue" or
"ask the customer for more information" can be grounded
when it follows directly from the conversation.

5. A recommendation can address the customer's problem without
being grounded if it assumes an unstated system capability.

6. Do not require the exact wording of the recommendation
to appear in the conversation.

7. Keep the reason short and explain the specific unsupported
assumption when grounded = false.
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    response_text = response.text.strip()

    if response_text.startswith("```"):
        response_text = response_text.replace("```json", "")
        response_text = response_text.replace("```", "")
        response_text = response_text.strip()

    try:
        result = json.loads(response_text)
    except json.JSONDecodeError:
        raise ValueError("Grounding checker returned invalid JSON.")

    if "grounded" not in result:
        raise ValueError("Grounding checker response is missing 'grounded'.")

    if "reason" not in result:
        result["reason"] = ""

    return result
