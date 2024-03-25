import subprocess

def install_dependencies():
    # Read the list of dependencies from the requirements.txt file
    with open('requirements.txt', 'r') as file:
        dependencies = [line.strip() for line in file.readlines()]

    # Install each dependency using pip
    for dependency in dependencies:
        subprocess.call(['pip', 'install', dependency])

    print("All dependencies installed successfully.")

if __name__ == "__main__":
    install_dependencies()
