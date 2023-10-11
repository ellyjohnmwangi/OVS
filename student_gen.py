import csv

import faker

fake = faker.Faker()

csv_file = 'student_records.csv'
num_records = 10

with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['first_name', 'last_name', 'email', 'password'])

    for _ in range(num_records):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        password = fake.password(length=12, special_chars=True, digits=True, upper_case=True, lower_case=True)

        writer.writerow([first_name, last_name, email, password])

print(f"{num_records} sample student records generated and saved to '{csv_file}'.")
