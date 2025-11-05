def calculate_minutes(age_years):
    DAYS_IN_YEAR = 365.25  # accounting for leap years
    HOURS_IN_DAY = 24
    MINUTES_IN_HOUR = 60

    total_days = age_years * DAYS_IN_YEAR
    total_hours = total_days * HOURS_IN_DAY
    total_minutes = total_hours * MINUTES_IN_HOUR
    return round(total_days), round(total_hours), round(total_minutes)


while True:
    try:
        age = float(input('Enter your age in years: '))
        if age <= 0:
            print('Please enter a valid positive number.\n')
            continue
        
        days, hours, minutes = calculate_minutes(age)
        print(f"\nYou have lived approximately:\n"
              f" 🗓️  {days:,} days\n"
              f" ⏰ {hours:,} hours\n"
              f" 🕒 {minutes:,} minutes.")
        
        again = input('\nWould you like to calculate again? (yes/no): ').strip().lower()
        if again not in ('yes', 'y'):
            print('\n👋 Goodbye! Have a great day!')
            break

    except ValueError:
        print('Please enter a valid number to calculate.\n')
