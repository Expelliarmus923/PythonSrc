import Image
im = Image.open('test.jpg')
print im.format,im.size,im.mode
im.thumbnail((200,200))
im.save('thumb.jpg','JPEG')

