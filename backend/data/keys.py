import base64 
private_key = "m][638R)CnfPILdNIw15qEH7CJm(2#)."
orders_endpoint = "https://api.quickbutik.com/v1/orders"

auth_str = f"{private_key}:{private_key}"
# Base64 encode the auth string
auth_bytes = auth_str.encode('utf-8')
encoded_auth = base64.b64encode(auth_bytes).decode('utf-8')