def save_report(result: dict, filename: str = "report.txt") -> None:
    with open(filename, "a", encoding="utf-8") as file:
        file.write("=" * 50 + "\n")
        file.write("PASSWORD STRENGTH REPORT\n")
        file.write("=" * 50 + "\n")
        file.write(f"Password: {result['password']}\n")
        file.write(f"Length: {result['length']}\n")
        file.write(f"Score: {result['score']}/6\n")
        file.write(f"Strength: {result['strength']}\n")
        file.write(f"Entropy: {result['entropy_bits']} bits\n")
        file.write("Feedback:\n")

        for item in result["feedback"]:
            file.write(f"- {item}\n")

        file.write("\n")
