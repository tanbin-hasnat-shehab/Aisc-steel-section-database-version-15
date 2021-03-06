
import streamlit as st
from openpyxl import load_workbook
from reportlab.pdfgen import canvas
from PyPDF2 import PdfFileWriter, PdfFileReader
my_pdf=canvas.Canvas('temp.pdf')
@st.cache

def about():
    st.write(
        '''
        contact email - tanbinhasnat04@gmail.com
        ''')


def main():
	st.set_page_config(layout="wide")
	
	def caln():
		prop_arr=[]
		for i in range(1,86):
			name_tr=sheet.cell(row=1,column=i).value
			prop_arr.append(name_tr)
		prop=st.selectbox('Select or write property',prop_arr)
		st.markdown(f"""# you selected  {section}""")
		if section in name_tr_label:
			indi_name=name_tr_label.index(section)+1
		if prop in prop_arr:
			prop_name=prop_arr.index(prop)+1
			
			
		st.markdown(f"""# value : {prop} = {sheet.cell(row=indi_name,column=prop_name).value}""")


		j=0
		for i in range(4,90):
			st.write(f'{prop_arr[j]} = {sheet.cell(row=indi_name,column=i-3).value}')
			j+=1
		
		
	

	st.title("Aisc database version - v15 : ")
    

	activities = ["Home", "About"]
	choice = st.sidebar.selectbox("Pick something fun", activities)

	if choice == "Home":

        
		wb=load_workbook('aisc.xlsx')
		sheet=wb.active
		names=[]

	
		name_tr_label=[]
		for i in range(1,len(sheet['A'])+1):
			if i==1:
				name_tr_label.append('')
			else:
				name_tr=sheet.cell(row=i,column=3).value
				name_tr_label.append(name_tr)
		section=st.selectbox('Select or write section',name_tr_label)
		caln()

		
        

	elif choice == "About":
		
		about()



if __name__ == "__main__":
	main()

