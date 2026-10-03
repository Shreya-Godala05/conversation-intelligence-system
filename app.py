import streamlit as st
from analyzer import analyze_conversation, validate_result
from grounding_checker import check_grounding


st.set_page_config(
    page_title="Conversation Intelligence System",
    page_icon="💬",
    layout="wide"
)


st.title("💬 Conversation Intelligence System")

st.write(
    "Analyze customer conversations using an LLM and extract "
    "actionable customer insights."
)

st.divider()

st.subheader("Customer Conversation")

conversation = st.text_area(
    "Paste a customer conversation below:",
    height=200,
    placeholder="Example: I have been trying to reset my password..."
)

analyze_button = st.button("🔍 Analyze Conversation")


if analyze_button:

    if not conversation.strip():
        st.warning("Please enter a customer conversation first.")

    else:

        try:

            with st.spinner("Analyzing conversation..."):
                result = analyze_conversation(conversation)

            is_valid, validation_message = validate_result(result)

            if not is_valid:

                st.error(
                    f"Invalid AI output: {validation_message}"
                )

            else:

                st.success("Analysis completed successfully!")

                st.divider()

                st.subheader("📊 Customer Insights")

                col1, col2, col3 = st.columns(3)

                with col1:
                    st.metric(
                        "Sentiment",
                        result["sentiment"]
                    )

                with col2:
                    st.metric(
                        "Urgency",
                        result["urgency"]
                    )

                with col3:
                    st.metric(
                        "Intent",
                        result["intent"]
                    )

                st.subheader("🔎 Main Issue")

                st.write(
                    result["main_issue"]
                )

                st.subheader("📌 Key Points")

                for point in result["key_points"]:
                    st.write(f"• {point}")

                st.subheader("💡 Suggested Next Action")

                st.info(
                    result["suggested_next_action"]
                )

                st.divider()

                st.subheader("🛡️ Recommendation Grounding")

                with st.spinner(
                    "Checking recommendation grounding..."
                ):

                    grounding_result = check_grounding(
                        conversation,
                        result["suggested_next_action"]
                    )

                if grounding_result.get("grounded") is True:

                    st.success(
                        "✅ Recommendation appears to be grounded "
                        "in the conversation."
                    )

                else:

                    st.warning(
                        "⚠️ Recommendation may contain "
                        "unsupported assumptions."
                    )

                st.caption(
                    grounding_result.get(
                        "reason",
                        "No explanation provided."
                    )
                )

                st.divider()

                st.caption(
                    f"Output validation: {validation_message}"
                )

        except Exception as e:

            st.error(
                f"Something went wrong while analyzing "
                f"the conversation: {e}"
            )
