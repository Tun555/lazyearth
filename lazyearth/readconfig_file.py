# import numpy
# import configparser

# class reader:
#     def __init__(self,config_file=None):
#         self.config = self.load_config_file(config_file)
#     def load_config_file(self,config_file):
#         if config_file:
#             self._config_file = config_file
#         print(f"Yoh loading configuration file {self._config_file}")
#         config = configparser.ConfigParser()
#         config.read(self._config_file)
#         return config
#     def get_value(self,section,key):
#         return self.config.get(section,key)
    

# test = reader(r'I:\My Drive\MyLibrary\lazyearth\Upload to PyPI\lazyearth\lazyearth.ini')
# print(test.get_value('water','water_mask'))



# from lazyearth.mainfile import objearth

from configparser import ConfigParser

file = 'lazyearth.ini'
config = ConfigParser()
config.read(file)

fractionconstant = float(config['Plot']['fractionnumber'])
print(fractionconstant)

