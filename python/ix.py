from datetime import datetime

# Define the birth date in format yyyy-mm-dd
birth_date = '1990-01-01'

# Parse the birth date
dt = datetime.strptime(birth_date, '%Y-%m-%d')

# Define the zodiac signs and their date ranges
zodiac_signs = {
    'Aries':      (datetime(dt.year,  3, 21), datetime(dt.year,  4, 19)),
    'Taurus':     (datetime(dt.year,  4, 20), datetime(dt.year,  5, 20)),
    'Gemini':     (datetime(dt.year,  5, 21), datetime(dt.year,  6, 20)),
    'Cancer':     (datetime(dt.year,  6, 21), datetime(dt.year,  7, 22)),
    'Leo':        (datetime(dt.year,  7, 23), datetime(dt.year,  8, 22)),
    'Virgo':      (datetime(dt.year,  8, 23), datetime(dt.year,  9, 22)),
    'Libra':      (datetime(dt.year,  9, 23), datetime(dt.year, 10, 22)),
    'Scorpio':    (datetime(dt.year, 10, 23), datetime(dt.year, 11, 21)),
    'Sagittarius':(datetime(dt.year, 11, 22), datetime(dt.year, 12, 21)),
    'Capricorn':  (datetime(dt.year, 12, 22), datetime(dt.year+1,  1, 19)),
    'Aquarius':   (datetime(dt.year+1,  1, 20), datetime(dt.year+1,  2, 18)),
    'Pisces':     (datetime(dt.year+1,  2, 19), datetime(dt.year+1,  3, 20))
}



gk = {
    'Aries':      (datetime(dt.year,  3, 21), datetime(dt.year,  4, 19)),
    'Taurus':     (datetime(dt.year,  4, 20), datetime(dt.year,  5, 20)),
    'Gemini':     (datetime(dt.year,  5, 21), datetime(dt.year,  6, 20)),
    'Cancer':     (datetime(dt.year,  6, 21), datetime(dt.year,  7, 22)),
    'Leo':        (datetime(dt.year,  7, 23), datetime(dt.year,  8, 22)),
    'Virgo':      (datetime(dt.year,  8, 23), datetime(dt.year,  9, 22)),
    'Libra':      (datetime(dt.year,  9, 23), datetime(dt.year, 10, 22)),
    'Scorpio':    (datetime(dt.year, 10, 23), datetime(dt.year, 11, 21)),
    'Sagittarius':(datetime(dt.year, 11, 22), datetime(dt.year, 12, 21)),
    'Capricorn':  (datetime(dt.year, 12, 22), datetime(dt.year+1,  1, 19)),
    'Aquarius':   (datetime(dt.year+1,  1, 20), datetime(dt.year+1,  2, 18)),
    'Pisces':     (datetime(dt.year+1,  2, 19), datetime(dt.year+1,  3, 20))
}

# Check which zodiac sign the birth date falls under
for sign, (start, end) in zodiac_signs.items():
    if start <= dt <= end:
        #print(f"The zodiac sign for the birth date {birth_date} is {sign}.")
        break


print(f"The zodiac sign for the birth date {birth_date} is {sign}.")