from salary_data import total_salary

def main():
    path = "salaries.txt"
    total, average = total_salary(path)
    if total > 0:
        print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
    else:
        print("Could not process salary data.")


if __name__ == "__main__":
    main()



