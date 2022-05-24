MY_DICT = {'A': "Ньюфаундленд", 'B': "Новая Шотландия",
                'C': "Остров Принца Эдуарда", 'E': "Нью-Брансуик",
                'G': "Квебек", 'H': "Квебек", 'J': "Квебек", 'K': "Онтарио",
                'L': "Онтарио", 'M': "Онтарио", 'N': "Онтарио", 'P': "Онтарио",
                'R': "Манитоба", 'S': "Саскачеван", 'T': "Альберта",
                'V': "Британская Колумбия",
                'X': "Нунавут или Северо-Западные территории", 'Y': "Юкон"}


zip = input("please enter the zipcode ------>")
if zip[0].upper() in MY_DICT.keys():
    if zip[1] == "0":
        citytype = "village"
    else:
        citytype = "city"
        identificator = zip[0]
        identificator = identificator.upper()
        region = MY_DICT.get(identificator)
        print("The entered zip code belongs to the " + citytype + " " + region)
else:
    print("Please enter a valid zip code")
