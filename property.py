class Property:
    """
    the  class representation of a property
    """
    def __init__(self, square_feet='', beds='',
                 baths='', **kwargs):
        super().__init__(**kwargs)
        self.square_feet = square_feet
        self.num_bedrooms = beds
        self.num_baths = baths

    def display(self):
        """
        (object) -> ()
        Prints some details about the property:
        square footage, the number of bedrooms and
        the number of bathrooms.
        """
        print("PROPERTY DETAILS")
        print("================")
        print("square footage: {}".format(self.square_feet))
        print("bedrooms: {}".format(self.num_bedrooms))
        print("bathrooms: {}".format(self.num_baths))
        print()

    def prompt_init():
        """
        Prompts (input) for square feet, the number of beds and the number of baths.
        :return: (dict) - collected information.
        """
        return dict(square_feet=input("Enter the square feet: "),
                    beds=input("Enter number of bedrooms: "),
                    baths=input("Enter number of baths: "))
    prompt_init = staticmethod(prompt_init)


def get_valid_input(input_string, valid_options):
    """
    Asks for information and returns it.
    :param input_string: (str) - the question.
    :param valid_options: (tuple) - options to choose.
    :return: (str) - collected information.
    """
    input_string += " ({}) ".format((", ".join(valid_options)))
    response = input(input_string)
    while response.lower() not in valid_options:
        response = input(input_string)
    return response


class Apartment(Property):
    """
    a class representation of the apartment property
    """
    valid_laundries = ("coin", "ensuite", "none")
    valid_balconies = ("yes", "no", "solarium")

    def __init__(self, balcony='', laundry='', **kwargs):
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        """
        (object) -> ()
        Prints some details about the apartment property:
        laundry and balcony.
        """
        super().display()
        print("APARTMENT DETAILS")
        print("laundry: {}".format(self.laundry))
        print("has balcony: {}".format(self.balcony))

    def prompt_init():
        """
        Prompts (input) for laundry facilities and the existence of a balcony.
        :return: (dict) - collected information.
        """
        parent_init = Property.prompt_init()
        laundry = get_valid_input(
                "What laundry facilities does "
                "the property have? ",
                Apartment.valid_laundries)
        balcony = get_valid_input(
                "Does the property have a balcony?",
                Apartment.valid_balconies)
        parent_init.update({
            "laundry": laundry,
            "balcony": balcony
        })
        return parent_init
    prompt_init = staticmethod(prompt_init)


class House(Property):
    """
    a class representation of the house property
    """
    valid_garage = ("attached", "detached", "none")
    valid_fenced = ("yes", "no")

    def __init__(self, num_stories='',
                 garage='', fenced='', **kwargs):
        super().__init__(**kwargs)
        self.garage = garage
        self.fenced = fenced
        self.num_stories = num_stories

    def display(self):
        """
        (object) -> ()
        Prints some details about the house property:
        # (number) of stories, existence of a garage and a yard (fenced or not).
        """
        super().display()
        print("HOUSE DETAILS")
        print("# of stories: {}".format(self.num_stories))
        print("garage: {}".format(self.garage))
        print("fenced yard: {}".format(self.fenced))

    def prompt_init():
        """
        Prompts (input) for type of a yard (fenced or not), existence of a garage and
        the # (number) of stories in the house.
        :return: (dict) - collected information.
        """
        parent_init = Property.prompt_init()
        fenced = get_valid_input("Is the yard fenced? ",
                                 House.valid_fenced)
        garage = get_valid_input("Is there a garage? ",
                                 House.valid_garage)
        num_stories = input("How many stories? ")

        parent_init.update({
            "fenced": fenced,
            "garage": garage,
            "num_stories": num_stories
        })
        return parent_init
    prompt_init = staticmethod(prompt_init)


class Purchase:
    """
    a class representation for purchase payment
    """
    def __init__(self, price='', taxes='', **kwargs):
        super().__init__(**kwargs)
        self.price = price
        self.taxes = taxes

    def display(self):
        """
        (object) -> ()
        Prints some details about the purchase deal:
        selling price and estimated taxes.
        """
        super().display()
        print("PURCHASE DETAILS")
        print("selling price: {}".format(self.price))
        print("estimated taxes: {}".format(self.taxes))

    def prompt_init():
        """
        Prompts (input) for selling price and the estimated taxes.
        :return: (dict) - collected information.
        """
        return dict(price=input("What is the selling price? "),
                    taxes=input("What are the estimated taxes? "))
    prompt_init = staticmethod(prompt_init)


class Rental:
    def __init__(self, furnished='', utilities='',
            rent='', **kwargs):
        super().__init__(**kwargs)
        self.furnished = furnished
        self.rent = rent
        self.utilities = utilities

    def display(self):
        """
        (object) -> ()
        Prints some details about the rental deal:
        price of a rent, estimated utilities and whether the property is furnished.
        """
        super().display()
        print("RENTAL DETAILS")
        print("rent: {}".format(self.rent))
        print("estimated utilities: {}".format(self.utilities))
        print("furnished: {}".format(self.furnished))

    def prompt_init():
        """
        Prompts (input) for price of a rent, estimated utilities and whether the property is furnished.
        :return: (dict) - collected information.
        """
        return dict(
            rent=input("What is the monthly rent? "),
            utilities=input("What are the estimated utilities? "),
            furnished = get_valid_input("Is the property furnished? ",
                                        ("yes", "no")))
    prompt_init = staticmethod(prompt_init)


class HouseRental(Rental, House):
    """
    a class-template representation of the rental house property
    """
    def prompt_init():
        """
        Prompts (input) for information on the rental house property.
        :return: (dict) - collected information.
        """
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)


class ApartmentRental(Rental, Apartment):
    """
    a class-template representation of the rental apartment property
    """
    def prompt_init():
        """
        Prompts (input) for information on the rental apartment property.
        :return: (dict) - collected information.
        """
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)


class ApartmentPurchase(Purchase, Apartment):
    """
    a class-template representation of the purchased apartment property
    """
    def prompt_init():
        """
        Prompts (input) for information on the purchased apartment property.
        :return: (dict) - collected information.
        """
        init = Apartment.prompt_init()
        init.update(Purchase.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)


class HousePurchase(Purchase, House):
    """
    a class-template representation of the purchased house property
    """
    def prompt_init():
        """
        Prompts (input) for information on the purchased house property..
        :return: (dict) - collected information.
        """
        init = House.prompt_init()
        init.update(Purchase.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)


class Agent:
    """
    a class representation of the agent
    """
    type_map = {
        ("house", "rental"): HouseRental,
        ("house", "purchase"): HousePurchase,
        ("apartment", "rental"): ApartmentRental,
        ("apartment", "purchase"): ApartmentPurchase
        }

    def __init__(self):
        self.property_list = []

    def display_properties(self):
        """
        (object) -> ()
        Prints all the information about the chosen property(ies).
        """
        for property in self.property_list:
            print()
            property.display()
            print()

    def add_property(self):
        """
        (object) -> ()
        Adds the new property to the agent list.
        """
        property_type = get_valid_input(
                "What type of property? ",
                ("house", "apartment")).lower()
        payment_type = get_valid_input(
                "What payment type? ",
                ("purchase", "rental")).lower()

        PropertyClass = self.type_map[(property_type, payment_type)]
        init_args = PropertyClass.prompt_init()
        self.property_list.append(PropertyClass(**init_args))

    def remove_property(self):
        """
        (object) -> ()
        Removes the property from the agent list.
        """
        if len(self.property_list) == 0:
            print('Nothing to remove.')
            return None
        print('--------------------------------------------')
        print('\nHere is the list:\n')
        self.display_properties()
        print('\nWhich one you would like to remove from it?\n')
        print('--------------------------------------------')
        index = eval(input('What element to remove, type the index of it. Starting from 1.'))
        if type(index) != int:
            print('Wrong input.')
            return None
        index -= 1
        self.property_list.pop(index)
        print('\nYou have successfuly removed the property from the list.\n')
        print('--------------------------------------------')
        print('\nHere is the list:\n')
        self.display_properties()
        print('--------------------------------------------')

    def multiply(self):
        """
        (object) -> ()
        Multiplies the property in the agent list.
        """
        if len(self.property_list) == 0:
            print('Nothing to remove.')
            return None
        print('--------------------------------------------')
        print('\nHere is the list:\n')
        self.display_properties()
        print('\nWhich one you would like to remove from it?\n')
        print('--------------------------------------------')
        index = eval(input('What element to multiply, type the index of it. Starting from 1.'))
        by = eval(input('How many more property like this you want?'))
        while type(by) != int:
            print('Wrong input.')
            by = eval(input('How many more property like this you want?'))
        while type(index) != int:
            print('Wrong input.')
            index = eval(input('What element to multiply, type the index of it. Starting from 1.'))
        index -= 1
        for i in range(0, by-1):
            self.property_list.append(self.property_list[index])
        print('\nYou have successfuly multiplied the property in the list.\n')
        print('--------------------------------------------')
        print('\nHere is the list:\n')
        self.display_properties()
        print('\n--------------------------------------------')


def main():
    """
    module for checking if the program works
    """
    agent = Agent()
    agent.add_property()
    agent.multiply()
    agent.remove_property()

main()
