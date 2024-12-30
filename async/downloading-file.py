import requests

# URL of the file you want to download
url = "https://example.com/somefile.zip"

try:
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Raise an exception if the response status code is not 200 (OK)
    response.raise_for_status()
    
    
    print("File downloaded successfully!")
    

except Exception as e:
    # Catch any other errors that may occur
    print(f"An unexpected error occurred: {e}")


print("i kept going , im still running , after errors ")