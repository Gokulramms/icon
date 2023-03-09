!pip install streamlit_lottie
import streamlit_lottie
import streamlit as st
import pandas as pd
import json 
import requests
from streamlit_lottie import st_lottie
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def load_lottieurl(url:str):
	r= requests.get(url)
	if r.status_code != 200:
		return None
	return r.json()

glob=load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_s8okgady.json")
st_lottie(glob,key="___")
st.title("WHICH CAREER IS BEST FOR YOU...?")

#SET OF QUESTION AS LIST
G=["I like to work on cars : ","I like to build things : ","I like to do experiments : ","I like to take care of animals : ","I like to cook : ","I am a practical person : ","I like working outdoors : "]
K=["I like to do puzzles : ","I like to do experiments : ","I enjoy science : "," I enjoy trying to figure out how thinks work: "," I like to analyze things (problems\situations):","I like working with numbersor charts : "," I’m good at math : "]
A=["I am good at working independently : "," I like to read about art and music : ","I enjoy creative writing : ","I am a creative person : ","I like to play instruments or sing : ","I like acting in plays : ","I like to draw : "]
D=["I like to work in teams : ","I like to teach or train people : ","I like trying to help people solve their problems : ","I am interested in healing people : ","I enjoy learning about other cultures : ","I like to get into discussions about issues : ","I like helping people : "]
M=["I am an ambitious person(I set goals for myself):"," I like to try to influence or persuade people : ","I like selling things : ","I am quick to take on new responsibilities : ","I would like to start my own business: ","I like to lead: "]
J=[" I like to organize things(files, desks/offices): ","I like to have clear instructions to follow: ","I wouldn’t mind working 8 hours per day in an office: ","I pay attention to details: ","I like to do filing or typing : ","I am good at keeping records of my work: "," I would like to work in an office :"]
st.write("*"*70)
st.header("Hello Guys Welcome to our project")
st.write("*"*70)
name=st.text_input('Enter your Name: ',' ')
gmail=st.text_input('Enter your Email:',' ')
Age=st.slider('How old are you?', 10, 100, 18)
st.subheader("\nIf you are interest in the content of the question , select 'Yes' or 'No'")

current=[]
countG=0
countK=0
countA=0
countD=0
countM=0
countJ=0
ans=f'''HELLO MR/MRS {name} , THANKYOU FOR WISITING OUR WEBSITE.
SHARE THIS WEBSITE TO YOUR FRIENDS SO THAT THEY CAN ABLE TO GET CLARIFY ON THIER CAREER.'''
#USER INPUT OPTION
df = pd.DataFrame({
	'option':["Yes","No"]
	})

if st.checkbox("Let's Begin:"):

	for i in G:#GETTING ANSWER FORM THE USER 
		oppr=st.selectbox(
			i,
			df['option']
		)
		if oppr=="Yes":   # IF THE ANSWER IS TRUE BELOW CODE EXECUTED
			countG=countG+1  #INCRIMENT COUNT_R WITH ONE
		current.append(countG) #APPENDING COUNT TO CURRENT LIST
	if st.checkbox("Next-->"):

		for i in K:
			I_opp=st.radio(
				i,
				df['option']
			)
			if I_opp=="Yes":
				countK=countK+1    #INCRIMENT COUNT_I WITH ONE
			current.append(countK)  #APPENDING COUNT TO CURRENT LIST
		if st.checkbox("Next->"):

			for i in A:
				oppa=st.radio(
					i,
					df['option']
				)
				if oppa=="Yes":
					countA=countA+1    #INCRIMENT COUNT_A WITH ONE
				current.append(countA)  #APPENDING COUNT TO CURRENT LIST
			if st.checkbox(" Next-->"):

				for i in D:
					opps=st.radio(
						i,
						df['option']
					)
					if opps=="Yes":
						countD=countD+1    #INCRIMENT COUNT_S WITH ONE
					current.append(countD)  #APPENDING COUNT TO CURRENT LIST
				if st.checkbox("Next--> "):
					for i in M:
						oppc=st.radio(
							i,
							df['option']
						)
						if oppc=="Yes":
							countM=countM+1   #INCRIMENT COUNT_C WITH ONE
						current.append(countM) #APPENDING COUNT TO CURRENT LIST
					if st.checkbox("Next-->  "):
						for i in J:
							oppe=st.radio(
								i,
								df['option']
							)
							if oppe=="Yes":
								countJ=countJ+1   #INCRIMENT COUNT_E WITH ONE
							current.append(countJ)  #APPENDING COUNT TO CURRENT LIST

						if st.button("Get Your Result-->"):
							max=max(current)
							if max==countG :
								
								st.title('''Related Pathways--> Natural Resources,Health Services,Industrial and Engineering Technolog''')
								nat=load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_ocyegDP2iy.json")
								st_lottie(nat, key="Natural Resources")
								ind=load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_dj2iGEFiUX.json")
								st_lottie(ind, key="Industry field")
								
							elif max==countK:
							
								st.title('''Related Pathways--> Health Services,Business,Public and Human Service''')
								health=load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_ssjAlSigs7.json")
								st_lottie(health, key="Health")
								buisness=load_lottieurl("https://assets6.lottiefiles.com/private_files/lf30_jui5y7ab.json")
								st_lottie(buisness, key="Buisness ")
							elif max==countA:
							
								st.title('''Related Pathways--> Public and Human Services,Arts and Communication''')
								public=load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_fUq9u8VGIo.json")
								st_lottie(public, key=="Public ")
								arts=load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_iqhd0uv0.json")
								st_lottie(arts, key=" Arts")
								
							elif max==countD:
								
								st.title('''Related Pathways--> Health Service,Public and Human Services''')
								health=load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_ssjAlSigs7.json")
								st_lottie(health, key="Health")
								nat=load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_ocyegDP2iy.json")
								st_lottie(nat, key="Natural resources ")
		
								
							elif max==countM:
								
								st.title('''Related Pathways--> Buisness,Arts and Communication''')
								buisness=load_lottieurl("https://assets6.lottiefiles.com/private_files/lf30_jui5y7ab.json")
								st_lottie(buisness, key="Buisness ")
								communication=load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_jvj9d2lc.json")
								st_lottie(communication, key=" Communication")
								
							else:
							
								st.title('''Related Pathways--> Health Services,Business,Industrial and Engineering ,Technology''')
								eng=load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_ic7oz9ip.json")
								st_lottie(eng, key=" Engineering")
								ind=load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_dj2iGEFiUX.json")
								st_lottie(ind, key="Industry field ")

							send='iconcreationai81@gmail.com'
							pas='tetkkfrshnidygvq'
							rec=gmail
							message=MIMEMultipart()
							message['From']=send
							message['To']=rec
							message['Subject']='WHICH CAREER IS BEST FOR YOU...'
							message.attach(MIMEText(ans,'plain'))
							session=smtplib.SMTP('smtp.gmail.com',587)
							session.starttls()
							session.login(send,pas)
							text=message.as_string()
							session.sendmail(send,rec,text)
							session.quit()
							st.subheader('Mail sent')
