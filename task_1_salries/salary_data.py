def total_salary(path):
    total = 0
    count = 0
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                if line.strip():
                    _, salary = line.strip().split(",")
                    total += float(salary)
                    count += 1
            average = total / count if count > 0 else 0
            return total, average
    except FileNotFoundError:
        return "No salaries file found."
        return 0, 0
    except ValueError:
        return "No salaries file found."
        print("Error: The file contains invalid data.")
        return 0, 0

