import PyPDF2
import sys

inputs = sys.argv[1:]

def pdf_combiner(pdf_list):
	merger = PyPDF2.PdfFileMerger()
	for pdf in pdf_list:
		print(pdf)
		merger.append(pdf)
	merger.write('super.pdf')



pdf_combiner(inputs)


#rb - converts the file objects into binary mode 
#with open('Fashion tickets.pdf', 'rb') as file: 
	#reader = PyPDF2.PdfFileReader(file)
	#print(reader.numPages) #gives the number of pages in the pdf
	#print(reader.getPage(0))
	#page = reader.getPage(0)
	#print(page.rotateCounterClockwise(90))
	#writer = PyPDF2.PdfFileWriter()
	#writer.addPage(page)
	#with open('tilt.pdf', 'wb') as new_file:
		#writer.write(new_file)

