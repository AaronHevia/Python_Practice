def greeting() -> None:
    """
    Prints the opening greeting to the Band Name Generator.
    @rtype: None
    """
    print('Hello and welcome to Band Name Generator')


def get_city() -> str:
    """
    Asks the user for the city they were born in.
    @rtype: str
    @ return City Name
    """
    return input('In what city were you born?\n')


def get_pet() -> str:
    """
    Asks the user for a pet name.
    @rtype: str
    @return: Pet Name
    """
    return input("If you had a pet, what would it's name be?\n")


def concatenate(city, pet) -> str:
    """
    Concatenates 2 strings together with a space in between.
    @param city: string City Name
    @param pet: string Pet Name
    @rtype: str
    @return: Band Name
    """
    return city + ' ' + pet


def give_result(band) -> None:
    """
    Prints a band name response to the user.
    @param band: string Band Name
    @rtype: str
    @return: Response of Band Name
    """
    print('The name of your band shall be "' + band + '"\nRock on ' + band + '!')


greeting()
cityName = get_city()
petName = get_pet()
bandName = concatenate(cityName, petName)
give_result(bandName)
