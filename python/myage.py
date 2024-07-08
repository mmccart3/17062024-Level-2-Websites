day_of_birth = 29
month_of_birth = 4
year_of_birth = 1965

days_in_months = [31,28,31,30,31,30,31,31,30,31,30,31]

day_today = 1
month_today = 7
year_today = 2024

days_till_end_of_first_year = days_in_months[month_of_birth-1] - day_of_birth
for x in range(month_of_birth, 12):
    days_till_end_of_first_year = days_till_end_of_first_year + days_in_months[x]
print(days_till_end_of_first_year)

days_till_today = day_today
for x in range(0,month_today-1):
    days_till_today = days_till_today + days_in_months[x]
print(days_till_today)

leap_days = 0
for x in range(year_of_birth,year_today):
    if x%4 == 0:
        leap_days += 1
print(leap_days)

number_of_full_years_alive = year_today - year_of_birth - 1

days_alive = (number_of_full_years_alive * 365) + leap_days + days_till_end_of_first_year + days_till_today

print(days_alive)