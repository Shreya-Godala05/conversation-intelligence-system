import time

from analyzer import analyze_conversation, validate_result
from test_cases import TEST_CASES


correct_sentiment = 0
correct_urgency = 0
completed_cases = 0
valid_outputs = 0


print("\n===== CONVERSATION INTELLIGENCE EVALUATION =====\n")


for i, case in enumerate(TEST_CASES, start=1):

    print(f"Test {i}/{len(TEST_CASES)}")

    try:
        result = analyze_conversation(case["conversation"])

        is_valid, validation_message = validate_result(result)

        if is_valid:
            valid_outputs += 1

        predicted_sentiment = result["sentiment"].lower()
        expected_sentiment = case["expected_sentiment"].lower()

        predicted_urgency = result["urgency"].lower()
        expected_urgency = case["expected_urgency"].lower()

        sentiment_correct = predicted_sentiment == expected_sentiment
        urgency_correct = predicted_urgency == expected_urgency

        if sentiment_correct:
            correct_sentiment += 1

        if urgency_correct:
            correct_urgency += 1

        completed_cases += 1

        print(f"Expected sentiment: {case['expected_sentiment']}")
        print(f"Predicted sentiment: {result['sentiment']}")
        print(f"Sentiment correct: {sentiment_correct}")

        print(f"Expected urgency: {case['expected_urgency']}")
        print(f"Predicted urgency: {result['urgency']}")
        print(f"Urgency correct: {urgency_correct}")

        print(f"Output valid: {is_valid}")
        print("-" * 50)

    except Exception as e:

        print(f"Test {i} could not be completed.")
        print(f"Error: {e}")
        print("-" * 50)

        print("Waiting before continuing...")
        time.sleep(60)

        continue

    # Wait between API requests to reduce the chance
    # of hitting the free-tier rate limit.
    time.sleep(5)


print("\n===== FINAL EVALUATION =====")

print(f"Completed cases: {completed_cases}/{len(TEST_CASES)}")

if completed_cases > 0:

    sentiment_accuracy = (
        correct_sentiment / completed_cases
    ) * 100

    urgency_accuracy = (
        correct_urgency / completed_cases
    ) * 100

    validation_rate = (
        valid_outputs / completed_cases
    ) * 100

    print(
        f"Sentiment accuracy: "
        f"{sentiment_accuracy:.2f}%"
    )

    print(
        f"Urgency accuracy: "
        f"{urgency_accuracy:.2f}%"
    )

    print(
        f"Valid output rate: "
        f"{validation_rate:.2f}%"
    )

else:

    print("No cases were completed.")
