# Old version
file = open('youtube.txt', 'w')
try:
    file.write("This file is created automatically")
except:
    pass
finally:
    file.close()


# Updated version
with open('youtube.txt', 'w') as file:
    file.write('File Handling Using Python') 