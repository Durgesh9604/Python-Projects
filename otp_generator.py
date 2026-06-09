import random

print("*" * 35)
print("WELCOME TO OTP GENERATOR")
print("*" * 35)

def otp_generator():
    generated_otp = random.randint(100000, 999999)

    print(f"Generated OTP: {generated_otp}")

    try:
        user_otp = int(input("Enter the OTP: "))

        if user_otp == generated_otp:
            print("Correct OTP 👌")
        else:
            print("Wrong OTP ❌")

    except ValueError:
        print("Please enter numbers only.")

otp_generator()