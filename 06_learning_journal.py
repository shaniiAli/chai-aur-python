import datetime

def log_learning_entry():
    entry = input("What did you learn today: ").strip()
    rating = input("Rate your productivity (1-5): ").strip()
    while not rating.isdigit() or not (1 <= int(rating) <= 5):
        rating = input("Please enter a valid productivity rating (1-5): ").strip()
    f = open("learning_journal.txt", "a")
    time = datetime.datetime.now().strftime(" -- %Y-%m-%d %H:%M:%S")
    f.write(entry + time + "\n")
    f.write("Productivity Rating: " + rating + "\n\n")
    f.close()

log_learning_entry()
