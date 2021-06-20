import streamlit as st
from openpyxl import load_workbook

def about():
    st.write(
        '''
        contact email - tanbinhasnat04@gmail.com
        ''')


def main():
	def caln():
		section = st.text_input("Section Name")
		prop = st.text_input("Property Name")
		section.upper()
		print(section)

		indi_name=0
		if section in names:
			indi_name=names.index(section)+1
		if section in name_tr_label:
			indi_name=name_tr_label.index(section)+1
		
		
		
		for i in range(1,86):
			if prop==sheet.cell(row=1,column=i).value:
				indi_prop=i
				break
        
		try:
			if indi_name!=0:
				st.write(f'''Value : {sheet.cell(row=indi_name+1,column=indi_prop).value}''')
			else:
				st.write('Could not found')
				
		except:
			st.write('Could not found')
	st.title("Aisc database version - v15 : ")
    

	activities = ["Home", "About"]
	choice = st.sidebar.selectbox("Pick something fun", activities)

	if choice == "Home":

        
		wb=load_workbook('aisc.xlsx')
		sheet=wb.active
		names=[]

		for i in range(1,len(sheet['A'])+1):
			name_tr=sheet.cell(row=i+1,column=2).value
			names.append(name_tr)
		name_tr_label=[]
		for i in range(1,len(sheet['A'])+1):
			name_tr=sheet.cell(row=i+1,column=3).value
			name_tr_label.append(name_tr)
        

		caln()
        

	elif choice == "About":
		about()




if __name__ == "__main__":
	main()

