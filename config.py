from configparser import ConfigParser

def config(filename='database.ini', section='postgresql'):
    '''This Function reads the database.ini and make configuration dict'''
    parser = ConfigParser()
    parser.read(filename)

    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'. format(section, filename))
    
    return db

