import streamlit as st

st.set_page_config(page_title="AI-Powered Study Buddy")

st.title("📚 AI-Powered Study Buddy")

st.write("""
Students often struggle to understand complex concepts.
This AI tool helps explain topics, summarize notes,
and generate quizzes and flashcards instantly.
""")

menu = st.tabs(["📖 Explain Topic", "📝 Summarize Notes", "❓ Quiz Generator", "🗂 Flashcards"])

# ---------------- EXPLAIN TOPIC ----------------
with menu[0]:
    st.subheader("Explain a Topic Simply")

    topic = st.text_input("Enter Topic Name")
    level = st.selectbox("Select Difficulty Level", ["Beginner", "Intermediate", "Advanced"])

    if st.button("Generate Explanation"):
        if topic:

            if level == "Beginner":
                explanation = f"""
{topic} is a concept that helps solve real-world problems.

In simple terms, it is a method or idea used in its respective field
to improve efficiency and decision-making.

It works by applying basic principles and structured techniques
to achieve better results.
                """

            elif level == "Intermediate":
                explanation = f"""
{topic} is an important subject in its domain.

It involves understanding core principles, processes, and techniques
used to analyze, manage, or improve systems.

It plays a significant role in modern technology and research.
                """

            else:  # Advanced
                explanation = f"""
{topic} is a specialized concept involving advanced methodologies
and structured frameworks.

It integrates theoretical foundations with practical implementation,
often using algorithms, optimization techniques, and computational models.

It is widely applied in research, industry, and innovation-driven systems.
                """

            output = f"""
Topic: {topic}

Level: {level}

Explanation:
{explanation}
            """

            st.success("Explanation Generated Successfully!")
            st.text_area("Explanation Output", output, height=350)

        else:
            st.warning("Please enter a topic.")

# ---------------- SUMMARIZE NOTES ----------------
with menu[1]:
    st.subheader("Summarize Study Notes")

    notes = st.text_area("Paste Your Study Notes Here")

    if st.button("Generate Summary"):
        if notes:

            summary = f"""
SUMMARY:

The provided notes mainly discuss:

• Important definitions  
• Key concepts  
• Core explanations  
• Applications  

This is a simplified version of your notes for quick revision.
            """

            st.success("Summary Generated Successfully!")
            st.text_area("Summary Output", summary, height=350)
        else:
            st.warning("Please paste your notes.")

# ---------------- QUIZ GENERATOR ----------------
with menu[2]:
    st.subheader("Generate Quiz Questions")

    quiz_topic = st.text_input("Enter Topic for Quiz")
    num_questions = st.selectbox("Number of Questions", [3, 5, 10])

    if st.button("Generate Quiz"):
        if quiz_topic:

            question_templates = [
                f"What is {quiz_topic}?",
                f"Explain the importance of {quiz_topic}.",
                f"What are the main components of {quiz_topic}?",
                f"Give one real-world example of {quiz_topic}.",
                f"What are the advantages of {quiz_topic}?",
                f"What are the limitations of {quiz_topic}?",
                f"How is {quiz_topic} used in industry?",
                f"Differentiate {quiz_topic} from related concepts.",
                f"What tools are commonly used in {quiz_topic}?",
                f"Why is {quiz_topic} important in modern technology?"
            ]

            quiz = f"Quiz on {quiz_topic}\n\n"

            for i in range(num_questions):
                quiz += f"{i+1}. {question_templates[i]}\n"

            st.success("Quiz Generated Successfully!")
            st.text_area("Quiz Output", quiz, height=350)

        else:
            st.warning("Please enter a topic.")

# ---------------- FLASHCARDS ----------------
with menu[3]:
    st.subheader("Generate Flashcards")

    flash_topic = st.text_input("Enter Topic for Flashcards")

    if st.button("Generate Flashcards"):
        if flash_topic:

            flashcards = f"""
Flashcards on {flash_topic}

Card 1:
Q: What is {flash_topic}?
A: Definition of {flash_topic}

Card 2:
Q: Why is {flash_topic} important?
A: It helps in understanding core concepts.

Card 3:
Q: Give one example of {flash_topic}.
A: Real-world example.
            """

            st.success("Flashcards Generated Successfully!")
            st.text_area("Flashcards Output", flashcards, height=350)
        else:
            st.warning("Please enter topic.")