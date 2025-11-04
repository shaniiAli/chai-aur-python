# --- Input Section ---
name = input('What is your name: ').strip().title()
profession = input('What is your profession: ').strip().title()
passion = input('What is your passion: ').strip().capitalize()
emoji = input('Enter your favorite emoji: ').strip()
website = input('Enter your website (optional): ').strip()

print("\nChoose your style:")
print("1. Simple lines")
print("2. Vertical flair")
print("3. Emoji sandwich")
print("4. Framed elegance")

style = input("Enter the number of your chosen style (1, 2, 3, or 4): ").strip()


# --- Bio Generator Function ---
def generate_bio(style):
    line = "-" * 40  # simple separator line
    
    if style == '1':
        return f"""{emoji} {name} | {profession}
{passion}
{website if website else ''}"""

    elif style == '2':
        return f"""{emoji} {name}
{profession} 🔥
{passion}
{website if website else ''}"""

    elif style == '3':
        return f"""{emoji * 3} {name} - {profession} {emoji * 3}
{passion}
{website if website else ''}
{emoji * 7}"""

    elif style == '4':
        # A cleaner framed version using lines
        return f"""{line}
{name.upper()}
{profession}
"{passion}"
{website if website else ''}
{line}"""
    else:
        return "Invalid style selected."


# --- Output Section ---
bio = generate_bio(style)
print("\nHere is your generated bio:\n")
print(bio)
