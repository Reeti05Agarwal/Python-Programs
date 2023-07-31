import importlib.util

# For illustrative purposes.
package_name = 'pyttsx3'

spec = importlib.util.find_spec(pyttsx3)
if spec is None:
    print(pyttsx3 +" is not installed")
