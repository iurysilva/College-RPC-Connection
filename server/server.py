from xmlrpc.server import SimpleXMLRPCServer
from PIL import Image
import xmlrpc.client

def image_compression(arg):
    with open("server/image.jpg", "wb") as handle:
        handle.write(arg.data)
    image = Image.open('server/image.jpg')
    print("Received image, doing compression...")
    image.save('server/compressed_image.jpg',quality=20,optimize=True)
    print("Sending compressed image back")
    with open("server/compressed_image.jpg", "rb") as handle:
        binary_data = xmlrpc.client.Binary(handle.read())
    return binary_data



server = SimpleXMLRPCServer(("192.168.100.35", 8000))

print("Listening on port 8000...")

server.register_function(image_compression, "image_compression")
server.serve_forever()