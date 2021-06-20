
import streamlit as st
from openpyxl import load_workbook

def about():
    st.write(
        '''
        contact email - tanbinhasnat04@gmail.com
        ''')


def main():
	

	st.title("Aisc database version - v15 : ")
    

	activities = ["Home", "About"]
	choice = st.sidebar.selectbox("Pick something fun", activities)

	if choice == "Home":

        
		wb=load_workbook('aisc.xlsx')
		sheet=wb.active
		names=[]

	
		name_tr_label=[]
		for i in range(1,len(sheet['A'])+1):
			name_tr=sheet.cell(row=i+1,column=3).value
			name_tr_label.append(name_tr)
    	#######
	result=st.selectbox('Select or write section',name_tr_label)
	st.write(f'you selected {result}')

		
        

	elif choice == "About":
		
		about()



if __name__ == "__main__":
	main()

