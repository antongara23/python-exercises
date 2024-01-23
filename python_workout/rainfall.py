def get_rainfall():
    """Tracks rainfall in a number of cities. User enter the name of a
    city and how much rain has fallen in that city. If the city name is
    blank, then the function prints a report"""
    rainfall = {}
    while True:
        city = input("Enter a city: ")
        if city:
            rain = input("Enter much rain there was: ")
            if not rain:
                rain = 0
            rainfall[city] = rainfall.get(city, 0) + int(rain)
        else:
            break
    for city, rain in rainfall.items():
        print(f"{city}: {rain}")


def get_rainfall_avg():
    """Same as get_rainfall plus avg of rainfall in report."""
    rainfall = {}
    while True:
        city = input("Enter a city: ")
        if city:
            rain = input("Enter much rain there was: ")
            if not rain:
                rain = 0
            if city in rainfall:
                rainfall[city].append(int(rain))
            else:
                rainfall[city] = [int(rain)]
        else:
            break
    for city, rain in rainfall.items():
        print(f"{city}: total is {sum(rainfall[city])},"
              f"average is {sum(rainfall[city]) / len(rainfall[city])}")


def word_counter():
    """Read text file and return a sorted dict which is contained words with
    number of appearances in a text"""
    words = {}
    with open('some_text.txt', mode='r') as file:
        text = file.read()
        for word in text.split():
            if word not in words:
                words[word] = 1
            else:
                words[word] += 1
    print(dict(sorted(words.items(), key=lambda x: x[1], reverse=True)))


if __name__ == '__main__':
    get_rainfall()
    get_rainfall_avg()
    word_counter()
