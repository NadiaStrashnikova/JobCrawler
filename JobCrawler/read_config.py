from configparser import ConfigParser
import os

file_directory = os.path.dirname(os.path.abspath(__file__))


def read_config_file(filename='config.ini', section='mysql'):
    parser = ConfigParser()

    if parser.read(os.path.join(file_directory, filename)):
        db_config = {}
        if parser.has_section(section):
            items = parser.items(section)
            for item in items:
                db_config[item[0]] = item[1]
            return db_config
        else:
            raise Exception(f'There is no such {section} in the {filename} file')
    else:
        raise Exception(f'File not found: {filename}')


if __name__ == '__main__':
    db_config = read_config_file('config.ini','mysql')
    print(db_config)
