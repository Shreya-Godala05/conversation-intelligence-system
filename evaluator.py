import json

from analyzer import analyze_conversation
from test_cases import TEST_CASES


def evaluate():

    total = len(TEST_CASES)

    sentiment_correct = 0
    urgency_correct = 0

    print("\n===== MODEL EVALUATION =====\n")

    for case in TEST_CASES:

        print(f"Test Case {case['id']}")

        result = analyze_conversation(case["conversation"])

        predicted_sentiment = result.get("sentiment")
        predicted_urgency = result.get("urgency")

        expected_sentiment = case["expected_sentiment"]
        expected_urgency = case["expected_urgency"]

        sentiment_match = (
            predicted_sentiment.lower()
            == expected_sentiment.lower()
        )

        urgency_match = (
            predicted_urgency.lower()
            == expected_urgency.lower()
        )

        if sentiment_match:
            sentiment_correct += 1

        if urgency_match:
            urgency_correct += 1

        print("Expected sentiment:", expected_sentiment)
        print("Predicted sentiment:", predicted_sentiment)

        print("Expected urgency:", expected_urgency)
        print("Predicted urgency:", predicted_urgency)

        print("Sentiment correct:", sentiment_match)
        print("Urgency correct:", urgency_match)

        print("-" * 50)

    sentiment_accuracy = sentiment_correct / total
    urgency_accuracy = urgency_correct / total

    print("\n===== FINAL RESULTS =====")

    print(
        f"Sentiment accuracy: "
        f"{sentiment_accuracy * 100:.1f}%"
    )

    print(
        f"Urgency accuracy: "
        f"{urgency_accuracy * 100:.1f}%"
    )


if __name__ == "__main__":
    evaluate()
