import requests
import json

def get_instance_metadata(key):
    base_url = "http://169.254.169.254/latest/meta-data/"
    response = requests.get(base_url + key)
    return response.text

def main():
    key = "instance-id"  # Example key
    metadata_value = get_instance_metadata(key)
    
    metadata_json = {key: metadata_value}
    print(json.dumps(metadata_json, indent=4))

if __name__ == "__main__":
    main()


