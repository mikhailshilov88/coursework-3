from utils import load_data, filter_sort, formatted_data

JSONE_FILE = 'operations.json'


def main():
    data = load_data(JSONE_FILE)
    data = filter_sort(data)

    for i in range(5):
        print(formatted_data(data[i]))

if __name__ == '__main__':
    main()
