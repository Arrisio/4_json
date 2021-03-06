import json
import argparse


def load_data(filepath):
    with open(filepath, 'r', encoding='UTF8') as file_handler:
        return json.load(file_handler)


def pretty_print_json(loaded_json):
    print(json.dumps(loaded_json, indent=4, ensure_ascii=False))


def parse_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-f', action='store',
        dest='filepath',
        help='Filepath with data, "alco_shops.json" by default',
        default='alco_shops.json'
    )

    return parser.parse_args()


if __name__ == '__main__':
    params = parse_arguments()

    try:
        loaded_json = load_data(params.filepath)
    except ValueError:
        exit('Не могу прочитать данные из файла {}'.format(params.filepath))
    except OSError:
        exit('Файл {} не существует '.format(params.filepath))
    else:
        pretty_print_json(loaded_json)
