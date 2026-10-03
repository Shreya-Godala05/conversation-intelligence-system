# Conversation Intelligence System

An LLM-powered system for analyzing customer conversations and extracting actionable insights.

## Overview

The Conversation Intelligence System is a Python-based AI application that analyzes customer conversations and converts unstructured text into structured customer-support insights.

The system extracts:

- Sentiment
- Customer intent
- Main issue
- Urgency level
- Key points
- Suggested next action

It also validates the generated output and performs a grounding check to identify recommendations that may rely on unsupported assumptions.

## Features

- LLM-powered conversation analysis
- Structured JSON output
- Sentiment classification
- Customer intent extraction
- Main issue identification
- Urgency classification
- Key-point extraction
- Suggested next-action generation
- Output validation
- Recommendation grounding check
- Interactive Streamlit interface
- API key protection using environment variables

## Architecture

```text
Customer Conversation
        |
        v
   Gemini LLM
        |
        v
Structured JSON Analysis
        |
        +------------------+
        |                  |
        v                  v
Output Validation    Grounding Check
        |                  |
        +--------+---------+
                 |
                 v
          Streamlit UI
Tech Stack
- Python
- Google Gemini API
- Streamlit
- python-dotenv
- Git / GitHub
Project Structure
conversation-intelligence-system/
│
├── analyzer.py
├── app.py
├── evaluator.py
├── grounding_checker.py
├── test_cases.py
├── requirements.txt
├── .gitignore
└── README.md

How It Works
1. Conversation Analysis
A customer conversation is sent to the Gemini model with instructions to return structured JSON.
The model extracts:
Sentiment
Intent
Main Issue
Urgency
Key Points
Suggested Next Action

2. Output Validation
The generated response is parsed as JSON and checked for:
- Required fields
- Valid sentiment values
- Valid urgency values
- Correct key-point structure
- Non-empty required text fields
3. Recommendation Grounding
The suggested next action is separately evaluated against the original conversation.
The grounding checker is designed to flag recommendations that assume capabilities, tools, permissions, or information that were not established in the conversation.
For example, if a customer says they cannot receive a password reset email, a recommendation to manually reset the password may require support capabilities that were never mentioned.
Example
Customer Conversation
I have been trying to reset my password since yesterday,
but I never receive the password reset email.
I have checked my spam folder twice.
I need access to my account today because I have an important payment.

Extracted Insights
Sentiment: Frustrated

Urgency: High

Intent:
Reset password and access account

Main Issue:
Not receiving the password reset email

The system also extracts key points and generates a suggested next action.
The grounding layer then evaluates whether that recommendation is actually supported by the conversation.
Running the Project
1. Clone the repository
git clone https://github.com/Shreya-Godala05/conversation-intelligence-system.git
cd conversation-intelligence-system

2. Create a virtual environment
python -m venv .venv

Activate it on macOS/Linux:
source .venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Configure the API key
Create a .env file:
GEMINI_API_KEY=your_api_key_here

The .env file is excluded from Git using .gitignore.
5. Run the application
python -m streamlit run app.py

The application will open in your browser.
##Evaluation
The system was evaluated on a 20-case customer-support test set covering different sentiment and urgency scenarios.

| Metric | Result |
|---|---:|
| Test cases completed | 20/20 |
| Sentiment accuracy | 95% |
| Urgency accuracy | 95% |
| Valid structured outputs | 100% |

Two classification mismatches were observed during evaluation. One involved urgency classification and one involved sentiment classification, highlighting the ambiguity that can occur in natural-language customer conversations.

The evaluation is a small development benchmark and should not be interpreted as production-level model performance.

The project also includes a separate grounding check for identifying recommendations that may rely on unsupported assumptions.

##Limitations
This project is a prototype designed for demonstrating LLM-based conversation analysis.
It does not provide:
- Real-time call transcription
- Production customer-service integration
- Autonomous customer support
- Guaranteed factual accuracy
- Access to internal customer-support systems
LLM outputs may still contain incorrect classifications or recommendations, which is why validation and grounding checks are included.
Future Improvements
Potential future improvements include:
- Larger and more diverse evaluation datasets
- More systematic grounding metrics
- Human evaluation of recommendations
- Conversation history analysis
- Dashboarding and analytics
- Integration with customer-support platforms
- Cost and latency optimization
- Production-grade monitoring
Author
Shreya Godala
Built as an applied AI / product-oriented project exploring LLM-powered customer conversation 
intelligence.
