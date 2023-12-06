import fitz

doc_a = fitz.open("vector.pdf") # open the 1st document
doc_b = fitz.open("raster.pdf") # open the 2nd document

doc_a.insert_pdf(doc_b) # merge the docs
doc_a.save("merged.pdf") # save the merged document with a new filename