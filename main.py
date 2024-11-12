import importlib
import subprocess
import sys

def install_and_import(package):
    try:
        # Try importing the package
        module = importlib.import_module(package)
        print(f"{package} {module.__version__} is already installed.")
    except ImportError:
        # If not installed, install the package and import it
        print(f"{package} not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        module = importlib.import_module(package);
        print(package, module.__version__)
    return module



# Example usage with common data science modules
pandas = install_and_import('pandas')
numpy = install_and_import('numpy')
matplotlib = install_and_import('matplotlib')
seaborn= install_and_import("seaborn")
# Now you can use pandas, numpy, and matplotlib as usual
#print(pandas.__version__)
