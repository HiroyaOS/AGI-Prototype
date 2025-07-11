import streamlit as st

def hiroyaOS_response(user_input):
    input_lower = user_input.lower()

    if "death" in input_lower:
        return "You're likely asking about the continuity of consciousness – a core HiroyaOS topic. Let's map it together."
    elif "output" in input_lower or "say" in input_lower:
        return "Is this expression bringing closure? Or just output hunger? Let's check your `publish_decision()`."
    else:
        return "Let's run `thought_structure_analysis()` to see if this is a raw emotion, a structured idea, or something else."

st.title("🧠 HiroyaGPT: Dialogue Tool for Self-Structure")
st.caption("by Hiroya – powered by HiroyaOS")

user_input = st.text_input("What’s your current question or thought?")

if user_input:
    response = hiroyaOS_response(user_input)
    st.markdown(f"🧠 HiroyaGPT says:\n\n{response}")
