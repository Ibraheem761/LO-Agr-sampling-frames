import numpy as np
import pandas as pd
import streamlit as st
import altair as alt



df_en = pd.read_excel('Base_sondage_maraichage.xlsx',na_values=['NA'], sheet_name=1)

df_en = df_en.fillna({"Irrigation_mode": "Pluvial"})


df_en = df_en.replace(to_replace ="Great Tunel",value ="Big Tunel")

df_en = df_en.replace(to_replace ="Great Tunel",value ="Big Tunel")
df_en = df_en.replace(to_replace ="Under floor",value ="Understorey")


html_temp = """
    <div class='octopusheader' style="background-color:ghostwhite;padding:10px 20px;margin-bottom: 25px">
    <h1 style="color:black;text-align:center;">Market Gardening Sampling</h1>
    <p style="color:black;text-align:left;" ><b>Goal:</b> Analyze a population by applying different sampling designs with the aim of choosing the most proper one for future surveys.</p>
    
    <ul style="padding-left: 40px">
  <li>Random sampling</li>
  <li>Systematic sampling</li>
  <li>Double sampling</li>
  <li>Probability-Proportional-to-size sampling (PPS)</li>
  <li>Stratified sampling</li>
    </ul>  
    
    <img style='display: block; margin: 0 auto' src="https://static1.squarespace.com/static/62be1a89fa808b415fffc8a6/t/6342bb82b1e88a6180a567d5/1665317769691/ezgif.com-gif-maker.gif">

    </div>
    """
st.markdown(html_temp,unsafe_allow_html=True)


st.dataframe(df_en)


customcss = """
  <style>
     
  </style> 
  """
st.markdown(customcss, unsafe_allow_html=True)



# EN

def UAA(i):
    grouped_df_by_crop = df_en[df_en.Crop.str.contains(i)]
    Somme = np.sum(grouped_df_by_crop.Field_area)
    return Somme

def UAA_V():
    V=[]
    for i in df_en.Crop.value_counts().index:
        V.append(UAA(i))
    return V


UAA_by_Crop = pd.DataFrame({"Crop":df_en.Crop.value_counts().index,"UAA":UAA_V(),
                                    "% UAA": np.round((UAA_V()/np.sum(UAA_V()))*100,2) })
    
UAA_by_Crop['% UAA'] = UAA_by_Crop['% UAA'].astype(str) + '%'




st.header('Population')


select_box_1 = st.selectbox('', ["Production mode","Irrigation mode","Crop","Irrigation ","Greenhouse",
                                       "Field area","UAA by crop"])
    
    
# EN



if select_box_1 == "Crop":
    chart = alt.Chart(df_en).mark_bar().encode(
    alt.X("count()", bin=False),
    y='Crop',color='Crop').properties(width=700, height=500)
    st.altair_chart(chart)
    
elif select_box_1 == "Production mode":
    chart = alt.Chart(df_en).mark_bar().encode(
    alt.X("count()", bin=False),
    y='Production_Mode',color='Production_Mode').properties(width=700, height=200)
    st.altair_chart(chart)

elif select_box_1 == "Irrigation mode":
    chart = alt.Chart(df_en).mark_bar().encode(
    alt.X("count()", bin=False),
    y='Irrigation_mode',color='Irrigation_mode').properties(width=700, height=250)
    st.altair_chart(chart)

elif select_box_1 == "Irrigation ":
    chart = alt.Chart(df_en).mark_bar().encode(
    alt.X("count()", bin=False),
    y='Irrigation',color='Irrigation').properties(width=700, height=150)
    st.altair_chart(chart)

elif select_box_1 == "Greenhouse":
    chart = alt.Chart(df_en).mark_bar().encode(
    alt.X("count()", bin=False),
    y='Greenhouse',color='Greenhouse').properties(width=700, height=200)
    st.altair_chart(chart)

elif select_box_1 == "Field area":
    chart = alt.Chart(df_en).transform_density(
    'Field_area',
    as_=['Field_area', 'density'],).mark_area().encode(
    x="Field_area:Q",
    y='density:Q',).properties(width=650, height=300)
    st.altair_chart(chart)

elif select_box_1 == "UAA by crop":
    chart = alt.Chart(UAA_by_Crop).mark_bar().encode(
    alt.X("UAA", bin=False),
    y='Crop',color='Crop')

    text = chart.mark_text(
    align='left',
    baseline='middle',
    dx=3 ).encode(
    text="% UAA")
    st.altair_chart((chart + text).properties(width=700, height=500))
    
    
# --------------



st.header('Sampling & Inference')
    
    
select_box_2 = st.selectbox('', ["Simple Random Sampling","Systematic Sampling",
                                           "Replicated Sampling","Probability Proportional to Size Sampling",
                                           "Stratified Sampling"])
    
select_box_3 = st.selectbox('', ["Irrigation mode","Production mode","Crop","Irrigation  ",
                                     "Greenhouse", "Field area", "UAA by crop"]) 




##################### Echantillonnage aléatoire simple - Simple Random Sampling ##################################

# import random
# seq=list(range(1,606,1))
# V1=sorted(random.sample(seq, 200))
# print("Random sample, n = 200:", V1)


V1 = [5, 6, 9, 10, 11, 12, 15, 16, 19, 20, 21, 23, 24, 27, 38, 40, 42, 46, 53, 56, 58, 59, 63, 64, 71, 72, 
      73, 81, 85, 89, 90, 92, 94, 95, 96, 98, 101, 102, 106, 110, 111, 112, 113, 115, 128, 129, 130, 131,
      132, 133, 142, 145, 148, 149, 151, 155, 161, 165, 166, 167, 168, 170, 172, 173, 175, 179, 182, 184, 185, 
      186, 192, 194, 195, 196, 199, 200, 201, 207, 208, 209, 211, 212, 215, 219, 220, 228, 230, 232, 233, 236, 
      243, 254, 256, 259, 261, 270, 275, 277, 279, 280, 281, 283, 285, 291, 293, 306, 307, 311, 318, 319, 321, 
      327, 332, 333, 336, 337, 340, 346, 347, 359, 362, 371, 377, 378, 383, 384, 386, 387, 388, 390, 392, 396, 
      398, 399, 400, 404, 405, 407, 408, 416, 417, 420, 423, 432, 434, 437, 439, 440, 442, 443, 450, 453, 458, 
      464, 465, 468, 472, 477, 478, 479, 484, 487, 488, 493, 494, 497, 502, 506, 507, 511, 517, 529, 530, 536, 
      540, 542, 544, 546, 547, 548, 549, 554, 555, 561, 564, 569, 571, 573, 574, 577, 578, 581, 583, 586, 593,
      599, 600, 601, 603, 605]


df_SRS=df_en.iloc[V1]



def UAA_SRS(i):
    grouped_df_by_crop = df_SRS[df_SRS.Crop.str.contains(i)]
    Somme = np.sum(grouped_df_by_crop.Field_area)
    return Somme

def UAA_V_SRS():
    V=[]
    for i in df_SRS.Crop.value_counts().index:
        V.append(UAA_SRS(i))
    return V



UAA_by_Crop_SRS = pd.DataFrame({"Crop":df_SRS.Crop.value_counts().index,"UAA":UAA_V_SRS(),
                                    "% UAA": np.round((UAA_V_SRS()/np.sum(UAA_V_SRS()))*100,2) })
    
UAA_by_Crop_SRS['% UAA'] = UAA_by_Crop_SRS['% UAA'].astype(str) + '%'


# EN


if select_box_2 == "Simple Random Sampling":
    
    if select_box_3 == "Crop":
        chart = alt.Chart(df_SRS).mark_bar().encode(
        alt.X("count()", bin=False),
        y='Crop',color='Crop').properties(width=700, height=500)
        st.altair_chart(chart)
    
    elif select_box_3 == "Production mode":
        chart = alt.Chart(df_SRS).mark_bar().encode(
        alt.X("count()", bin=False),
        y='Production_Mode',color='Production_Mode').properties(width=700, height=200)
        st.altair_chart(chart)

    elif select_box_3 == "Irrigation mode":
        chart = alt.Chart(df_SRS).mark_bar().encode(
        alt.X("count()", bin=False),
        y='Irrigation_mode',color='Irrigation_mode').properties(width=700, height=250)
        st.altair_chart(chart)
    
    elif select_box_3 == "Irrigation  ":
        chart = alt.Chart(df_SRS).mark_bar().encode(
        alt.X("count()", bin=False),
        y='Irrigation',color='Irrigation').properties(width=700, height=150)
        st.altair_chart(chart)
    
    elif select_box_3 == "Greenhouse":
        chart = alt.Chart(df_SRS).mark_bar().encode(
        alt.X("count()", bin=False),
        y='Greenhouse',color='Greenhouse').properties(width=700, height=200)
        st.altair_chart(chart)
    
    elif select_box_3 == "Field area":
        chart = alt.Chart(df_SRS).transform_density(
        'Field_area',
        as_=['Field_area', 'density'],).mark_area().encode(
        x="Field_area:Q",
        y='density:Q',).properties(width=650, height=300)
        st.altair_chart(chart)
    
    elif select_box_3 == "UAA by crop":
        chart = alt.Chart(UAA_by_Crop_SRS).mark_bar().encode(
        alt.X("UAA", bin=False),
        y='Crop',color='Crop')
    
        text = chart.mark_text(
        align='left',
        baseline='middle',
        dx=3 ).encode(
        text="% UAA")
        st.altair_chart((chart + text).properties(width=700, height=500))
        
        
##################### Echantillonnage systématique - Systematic sampling ##################################

def systematic_sampling(df, step):
    
    indexes = np.arange(0,len(df),step=step)
    systematic_sample = df.iloc[indexes]
    return systematic_sample


    
df_SS=systematic_sampling(df_en, 3)
df_SS=df_SS.iloc[1:]
df_SS=df_SS.iloc[:200]



def UAA_SS(i):
    grouped_df_by_crop = df_SS[df_SS.Crop.str.contains(i)]
    Somme = np.sum(grouped_df_by_crop.Field_area)
    return Somme

def UAA_V_SS():
    V=[]
    for i in df_SS.Crop.value_counts().index:
        V.append(UAA_SS(i))
    return V


UAA_by_Crop_SS = pd.DataFrame({"Crop":df_SS.Crop.value_counts().index,"UAA":UAA_V_SS(),
                                    "% UAA": np.round((UAA_V_SS()/np.sum(UAA_V_SS()))*100,2) })
    
UAA_by_Crop_SS['% UAA'] = UAA_by_Crop_SS['% UAA'].astype(str) + '%'



# EN

if select_box_2 == "Systematic Sampling":
    
    if select_box_3 == "Crop":
        chart = alt.Chart(df_SS).mark_bar().encode(
        alt.X("count()", bin=False),
        y='Crop',color='Crop').properties(width=700, height=500)
        st.altair_chart(chart)
    
    elif select_box_3 == "Production mode":
        chart = alt.Chart(df_SS).mark_bar().encode(
        alt.X("count()", bin=False),
        y='Production_Mode',color='Production_Mode').properties(width=700, height=200)
        st.altair_chart(chart)

    elif select_box_3 == "Irrigation mode":
        chart = alt.Chart(df_SS).mark_bar().encode(
        alt.X("count()", bin=False),
        y='Irrigation_mode',color='Irrigation_mode').properties(width=700, height=250)
        st.altair_chart(chart)
    
    elif select_box_3 == "Irrigation  ":
        chart = alt.Chart(df_SS).mark_bar().encode(
        alt.X("count()", bin=False),
        y='Irrigation',color='Irrigation').properties(width=700, height=150)
        st.altair_chart(chart)
    
    elif select_box_3 == "Greenhouse":
        chart = alt.Chart(df_SS).mark_bar().encode(
        alt.X("count()", bin=False),
        y='Greenhouse',color='Greenhouse').properties(width=700, height=200)
        st.altair_chart(chart)
    
    elif select_box_3 == "Field area":
        chart = alt.Chart(df_SS).transform_density(
        'Field_area',
        as_=['Field_area', 'density'],).mark_area().encode(
        x="Field_area:Q",
        y='density:Q',).properties(width=650, height=300)
        st.altair_chart(chart)
    
    elif select_box_3 == "UAA by crop":
        chart = alt.Chart(UAA_by_Crop_SS).mark_bar().encode(
        alt.X("UAA", bin=False),
        y='Crop',color='Crop')
    
        text = chart.mark_text(
        align='left',
        baseline='middle',
        dx=3 ).encode(
        text="% UAA")
        st.altair_chart((chart + text).properties(width=700, height=500))


##################### Echantillonnage double - Replicated Sampling ##################################

######### EAS


# seq=list(range(1,606,1))
# C=sorted(random.sample(seq, 100))
# print("Random sample, n = 100:", C)


C = [7, 11, 14, 16, 22, 28, 44, 45, 46, 56, 73, 74, 77, 90, 91, 101, 104, 113, 117, 122, 124, 138, 142, 143, 
     144, 148, 155, 159, 161, 168, 174, 190, 192, 203, 207, 208, 214, 215, 216, 219, 221, 239, 245, 264, 269, 
     273, 274, 278, 280, 281, 283, 290, 295, 300, 302, 303, 312, 313, 314, 321, 322, 324, 332, 343, 348, 356, 
     357, 358, 362, 384, 389, 399, 400, 411, 412, 413, 420, 434, 443, 460, 463, 467, 471, 483, 493, 498, 519, 
     526, 531, 532, 534, 547, 556, 565, 583, 590, 593, 597, 600, 601]


df_RS_SRS=df_en.iloc[C]


######### ES

def systematic_sampling(df, step):
    
    indexes = np.arange(0,len(df),step=step)
    systematic_sample = df.iloc[indexes]
    return systematic_sample
    

df_RS_SS=systematic_sampling(df_en, 6)
df_RS_SS=df_RS_SS.iloc[1:]

######### ED

df_RS = pd.concat([df_RS_SRS, df_RS_SS])



def UAA_RS(i):
    grouped_df_by_crop = df_RS[df_RS.Crop.str.contains(i)]
    Somme = np.sum(grouped_df_by_crop.Field_area)
    return Somme

def UAA_V_RS():
    V=[]
    for i in df_RS.Crop.value_counts().index:
        V.append(UAA_RS(i))
    return V



UAA_by_Crop_RS = pd.DataFrame({"Crop":df_RS.Crop.value_counts().index,"UAA":UAA_V_RS(),
                                    "% UAA": np.round((UAA_V_RS()/np.sum(UAA_V_RS()))*100,2) })
    
UAA_by_Crop_RS['% UAA'] = UAA_by_Crop_RS['% UAA'].astype(str) + '%'
        
        
        
# EN

if select_box_2 == "Replicated Sampling":
    
    if select_box_3 == "Crop":
        chart = alt.Chart(df_RS).mark_bar().encode(
        alt.X("count()", bin=False),
        y='Crop',color='Crop').properties(width=700, height=500)
        st.altair_chart(chart)
    
    elif select_box_3 == "Production mode":
        chart = alt.Chart(df_RS).mark_bar().encode(
        alt.X("count()", bin=False),
        y='Production_Mode',color='Production_Mode').properties(width=700, height=200)
        st.altair_chart(chart)

    elif select_box_3 == "Irrigation mode":
        chart = alt.Chart(df_RS).mark_bar().encode(
        alt.X("count()", bin=False),
        y='Irrigation_mode',color='Irrigation_mode').properties(width=700, height=250)
        st.altair_chart(chart)
    
    elif select_box_3 == "Irrigation  ":
        chart = alt.Chart(df_RS).mark_bar().encode(
        alt.X("count()", bin=False),
        y='Irrigation',color='Irrigation').properties(width=700, height=150)
        st.altair_chart(chart)
    
    elif select_box_3 == "Greenhouse":
        chart = alt.Chart(df_RS).mark_bar().encode(
        alt.X("count()", bin=False),
        y='Greenhouse',color='Greenhouse').properties(width=700, height=200)
        st.altair_chart(chart)
    
    elif select_box_3 == "Field area":
        chart = alt.Chart(df_RS).transform_density(
        'Field_area',
        as_=['Field_area', 'density'],).mark_area().encode(
        x="Field_area:Q",
        y='density:Q',).properties(width=650, height=300)
        st.altair_chart(chart)
    
    elif select_box_3 == "UAA by crop":
        chart = alt.Chart(UAA_by_Crop_RS).mark_bar().encode(
        alt.X("UAA", bin=False),
        y='Crop',color='Crop')
    
        text = chart.mark_text(
        align='left',
        baseline='middle',
        dx=3 ).encode(
        text="% UAA")
        st.altair_chart((chart + text).properties(width=700, height=500))

        
############################## Echantillonnage à probabilités inégales ##################################
   

#EN
df2=df_en
total = df2['Field_area'].sum()
sample_size = 200 #number of samples to be selected
interval_width = int(total/sample_size)
df2['Field_area_accumulated'] = df2['Field_area'].cumsum()
num = interval_width #can be a random number also as in the example
sampled_series = np.arange(num, total, interval_width)
cum_array = np.asarray(df2['Field_area_accumulated'])
selected_samples = np.zeros(sample_size, dtype='int32')
idx = np.searchsorted(cum_array,sampled_series) #the heart of code
result = cum_array[idx-1] 
df_PPS_en = df2[df2['Field_area_accumulated'].isin(result)]


def UAA_PPS(i):
    grouped_df_by_crop = df_PPS_en[df_PPS_en.Crop.str.contains(i)]
    Somme = np.sum(grouped_df_by_crop.Field_area)
    return Somme

def UAA_V_PPS():
    V=[]
    for i in df_PPS_en.Crop.value_counts().index:
        V.append(UAA_PPS(i))
    return V


UAA_by_Crop_PPS = pd.DataFrame({"Crop":df_PPS_en.Crop.value_counts().index,"UAA":UAA_V_PPS(),
                                    "% UAA": np.round((UAA_V_PPS()/np.sum(UAA_V_PPS()))*100,2) })
    
UAA_by_Crop_PPS['% UAA'] = UAA_by_Crop_PPS['% UAA'].astype(str) + '%'
    
        

if select_box_2 == "Probability Proportional to Size Sampling":
    
    if select_box_3 == "Crop":
        chart = alt.Chart(df_PPS_en).mark_bar().encode(
        alt.X("count()", bin=False),
        y='Crop',color='Crop').properties(width=700, height=500)
        st.altair_chart(chart)
    
    elif select_box_3 == "Production mode":
        chart = alt.Chart(df_PPS_en).mark_bar().encode(
        alt.X("count()", bin=False),
        y='Production_Mode',color='Production_Mode').properties(width=700, height=200)
        st.altair_chart(chart)

    elif select_box_3 == "Irrigation mode":
        chart = alt.Chart(df_PPS_en).mark_bar().encode(
        alt.X("count()", bin=False),
        y='Irrigation_mode',color='Irrigation_mode').properties(width=700, height=250)
        st.altair_chart(chart)
    
    elif select_box_3 == "Irrigation  ":
        chart = alt.Chart(df_PPS_en).mark_bar().encode(
        alt.X("count()", bin=False),
        y='Irrigation',color='Irrigation').properties(width=700, height=150)
        st.altair_chart(chart)
    
    elif select_box_3 == "Greenhouse":
        chart = alt.Chart(df_PPS_en).mark_bar().encode(
        alt.X("count()", bin=False),
        y='Greenhouse',color='Greenhouse').properties(width=700, height=200)
        st.altair_chart(chart)
    
    elif select_box_3 == "Field area":
        chart = alt.Chart(df_PPS_en).transform_density(
        'Field_area',
        as_=['Field_area', 'density'],).mark_area().encode(
        x="Field_area:Q",
        y='density:Q',).properties(width=650, height=300)
        st.altair_chart(chart)
    
    elif select_box_3 == "UAA by crop":
        chart = alt.Chart(UAA_by_Crop_PPS).mark_bar().encode(
        alt.X("UAA", bin=False),
        y='Crop',color='Crop')
    
        text = chart.mark_text(
        align='left',
        baseline='middle',
        dx=3 ).encode(
        text="% UAA")
        st.altair_chart((chart + text).properties(width=700, height=500))

############################## Stratified Sampling ##################################

median = np.median(df_en.Field_area)

df_Stra1=df_en.loc[df_en['Field_area'] < median]
df_Stra2=df_en.loc[df_en['Field_area'] >= median]

n=200


C1=np.std(df_Stra1["Field_area"])/np.mean(df_Stra1["Field_area"])
C2=np.std(df_Stra2["Field_area"])/np.mean(df_Stra2["Field_area"])
Xq1=(np.median(df_Stra1["Field_area"]))**0.5
Xq2=(np.median(df_Stra2["Field_area"]))**0.5
    
Nh1=n*((C1*Xq1)/(C1*Xq1+C2*Xq2))
Nh2=n*((C2*Xq2)/(C1*Xq1+C2*Xq2))

# import random

# seq=list(range(0,302,1))

# import random 

# V1=sorted(random.sample(seq, int(Nh1)))


V1 = [1, 3, 6, 13, 14, 30, 57, 59, 73, 85, 87, 104, 109, 111, 114, 117, 123, 124, 136, 147, 155, 160, 166, 178, 188, 
      194, 201, 204, 206, 226, 229, 260, 262, 272, 278, 293]

# V2=sorted(random.sample(seq, int(Nh2)))

V2 = [2, 9, 10, 11, 14, 16, 18, 19, 20, 21, 27, 29, 30, 33, 34, 35, 37, 38, 40, 41, 42, 43, 47, 48, 49, 52, 53, 54, 55,
      56, 57, 58, 63, 64, 67, 68, 70, 71, 75, 77, 84, 85, 86, 88, 89, 90, 91, 92, 94, 96, 97, 101, 102, 103, 105, 106, 
      111, 113, 116, 118, 119, 120, 122, 128, 129, 132, 134, 136, 140, 141, 143, 144, 147, 153, 154, 159, 160, 165, 166,
      167, 169, 170, 172, 173, 174, 175, 177, 178, 179, 181, 182, 183, 184, 185, 188, 189, 190, 191, 192, 193, 194, 195,
      196, 197, 198, 199, 200, 202, 203, 204, 205, 211, 213, 214, 215, 218, 219, 220, 221, 222, 224, 227, 228, 231, 233,
      234, 235, 236, 239, 240, 244, 245, 247, 251, 252, 254, 255, 256, 257, 258, 262, 264, 265, 266, 267, 269, 271, 273, 
      275, 276, 279, 280, 282, 284, 287, 288, 291, 293, 295, 296, 299, 300, 301]

# Dataframe de la premiere strata (18% de n)

# EN
df_Strat001=df_en.loc[df_en['Field_area'] < median]
df_Strat001=df_Strat001.iloc[V1]


# Dataframe de la deuxieme strata (82% de n)

# EN
df_Strat002=df_en.loc[df_en['Field_area'] >= median]
df_Strat002=df_Strat002.iloc[V2]


# Final df
df_Strat=pd.concat([df_Strat001,df_Strat002])


def UAA_Strat(i):
    grouped_df_by_crop = df_Strat[df_Strat.Crop.str.contains(i)]
    Somme = np.sum(grouped_df_by_crop.Field_area)
    return Somme

def UAA_V_Strat():
    V=[]
    for i in df_Strat.Crop.value_counts().index:
        V.append(UAA_Strat(i))
    return V



UAA_by_Crop_Strat = pd.DataFrame({"Crop":df_Strat.Crop.value_counts().index,"UAA":UAA_V_Strat(),
                                    "% UAA": np.round((UAA_V_Strat()/np.sum(UAA_V_Strat()))*100,2) })
    
UAA_by_Crop_Strat['% UAA'] = UAA_by_Crop_Strat['% UAA'].astype(str) + '%'
    


# EN

if select_box_2 == "Stratified Sampling":
    
    if select_box_3 == "Crop":
        chart = alt.Chart(df_Strat).mark_bar().encode(
        alt.X("count()", bin=False),
        y='Crop',color='Crop').properties(width=700, height=500)
        st.altair_chart(chart)
    
    elif select_box_3 == "Production mode":
        chart = alt.Chart(df_Strat).mark_bar().encode(
        alt.X("count()", bin=False),
        y='Production_Mode',color='Production_Mode').properties(width=700, height=200)
        st.altair_chart(chart)

    elif select_box_3 == "Irrigation mode":
        chart = alt.Chart(df_Strat).mark_bar().encode(
        alt.X("count()", bin=False),
        y='Irrigation_mode',color='Irrigation_mode').properties(width=700, height=250)
        st.altair_chart(chart)
    
    elif select_box_3 == "Irrigation  ":
        chart = alt.Chart(df_Strat).mark_bar().encode(
        alt.X("count()", bin=False),
        y='Irrigation',color='Irrigation').properties(width=700, height=150)
        st.altair_chart(chart)
    
    elif select_box_3 == "Greenhouse":
        chart = alt.Chart(df_Strat).mark_bar().encode(
        alt.X("count()", bin=False),
        y='Greenhouse',color='Greenhouse').properties(width=700, height=200)
        st.altair_chart(chart)
    
    elif select_box_3 == "Field area":
        chart = alt.Chart(df_Strat).transform_density(
        'Field_area',
        as_=['Field_area', 'density'],).mark_area().encode(
        x="Field_area:Q",
        y='density:Q',).properties(width=650, height=300)
        st.altair_chart(chart)
    
    elif select_box_3 == "UAA by crop":
        chart = alt.Chart(UAA_by_Crop_Strat).mark_bar().encode(
        alt.X("UAA", bin=False),
        y='Crop',color='Crop')
    
        text = chart.mark_text(
        align='left',
        baseline='middle',
        dx=3 ).encode(
        text="% UAA")
        st.altair_chart((chart + text).properties(width=700, height=500))



select_box_4 = st.selectbox('', ["Mean Comparison","Standard Deviation Comparison"])

#### Mean Comparision


l=np.array([np.mean(df_en['Field_area']),np.mean(df_SRS['Field_area']),np.mean(df_SS['Field_area']),
    np.mean(df_RS['Field_area']),np.mean(df_PPS_en['Field_area']),np.mean(df_Strat['Field_area'])])

l0=l/np.mean(df_en['Field_area'])
l1=l/np.mean(df_SRS['Field_area'])
l2=l/np.mean(df_SS['Field_area'])
l3=l/np.mean(df_RS['Field_area'])
l4=l/np.mean(df_PPS_en['Field_area'])
l5=l/np.mean(df_Strat['Field_area'])

index=['POP','SRS','SS','RS','PPS','Strat']

Compare_mean=pd.DataFrame({'POP':l0,'SRS':l1,'SS':l2,'RS':l3,'PPS':l4,'Strat':l5},index=index )

#### Comparaison des écarts-types


k=np.array([np.std(df_en['Field_area']),np.std(df_SRS['Field_area']),np.std(df_SS['Field_area']),
    np.std(df_RS['Field_area']),np.std(df_PPS_en['Field_area']),np.std(df_Strat['Field_area'])])

k0=k/np.std(df_en['Field_area'])
k1=k/np.std(df_SRS['Field_area'])
k2=k/np.std(df_SS['Field_area'])
k3=k/np.std(df_RS['Field_area'])
k4=k/np.std(df_PPS_en['Field_area'])
k5=k/np.std(df_Strat['Field_area'])

index=['POP','SRS','SS','RS','PPS','Strat']

Compare_sd=pd.DataFrame({'POP':k0,'SRS':k1,'SS':k2,'RS':k3,'PPS':k4,'Strat':k5},index=index )

if select_box_4 == "Mean Comparison":
    st.dataframe(Compare_mean)

if select_box_4 == "Standard Deviation Comparison":
    st.dataframe(Compare_sd)


#####################################################################################################################


st.write(r"""
**Systematic sampling** is the most appropriate sampling frame design for this population:

""")

st.write(r""" 
$Interval$ $(step) =  \frac{N}{n}$ 

""")
