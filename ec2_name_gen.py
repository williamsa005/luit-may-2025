import random  # Imports the random module to generate random values
import string  # Imports the string module to access sets of characters like letters and digits

# Ask the user how many EC2 instance names to generate, and convert the input to an integer
num_instances = int(input("How many EC2 instance names do you want to generate?"))

# Ask the user for the department name, strip leading/trailing spaces and convert to lowercase
department = input("Enter your department name: ").strip().lower()

# Function to generate a single EC2 name
def generate_ec2_name(department):
    # Generate a 6-character random string using uppercase letters and digits
    random_part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    # Return the EC2 name in the format: department-randomstring
    return f"{department}-{random_part}"

# Function to generate the requested number of unique EC2 names
def generate_unique_names(department, count):
    names = set()  # Use a set to ensure all names are unique
    while len(names) < count:  # Keep generating names until we have the desired amount
        name = generate_ec2_name(department)  # Generate a new name
        names.add(name)  # Add the name to the set (duplicates are automatically ignored)
    return list(names)  # Convert the set to a list before returning

# Call the function and store the result in ec2_names
ec2_names = generate_unique_names(department, num_instances)

# Print the generated names to the screen
print("\nGenerated EC2 Instance Names:")
for name in ec2_names:  # Loop through each name in the list
    print(name)  # Print the name

