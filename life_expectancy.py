poof = False
while __name__ == "__main__":
    try:
        with open("life-expectancy.csv") as file:
            try:
                start = int(input("Please choose an option from the following:\n 1. View highest, lowest, and average overall life expectancy\n 2. View highes, lowest, and average life expectancy for a given year\n 3. View highest, lowest, and average life expectancy for a given country\n 4. Exit\n "))
                print()
            except ValueError:
                start = 'not_a_number'
            year_data = list()
            country_data = list()
            if start == 1: #Overall
                lowest = float(999)
                highest = float(0)
                for data in file:
                    data_2 = data.split(",")
                    country = data_2[0]
                    year = data_2[2]
                    life = data_2[3]
                    try:
                        life = float(life)
                    except ValueError:
                        continue
                    try:
                        year = int(year)
                    except ValueError:
                        continue
                    if life < lowest:
                        lowest = life
                        lowest_year = year
                        lowest_country = country
                    if life > highest:
                        highest = life
                        highest_year = year
                        highest_country = country
                print (f"The lowest life expectancy is {lowest_country} in the year {lowest_year} with a life expectancy of {lowest} years")
                print(f"The highest life expectancy is {highest_country} in the year {highest_year} with {highest} years \n")
            elif start == 2: #Year
                check_year = int(input("Enter year of interest: "))
                year_lowest = float(999)
                year_highest= float(0)
                for data in file:
                    data_2 = data.split(",")
                    country = data_2[0]
                    year = data_2[2]
                    life = data_2[3]
                    try:
                        life = float(life)
                    except ValueError:
                        continue
                    try:
                        year = int(year)
                    except ValueError:
                        continue
                    if year == check_year:
                        year_data.append(life)
                        if life < year_lowest:
                            year_lowest = life
                            year_lowest_country = country
                        if life > year_highest:
                            year_highest = life
                            year_highest_country = country
                    else:
                        continue
                year_average = sum(year_data)/len(year_data)
                print (f"The average life expectancy for the year {check_year} was {year_average} years")
                print(f"The highest life expectancy for {check_year} was in {year_highest_country} with {year_highest} years")
                print(f"The lowest life expectancy for {check_year} was in {year_lowest_country} with {year_lowest} years \n")
            elif start == 3: #Country
                check_country = input("Enter country of interest: ")
                check_country = check_country.lower()
                country_lowest = float(999)
                country_highest= float(0)
                for data in file:
                    data_2 = data.split(",")
                    country = data_2[0]
                    year = data_2[2]
                    life = data_2[3]
                    try:
                        life = float(life)
                    except ValueError:
                        continue
                    try:
                        year = int(year)
                    except ValueError:
                        continue
                    country = country.lower()
                    if country == check_country:
                        country_data.append(life)
                        if life < country_lowest:
                            country_lowest = life
                            country_lowest_year = year
                        if life > country_highest:
                            country_highest = life
                            country_highest_year = year
                check_country = check_country.title()
                country_average = sum(country_data)/len(country_data)
                print (f"The average life expectancy for {check_country} was: {country_average} years")
                print(f"The highest life expectancy for {check_country} was in {country_highest_year} with {country_highest} years")
                print(f"The lowest life expectancy for {check_country} was in {country_lowest_year} with {country_lowest} years")
            elif start == 4:
                poof = True
                break
            else:
                if start == 'not_a_number':
                    print("That is not a number, please try again")
                else:
                    print("That is not an option, please try again.")
    except FileNotFoundError:
        print("File not found.")
        break
    if poof:
        break
