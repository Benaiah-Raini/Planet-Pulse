class CarbonFootprintCalculator:
    """
    A class to calculate carbon footprint based on transportation, electricity usage, and food consumption.
    """

    def __init__(self):
        """
        Initializes the CarbonFootprintCalculator instance.
        """
        self.transportation_cf = 0
        self.electricity_cf = 0
        self.food_cf = 0

    def transport_footprint(self, transport_method, distance):
        """
        Calculates the carbon footprint for transportation.

        Args:
            transport_method (str): The mode of transportation (e.g., 'gas_car', 'electric_car', 'bus', 'train', 'bike', 'walk').
            distance (float): The distance covered.

        Returns:
            float: The carbon footprint for transportation.
        """
        if transport_method.lower() == 'gas_car':
            self.transportation_cf = distance * 1.5  # Average for gasoline cars
        elif transport_method.lower() == 'electric_car':
            self.transportation_cf = distance * 0.5  # Average for electric cars
        elif transport_method.lower() == 'bus':
            self.transportation_cf = distance * 0.8  # Assuming a typical bus
        elif transport_method.lower() == 'train':
            self.transportation_cf = distance * 0.2  # Assuming a typical train
        elif transport_method.lower() == 'bike':
            self.transportation_cf = 0  # Assuming negligible carbon footprint
        elif transport_method.lower() == 'walk':
            self.transportation_cf = 0  # Assuming negligible carbon footprint
        else:
            print("Invalid transport method. Please choose from 'gas_car', 'electric_car', 'bus', 'train', 'bike', or 'walk'.")
            self.transportation_cf = 0
        return self.transportation_cf

    def electricity_footprint(self, usage):
        """
        Calculates the carbon footprint for electricity usage.

        Args:
            usage (float): The electricity usage.

        Returns:
            float: The carbon footprint for electricity usage.
        """
        if usage is None or usage < 0:
            print("Invalid electricity usage. Please enter a non-negative value.")
            self.electricity_cf = 0
        else:
            self.electricity_cf = usage * 0.5  # Assuming a typical grid mix
        return self.electricity_cf

    def food_footprint(self, category, num_of_meals):
        """
        Calculates the carbon footprint for food consumption.

        Args:
            category (str): The category of food (e.g., 'beef', 'pork', 'chicken', 'fish', 'vegetables', 'fruits').
            num_of_meals (int): The number of meals consumed.

        Returns:
            float: The carbon footprint for food consumption.
        """
        if num_of_meals < 0:
            print("Invalid number of meals. Please enter a non-negative value.")
            self.food_cf = 0
        else:
            if category.lower() == 'beef':
                self.food_cf = num_of_meals * 2.5
            elif category.lower() == 'pork':
                self.food_cf = num_of_meals * 1.8
            elif category.lower() == 'chicken':
                self.food_cf = num_of_meals * 1.2
            elif category.lower() == 'fish':
                self.food_cf = num_of_meals * 1.5
            elif category.lower() in ['vegetables', 'fruits']:
                self.food_cf = num_of_meals * 0.5
            else:
                self.food_cf = num_of_meals * 1.0
        return self.food_cf

    def calculate_total_carbon_footprint(self):
        """
        Calculates the total carbon footprint.

        Returns:
            float: The total carbon footprint.
        """
        total_individual_carbon_footprint = self.transportation_cf + self.electricity_cf + self.food_cf
        return total_individual_carbon_footprint

#  usage example
calculator = CarbonFootprintCalculator()
while True:
    transport_method = input('enter your transport method (gas_car, electric_car, bus, train, bike, walk):')
    if transport_method.lower() in ['gas_car', 'electric_car', 'bus', 'train', 'bike', 'walk']:
        break
    else:
        print("Invalid transport method. Please choose from 'gas_car', 'electric_car', 'bus', 'train', 'bike', or 'walk'.")

distance = float(input('enter the distance covered:'))
while True:
    try:
        usage = float(input('enter the electric usage:'))
        if usage >= 0:
            break
        else:
            print("Invalid electricity usage. Please enter a non-negative value.")
    except ValueError:
        print("Invalid input. Please enter a number.")
        
while True:
    try:
        num_of_meals = float(input('enter the num of meals:'))
        if num_of_meals >= 0:
            break
        else:
            print("Invalid number of meals. Please enter a non-negative value.")
    except ValueError:
        print("Invalid input. Please enter a number.")

category = input('enter your food category:')

calculator.transport_footprint(transport_method, distance)
calculator.electricity_footprint(usage)
calculator.food_footprint(category, num_of_meals)

total_individual_carbon_footprint = calculator.calculate_total_carbon_footprint()

print("Total Individual Carbon Footprint: {} tons CO2e".format(total_individual_carbon_footprint))

def generate_recommendations(total_carbon_footprint):
    recommendations = []
    if total_carbon_footprint > 200:  # Example threshold for high carbon footprint
        recommendations.append("Consider using public transportation or carpooling to reduce emissions from transportation.")
        recommendations.append("Switch to energy-efficient appliances and turn off unused electronics to reduce electricity consumption.")
        recommendations.append("Reduce consumption of high-carbon foods like beef and pork, and incorporate more plant-based meals into your diet.")
    elif total_carbon_footprint > 100:  # Example threshold for moderate carbon footprint
        recommendations.append("Opt for biking or walking short distances instead of driving.")
        recommendations.append("Unplug chargers and appliances when not in use to save energy.")
        recommendations.append("Choose locally sourced and seasonal foods to reduce carbon emissions from transportation.")
         recommendations.append("Reduce your overall number of car trips. Walk, bike, or use public transport whenever possible.")
    elif total_carbon_footprint > 50:
        recommendations.append("Reduce your meat consumption, especially red meat like beef.")
        recommendations.append("Consider adopting a more plant-based diet.")
        recommendations.append("Plant trees to offset your carbon footprint.")
        recommendations.append("Support companies committed to sustainability practices.")
    else:
        recommendations.append("Continue using sustainable transportation methods.")
        recommendations.append("Keep up the good work on managing electricity usage efficiently.")
        recommendations.append("Consider supporting sustainable farming practices by choosing organic and locally produced foods.")

    return recommendations

