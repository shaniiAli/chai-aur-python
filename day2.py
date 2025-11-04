# --- Input Section ---
import textwrap
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


def generate_bio(style):
    line = "-" * 40  
    
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
        return f"""{line}
        {name.upper()}
        {profession}
        "{passion}"
        {website if website else ''}
        {line}"""
    else:
        return "Invalid style selected."



bio = generate_bio(style)
print("\nHere is your generated bio:\n")
print(textwrap.dedent(bio))

save=input("\nWould you like to save this bio to a file? (y/n): ").strip().lower()
if save == 'y':
    filename=f"{name.lower().replace(' ','_')}_bio.txt"
    with open(filename,'w',encoding='utf-8') as f:
        f.write(bio)
    print(f"Bio saved to {filename}")
