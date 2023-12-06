import fitz

doc = fitz.open("merged.pdf")

index = 0
for page in doc:
    index = index + 1
    has_text = False
    has_images = False
    has_vector_graphics = False
    if len(page.get_images()) > 0:
        has_images = True
    if page.get_text() != "":
        has_text = True
    if len(page.get_drawings()) > 0:
        has_vector_graphics = True
    
    if has_images and has_text == False and has_vector_graphics == False:
        print("Page "+str(index)+" is raster")
    elif has_vector_graphics or has_text:
        print("Page "+str(index)+" is vector")
        