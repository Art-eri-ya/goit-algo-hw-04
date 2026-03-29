def get_cats_info(path : str) -> list[dict]:
    cats_info_list = []
    keys = ["id", "name", "age"]

    try:
        with open(path, 'r', encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(',')
                cat_dict = dict(zip(keys, parts))
                cats_info_list.append(cat_dict)

        return cats_info_list

    except FileNotFoundError:
        print("Error: The cats' information file was not found.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []


if __name__ == "__main__":
    cats = get_cats_info("cats_info.txt")
    from pprint import pprint

    pprint(cats, sort_dicts=False)