import json
import argparse


def load_data(filepath):
    return json.load(open(filepath, 'r', encoding='UTF8'))['features']


def pretty_print_json(json_data):
    return json.dumps(json_data, indent=4, ensure_ascii=False)


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
        json_data = load_data(params.filepath)
    except ValueError as e:
        print('Не могу прочитать данные из файла {}'.format(params.filepath))
        exit()
    except OSError as e:
        print('Файл {} не существует '.format(params.filepath))
        exit()
    
    try:
        print(pretty_print_json(json_data))
    except ValueError:
        print('Decoding JSON has failed')
