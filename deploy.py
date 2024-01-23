import streamlit as st
from streamlit.components.v1 import html
import base64
import pickle
from sklearn import preprocessing
le=preprocessing.LabelEncoder()
# add a image from local computer

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover;
        filter: opacity(90%);
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
# add_bg_from_local('images/background_img.jpeg') 

# Display Page title
st.markdown("<h1 style='text-align: center; color: grey; font-family: Arial, Helvetica, sans-serif; font-style : italic; font-size : 28px;'>Automobile Application</h1>", unsafe_allow_html=True)



with st.form(key='my_form'):
    input_form=st
    # Display the input Fields 
    input_form.markdown(f'<h1 style="font-size:18px; padding: 8px 12px; margin-bottom:-55px; color : grey;">Symboling</h1>', unsafe_allow_html=True)
    input_value_0=st.selectbox(
    '',
    ('Select the Option', 0 , 1 , 2 , 3 , -1 , -2 ) , key=1
)


    input_form.markdown(f'<h1 style="font-size:18px; padding: 8px 12px; margin-bottom:-55px; color : grey;">Normalized losses</h1>', unsafe_allow_html=True)
    input_value_1=st.selectbox(
    '',
    ('Select the Option', 65 ,  74 , 77 , 78 , 81 ,  83 , 85,  87 , 89 ,  90 , 91 , 93 ,  94 ,  95 , 98 , 101 ,  102 , 103 , 104 , 106, 107 ,  108, 110 ,113, 115 , 118,  119 , 121 , 122 , 125 ,  128 ,   129 ,   134 , 137 ,  142  , 145 ,  148,  150 , 153 ,  154 , 158 , 161 , 164 , 168 ,  186, 188 , 192 , 194,  197 , 231, 256) , key=2
)
   
    input_form.markdown(f'<h1 style="font-size:18px; padding: 8px 12px; margin-bottom:-55px; color : grey;">Stroke</h1>', unsafe_allow_html=True)
    input_value_2=st.selectbox('',
    ( 'Select the Option', 2.07,2.19,2.36,2.64,2.68,2.76,2.8,2.87,2.9,3.03,3.07,3.08,3.1,3.11,3.12,3.15,3.16,3.19,3.21,3.23,3.27,3.29,3.35,3.39,3.4,3.41,3.46,3.47,3.5,3.52,3.54,3.58,3.64,3.86,3.9,4.17) , key=3
)
    input_form.markdown(f'<h1 style="font-size:18px; padding: 8px 12px; margin-bottom:-55px; color : grey;">Number of Cylinders</h1>', unsafe_allow_html=True)
    input_value_3=st.selectbox(
    '',
    ( 'Select the Option', 'four', 'six' , 'five' , 'three' , 'twelve' , 'two' , 'eight') , key=4

)


    input_form.markdown(f'<h1 style="font-size:18px; padding: 8px 12px; margin-bottom:-55px; color : grey;">Engine Type</h1>', unsafe_allow_html=True)
    input_value_4=st.selectbox(
    '',
    ( 'Select the Option', 'dohc', 'ohcv' , 'ohc' , 'l' ,  'rotor' ,  'ohcf' , 'dohcv') , key=5

)

    input_form.markdown(f'<h1 style="font-size:18px; padding: 8px 12px; margin-bottom:-55px; color : grey;">Drive Wheels</h1>', unsafe_allow_html=True)
    input_value_5=st.selectbox(
    '',
    ( 'Select the Option', 'rwd', 'fwd' , '4wd') , key=6

)

    input_form.markdown(f'<h1 style="font-size:18px; padding: 8px 12px; margin-bottom:-55px; color : grey;">Body Style</h1>', unsafe_allow_html=True)
    input_value_6=st.selectbox(
    '',
    ( 'Select the Option', 'convertible' , 'hatchback', 'sedan' , 'wagon' , 'hardtop') , key=7

)

    input_form.markdown(f'<h1 style="font-size:18px; padding: 8px 12px; margin-bottom:-55px; color : grey;">Horse Power</h1>', unsafe_allow_html=True)
    input_value_7=st.selectbox(
    '',
    ( 'Select the Option', 111 , 154 , 102 , 115 , 110 , 140 , 160 , 101 , 121 , 182 , 48 , 70 , 68 , 88 , 145 , 58 , 76 , 60 , 86 , 100 , 78 , 90 , 176 , 262 , 135 ,84, 64 , 120 , 72 , 123 , 155 , 184 , 175 , 116 , 69 , 55 , 97 , 152 , 200 , 95 , 142 , 143 , 207 , 288 , 73 , 82 , 94 , 62 , 56 , 112 , 92 , 161 , 156 , 52 , 85 , 114 , 162 , 134 , 106) , key=8

)


    input_form.markdown(f'<h1 style="font-size:18px; padding: 8px 12px; margin-bottom:-55px; color : grey;">Engine location</h1>', unsafe_allow_html=True)
    input_value_8=st.selectbox(
    '',
    ('Select the Option' , 'front', 'rear') , key=9

)

    input_form.markdown(f'<h1 style="font-size:18px; padding: 8px 12px; margin-bottom:-55px; color : grey;">fuel System</h1>', unsafe_allow_html=True)
    input_value_9=st.selectbox(
    '',
    ( 'Select the Option', '1bbl', '2bbl', '4bbl', 'idi', 'mfi', 'mpfi', 'spdi', 'spfi') , key=10

)

    input_form.markdown(f'<h1 style="font-size:18px; padding: 8px 12px; margin-bottom:-55px; color : grey;">Compression Ratio</h1>', unsafe_allow_html=True)
    input_value_10=st.selectbox(
    '',
    ('Select the Option', 7.0,7.5,7.6,7.7,7.8,8.0,8.1,8.3,8.4,8.5,8.6,8.7,8.8,9.0,9.1,9.2,9.3,9.31,9.4,9.41,9.5,9.6,10.0,10.1,11.5,21.0,21.5,21.9,22.0,22.5,22.7,23.0) , key=11

)  
    input_form.markdown(f'<h1 style="font-size:18px; padding: 8px 12px; margin-bottom:-55px; color : grey;">make</h1>', unsafe_allow_html=True)
    input_value_11=st.selectbox(
    '',
    ('Select the Option', 'alfa-romero' , 'audi' , 'bmw' , 'chevrolet' , 'dodge' , 'honda' , 'isuzu' ,'jaguar' ,
 'mazda', 'mercedes-benz' , 'mercury' , 'mitsubishi' , 'nissan' , 'peugot' ,
 'plymouth' , 'porsche' , 'renault' , 'saab' , 'subaru' , 'toyota' , 'volkswagen' ,
 'volvo') , key=13

) 
    input_form.markdown(f'<h1 style="font-size:18px; padding: 8px 12px; margin-bottom:-55px; color : grey;">Fuel Type</h1>', unsafe_allow_html=True)
    input_value_12=st.selectbox(
    '',
    ('Select the Option', 'gas', 'diesel') , key=14

) 
    input_form.markdown(f'<h1 style="font-size:18px; padding: 8px 12px; margin-bottom:-55px; color : grey;">Aspiration</h1>', unsafe_allow_html=True)
    input_value_13=st.selectbox(
    '',
    ('Select the Option', 'std' , 'turbo') , key=15

) 
    input_form.markdown(f'<h1 style="font-size:18px; padding: 8px 12px; margin-bottom:-55px; color : grey;">Bore</h1>', unsafe_allow_html=True)
    input_value_14=st.selectbox(
    '',
    ('Select the Option', 3.47 , 2.68 , 3.19 , 3.13 , 3.5 , 3.31 , 3.62 , 2.91 , 3.03 , 2.97 ,
 3.34 , 3.6 , 2.92 , 3.15 , 3.43 , 3.63 , 3.54 , 3.08  , 3.39 , 3.76 ,
 3.58 , 3.46 ,3.8 ,3.78 ,3.17 , 3.35  ,3.59 , 2.99  , 3.33 , 3.7 , 3.61 , 3.94 , 3.74 , 2.54 , 3.05 , 3.27 , 3.24 , 3.01) , key=16

) 
    input_form.markdown(f'<h1 style="font-size:18px; padding: 8px 12px; margin-bottom:-55px; color : grey;">Peak rpm</h1>', unsafe_allow_html=True)
    input_value_15=st.selectbox(
    '',
    ('Select the Option', 5000 , 5500 , 5800 , 4250 , 5400 , 5100 , 4800 , 6000, 4750 , 4650 ,
 4200 , 4350 , 4500 , 5200 , 4150 , 5600 ,5900 , 5750 , 5250 , 4900 ,4400 , 6600 , 5300) , key=17

)    
    input_form.markdown(f'<h1 style="font-size:18px; padding: 8px 12px; margin-bottom:-55px; color : grey;">number of Doors</h1>', unsafe_allow_html=True)
    input_value_16=st.selectbox(
    '',
    ('Select the Option', 0 , 1, 2) , key=18

) 
    submit=st.form_submit_button(label='Submit')
    if submit:
        if input_value_0== 'Select the Option' and input_value_1== 'Select the Option' and input_value_2== 'Select the Option' and input_value_3== 'Select the Option' and input_value_4== 'Select the Option' and input_value_5== 'Select the Option' and input_value_6== 'Select the Option' and input_value_7== 'Select the Option' and input_value_8== 'Select the Option' and input_value_9== 'Select the Option' and input_value_10== 'Select the Option' and input_value_11== 'Select the Option' and input_value_12== 'Select the Option' and input_value_13== 'Select the Option' and input_value_14== 'Select the Option' and input_value_15== 'Select the Option':
            my_js = """alert("Kindly Fill the All input fields");"""
            # Wrapt the javascript as html code
            my_html = f"<script>{my_js}</script>"
            html(my_html)
        else:
            if input_value_3== 'four':
                input_value_3=0
            elif input_value_3== 'six': 
                input_value_3=1
            elif input_value_3== 'five' :
                input_value_3=2 
            elif input_value_3== 'three':
                input_value_3=3
            elif input_value_3== 'twelve':
                input_value_3=4
            elif input_value_3== 'two' :
                input_value_3=5
            elif input_value_3== 'eight' : 
                input_value_3=6
               
            if input_value_4== 'dohc':
                input_value_4=0
            elif input_value_4== 'ohcv': 
                input_value_4=1
            elif input_value_4=='ohc' :
                input_value_4=2 
            elif input_value_4== 'l' :
                input_value_4=3
            elif input_value_4== 'rotor':
                input_value_4=4
            elif input_value_4==  'ohcf' :
                input_value_4=5
            elif input_value_4=='dohcv' : 
                input_value_4=6
            
            if input_value_5== 'rwd':
                input_value_5=0
            elif input_value_5== 'fwd': 
                input_value_5=1
            elif input_value_5=='4wd' :
                input_value_5=2  
                
                
            if input_value_6== 'convertible':
                input_value_6=0
            elif input_value_6=='sedan': 
                input_value_6=1
            elif input_value_6== 'wagon' :
                input_value_6=2 
            elif input_value_6== 'hardtop' :
                input_value_6=3
                
             
            if input_value_8== 'front':
                input_value_8=0
            elif input_value_8== 'rear': 
                input_value_8=1
            
            if input_value_9== '1bbl':
                input_value_9=0
            elif input_value_9== '2bbl': 
                input_value_9=1
            elif input_value_9== '4bbl' :
                input_value_9=2 
            elif input_value_9== 'idi':
                input_value_9=3
            elif input_value_9== 'mfi':
                input_value_9=4
            elif input_value_9== 'mpfi' :
                input_value_9=5
            elif input_value_9== 'spdi' : 
                input_value_9=6  
            elif input_value_9== 'spfi' : 
                input_value_9=7  
            

 
            if input_value_11== 'alfa-romero':
                input_value_11=0
            elif input_value_11==  'audi': 
                input_value_11=1
            elif input_value_11== 'bmw' :
                input_value_11=2 
            elif input_value_11=='chevrolet':
                input_value_11=3
            elif input_value_11== 'dodge':
                input_value_11=4
            elif input_value_11== 'honda' :
                input_value_11=5
            elif input_value_11== 'isuzu' : 
                input_value_11=6  
            elif input_value_11=='jaguar' : 
                input_value_11=7 
            if input_value_11== 'mazda':
                input_value_11=8
            elif input_value_11== 'mercedes-benz' : 
                input_value_11=9
            elif input_value_11== 'mercury' :
                input_value_11=10 
            elif input_value_11==  'mitsubishi':
                input_value_11=11
            elif input_value_11== 'nissan':
                input_value_11=12
            elif input_value_11=='peugot' :
                input_value_11=13
            elif input_value_11== 'plymouth' : 
                input_value_11=14  
            elif input_value_11=='porsche' : 
                input_value_11=15 
            if input_value_11== 'renault':
                input_value_11=16
            elif input_value_11== 'saab': 
                input_value_11=17
            elif input_value_11== 'subaru' :
                input_value_11=18 
            elif input_value_11==  'toyota':
                input_value_11=19
            elif input_value_11== 'volkswagen':
                input_value_11=20
            elif input_value_11== 'volkswagen' :
                input_value_11=21
            elif input_value_11== 'volvo' : 
                input_value_11=22  
            
            if input_value_12== 'gas':
                input_value_12=0
            elif input_value_12== 'diesel': 
                input_value_12=1
                
            if input_value_13== 'std':
                input_value_13=0
            elif input_value_13== 'turbo': 
                input_value_13=1
                
            
            model_auto=pickle.load(open('auto_model.pkl' , 'rb'))
            



            inputs=[[input_value_0 , input_value_1 , input_value_2 , input_value_3 , input_value_4 , input_value_5 , input_value_6 , input_value_7 , input_value_8 , input_value_9 , input_value_10 , input_value_11 , input_value_12 , input_value_13 , input_value_14 , input_value_15 , input_value_16]]
            prediction=model_auto.predict(inputs)
            st.write(prediction)
            