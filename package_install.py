# reads the file requirements.txt
# install each and every python package
import os

with open("requirements.txt", 'r+') as f:
    package_name = f.read()
    list_of_packages = package_name.split('\n')
i, j = 0, len(list_of_packages) - 1
for package_name in list_of_packages:
    print(f"Package {i} of {j} installing")
    os.system(f"pip3 install {package_name}")
    print(f"Package {i} of {j} installed")
    i+=1