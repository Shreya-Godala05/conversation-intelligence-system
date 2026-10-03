import os
import json
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Get Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found. Check your .env file.")

# Create Gemini client
client = genai.Client(api_key=api_key)


def analyze_conversation(conversation):
    """
    Analyze a customer conversation and return
    structured customer insights.
    """

    prompt = f"""
You are a customer conversation analysis system.

Analyze the customer conversation below.

--- CONVERSATION ---
{conversation}
--- END CONVERSATION ---

Return ONLY valid JSON with exactly these fields:

{{
    "sentiment": "",
    "intent": "",
    "main_issue": "",
    "urgency": "",
    "key_points": [],
    "suggested_next_action": ""
}}

Rules:

1. sentiment MUST be one of:
   "Positive", "Neutral", "Frustrated", "Angry", "Negative"

2. urgency MUST be one of:
   "Low", "Medium", "High"

   Use "Low" when the customer has a general question,
   non-urgent request, or issue without a meaningful immediate impact.

   Use "Medium" when the customer has a real problem that
   requires attention but there is no immediate deadline,
   severe consequence, or repeated failed resolution.

   Examples include:
   - A delayed package without an urgent deadline
   - A duplicate charge that needs investigation
   - A normal refund request
   - A non-critical technical problem

   Use "High" only when there is strong evidence of immediate
   impact or escalation, such as:
   - An explicit immediate deadline
   - Loss of access needed for an important immediate task
   - A serious service disruption
   - Repeated failed attempts to resolve the same problem
   - An explicit cancellation threat connected to an unresolved issue

   Do NOT classify an issue as High solely because money,
   billing, or a refund is involved.

3. intent should describe what the customer is trying to accomplish.

4. main_issue should describe the customer's primary problem.

5. key_points should contain 2-5 important facts explicitly mentioned
   in the conversation.

6. suggested_next_action should be a practical action based only
   on information available in the conversation.

7. Do NOT invent facts.

8. Do NOT claim that an action has already been taken.

9. If information is unclear, use "Unknown".

10. Return JSON only. Do not include markdown or explanations.

Customer conversation:
{conversation}
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    # Get the model's response
    response_text = response.text.strip()

    # Remove markdown code fences if the model happens to add them
    if response_text.startswith("```"):
        response_text = response_text.replace("```json", "")
        response_text = response_text.replace("```", "")
        response_text = response_text.strip()

    # Convert JSON text into a Python dictionary
    try:
        result = json.loads(response_text)
    except json.JSONDecodeError:
        raise ValueError(
            "The model returned an invalid JSON response."
        )

    return result
def validate_result(result):
    """
    Validate the structure and allowed values
    of the LLM response.
    """

    required_fields = [
        "sentiment",
        "intent",
        "main_issue",
        "urgency",
        "key_points",
        "suggested_next_action"
    ]

    # Check that all required fields exist
    missing_fields = [
        field for field in required_fields
        if field not in result
    ]

    if missing_fields:
        return False, f"Missing fields: {missing_fields}"

    # Allowed sentiment values
    allowed_sentiments = {
        "Positive",
        "Neutral",
        "Frustrated",
        "Angry",
        "Negative"
    }

    # Allowed urgency values
    allowed_urgencies = {
        "Low",
        "Medium",
        "High"
    }

    if result["sentiment"] not in allowed_sentiments:
        return False, "Invalid sentiment value."

    if result["urgency"] not in allowed_urgencies:
        return False, "Invalid urgency value."

    # key_points should be a list
    if not isinstance(result["key_points"], list):
        return False, "key_points must be a list."

    # Check that important text fields aren't empty
    text_fields = [
        "intent",
        "main_issue",
        "suggested_next_action"
    ]

    for field in text_fields:
        if not isinstance(result[field], str) or not result[field].strip():
            return False, f"{field} must contain text."

    return True, "Valid result."


if __name__ == "__main__":

    sample_conversation = """
    I have been trying to reset my password since yesterday,
    but I never receive the password reset email.
    I have checked my spam folder twice.
    I need access to my account today because I have an important payment
    that I need to make.
    """

    result = analyze_conversation(sample_conversation)

    print("\n===== CUSTOMER CONVERSATION ANALYSIS =====")
    print(json.dumps(result, indent=4))

    print("\n===== VALIDATION =====")

    is_valid, message = validate_result(result)

    print("Valid:", is_valid)
    print("Message:", message)
