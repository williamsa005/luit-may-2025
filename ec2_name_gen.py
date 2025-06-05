import random
import string

num_instances = int(input("How many EC2 instance names do you want to generate?"))

department = input("Enter your department name: ").strip().lower()

def generate_ec2_name(department):
    # 6-character random string of letters and digits
    random_part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    return f"{department}-{random_part}"

def generate_unique_names(department, count):
    names = set()
    while len(names) < count:
        name = generate_ec2_name(department)
        names.add(name)
    return list(names)

ec2_names = generate_unique_names(department, num_instances)

print("\nGenerated EC2 Instance Names:")
for name in ec2_names:
    print(name)