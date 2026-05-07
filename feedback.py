def save_feedback(text):

    with open("feedback.txt", "a") as f:
        f.write(text + "\n")

