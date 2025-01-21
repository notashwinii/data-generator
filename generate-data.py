import csv
import random
import string

def generate_unique_numbers(start_number: int, num_digits: int, count: int):
    """Generates a list of unique numbers starting from the given number."""
    start_number_str = str(start_number)
    prefix = start_number_str[:num_digits - len(str(count))]
    return [f"{prefix}{i:02d}" for i in range(1, count + 1)]

def generate_random_names(count: int):
    """Generates a list of random names (sample names)."""
    first_names = ["Shreya", "Kritika", "Aarav", "Suman", "Pooja", "Anish", "Bikash", "Sita", "Ramesh", "Deepa"]
    last_names = ["Bashyal", "Regmi", "Sharma", "Thapa", "Gurung", "Rana", "Lama", "Karki", "Dahal", "Maharjan"]
    return [f"{random.choice(first_names)} {random.choice(last_names)}" for _ in range(count)]

def generate_email(names, numbers, domain):
    """Generates email IDs based on name initials and number."""
    emails = []
    for name, num in zip(names, numbers):
        initials = ''.join([part[0].lower() for part in name.split()])
        emails.append(f"{initials}{num}@{domain}")
    return emails

def generate_passwords(count: int, length: int = 10):
    """Generates a list of random passwords."""
    characters = string.ascii_letters + string.digits
    return [''.join(random.choices(characters, k=length)) for _ in range(count)]

def generate_data(start_number, num_digits, count, email_domain, output_file):
    numbers = generate_unique_numbers(start_number, num_digits, count)
    names = generate_random_names(count)
    emails = generate_email(names, numbers, email_domain)
    passwords = generate_passwords(count)
    
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Number", "Name", "Email", "Password"])
        for row in zip(numbers, names, emails, passwords):
            writer.writerow(row)
    
    print(f"CSV file '{output_file}' generated successfully!")

# Example Usage
#generate_data(start_number=31922, num_digits=7, count=64, email_domain="student.ku.edu.np", output_file="output.csv")
