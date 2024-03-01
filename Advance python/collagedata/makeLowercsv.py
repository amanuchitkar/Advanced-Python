import pandas as pd

# Replace 'your_file.csv' with the actual path to your CSV file
file_path = 'collagedata\Collage Email ID Genrating file.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

def Update_Gmail(email):
    # if email!=email.lower():
    #     print(email)
    email=email.lower()
    parts=email.split("@")
    # print(parts[1])
    if len(parts)==2:
        username,domain=parts
        # print(domain)
        if domain.strip() !="dbatu.ac.in":
            # print(username)
            return f"{username}@dbatu.ac.in"
    return email
# def is_weakPassword(password):
#     return(
#         any(char.isdigit() for char in password),
#         any(char.isupper() for char in password),
#         any(char.islower() for char in password),
#         any(char.isdigit() for char in password),
#         )
# Update_Gmail(df['Email Address [Required]'])
# Apply the function to the 'Gmail' column
df['Email Address [Required]'] = df['Email Address [Required]'].apply(Update_Gmail)
# df['Password [Required]']=df['Password [Required]'].apply(is_weakPassword)['Password [Required]']
# print(df['Email Address [Required]'],df['Password [Required]'])
# print(df['Password [Required]'])

# # Save the updated DataFrame to a new CSV file
output_file_path = 'output_file.csv'
df.to_csv(output_file_path, index=False)

# print(f"Conversion complete. Updated data saved to {output_file_path}")