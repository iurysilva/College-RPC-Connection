import xmlrpc.client

with xmlrpc.client.ServerProxy("http://68.183.143.117:8000/") as proxy:
    with open("urso.jpg", "rb") as handle:
        binary_data = xmlrpc.client.Binary(handle.read())
    print("Sending image to server")
    response = proxy.image_compression(binary_data)
    print("Received compressed image, saving...")
    with open("compressed_image.jpg", "wb") as handle:
        handle.write(response.data)
    print("Done")