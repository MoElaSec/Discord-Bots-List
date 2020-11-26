import configparser
import collections

# to read the bot config data
config = configparser.RawConfigParser()
config.read('bot_info.cfg')


def get_config_section():
    """Reading cfg file with configparser module and storing/return info inside a dict"""
    if not hasattr(get_config_section, 'section_dict'):
        get_config_section.section_dict = collections.defaultdict()

        for section in config.sections():
            get_config_section.section_dict[section] = dict(config.items(section))

    return get_config_section.section_dict
