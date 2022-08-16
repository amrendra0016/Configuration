from configparser import ConfigParser

# Creating object of ConfigParser

configur=ConfigParser()
configur.read("config.ini")

#Accessing values from config.ini file
print("Kafka Project Path =", configur.get('paths','kafka_project'))
print("Datatype of Kafka Project Path ",type(configur.get('paths','kafka_project')))

print("Age =", configur.getint('information','age'))
print("Data Type of Age using getint = ",type(configur.getint('information','age')))
print("Data Type of Age using just get = ",type(configur.get('information','age')))

# Accessing data using wrong get command will throw error
# print("Age ",configur.getboolean('information','age'))

print("Address =",configur.get('information','Address'))
print("Data Type of Address = ",type(configur.get('information','Address')))

# Accesing boolean type
print("Is Indian =", configur.get('information','Indian'))
print("Data type using just get to access boolean type. 'Is Indian' =", type(configur.get('information','Indian')))
print("Data type using just getboolean to access boolean type. 'Is Indian' =", type(configur.getboolean('information','Indian')))

# Updating config.ini file
print(configur.set('information','Age','28'))
# After updating value we need to write it into the file.
with open('config.ini', 'w') as configfile:
    configur.write(configfile)

print("\nPrinting All the sections " )
print(configur.sections())


# To add new sections and values create new object and don't read the file because if we read the file and than
# add the section it will also add previous section.
parser=ConfigParser()

print("\nAdding new Section in config.ini file")
print(parser.add_section('international information'))

print("\nAdding value to newly added Section in config.ini file")
print(parser.set('international information','NRI','0'))
print(parser.set('international information','Salary','21.46'))

# We can add section and values like this also
"""parser['international information']={
    'NRI':'0',
    'Salary':'21.46'
}
"""

with open('config.ini', 'a') as configfile:
    parser.write(configfile)

print("Printing to console what we are writing to file.")
import sys
parser.write(sys.stdout)

print("Reading the new added values")
configur=ConfigParser()
configur.read("config.ini")
print("NRI =", configur.getboolean('international information','NRI'))
print("Salary =", configur.getfloat('international information','Salary'))