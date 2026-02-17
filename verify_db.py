import urllib.request
import urllib.error
import json

BASE_URL = "http://127.0.0.1:8001"

def make_request(endpoint, method="GET", data=None):
    url = f"{BASE_URL}{endpoint}"
    headers = {"Content-Type": "application/json"}
    
    if data:
        data_bytes = json.dumps(data).encode("utf-8")
    else:
        data_bytes = None

    req = urllib.request.Request(url, data=data_bytes, headers=headers, method=method)
    
    try:
        with urllib.request.urlopen(req) as response:
            status = response.getcode()
            response_data = response.read().decode("utf-8")
            try:
                json_data = json.loads(response_data)
            except json.JSONDecodeError:
                json_data = response_data
            
            print(f"Status: {status}")
            print(f"Response: {json_data}")
            return status, json_data
    except urllib.error.HTTPError as e:
        print(f"Status: {e.code}")
        print(f"Response: {e.read().decode('utf-8')}")
        return e.code, None
    except urllib.error.URLError as e:
        print(f"Error: {e.reason}")
        return None, None

def test_create_item():
    print("Testing CREATE item...")
    payload = {"name": "Test Item", "quantity": 10}
    status, data = make_request("/items", "POST", payload)
    if status == 200 and data:
        return data.get("id")
    return None

def test_read_items():
    print("\nTesting READ ALL items...")
    make_request("/items", "GET")

def test_read_item(item_id):
    print(f"\nTesting READ ONE item (ID: {item_id})...")
    make_request(f"/items/{item_id}", "GET")

def test_update_item(item_id):
    print(f"\nTesting UPDATE item (ID: {item_id})...")
    payload = {"name": "Updated Test Item", "quantity": 20}
    make_request(f"/items/{item_id}", "PUT", payload)

def test_patch_item(item_id):
    print(f"\nTesting PATCH item (ID: {item_id})...")
    # Only update quantity, name should remain same
    payload = {"quantity": 50}
    make_request(f"/items/{item_id}", "PATCH", payload)

def test_delete_item(item_id):
    print(f"\nTesting DELETE item (ID: {item_id})...")
    make_request(f"/items/{item_id}", "DELETE")

if __name__ == "__main__":
    print("Starting verification...")
    # Clean up previous runs if possible? No, just add new item.
    
    item_id = test_create_item()
    if item_id:
        test_read_items()
        test_read_item(item_id)
        test_update_item(item_id)
        test_patch_item(item_id)
        test_delete_item(item_id)
        test_read_items() # Should be empty or not contain the deleted item
    else:
        print("Failed to create item, skipping other tests.")
