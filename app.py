from checker import check_password_strength
from generator import generate_password
from report import save_report


def show_menu():
    print("\n" + "=" * 50)
    print("PASSWORD STRENGTH CHECKER")
    print("=" * 50)
    print("1. Check password strength")
    print("2. Generate strong password")
    print("3. Exit")


def check_password_flow():
    password = input("\nEnter password to check: ").strip()

    if not password:
        print("Password cannot be empty.")
        return

    result = check_password_strength(password)

    print("\n--- RESULT ---")
    print(f"Password : {result['password']}")
    print(f"Length   : {result['length']}")
    print(f"Score    : {result['score']}/6")
    print(f"Strength : {result['strength']}")
    print(f"Entropy  : {result['entropy_bits']} bits")
    print("Feedback :")
    for item in result["feedback"]:
        print(f"- {item}")

    save_report(result)
    print("\nReport saved to report.txt")


def generate_password_flow():
    try:
        length = int(input("\nEnter password length (minimum 8): ").strip())
        password = generate_password(length)
        result = check_password_strength(password)

        print("\nGenerated Password:", password)
        print(f"Strength: {result['strength']}")
        print(f"Score   : {result['score']}/6")
        print(f"Entropy : {result['entropy_bits']} bits")

        save_report(result)
        print("\nGenerated password report saved to report.txt")
    except ValueError as e:
        print(f"Error: {e}")


def main():
    while True:
        show_menu()
        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            check_password_flow()
        elif choice == "2":
            generate_password_flow()
        elif choice == "3":
            print("Exiting program. Goodbye.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
