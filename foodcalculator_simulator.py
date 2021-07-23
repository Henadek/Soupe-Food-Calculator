from food_calculator import *
from PIL import Image
import streamlit as st
import pandas as pd

#######################################################################
################      GUI BEGINS HERE        ##########################
#######################################################################

image1 = Image.open('foodcalc_image.jpg')

st.markdown("<h1 style='text-align: center'> SOUPE FOOD CALCULATOR </h1>", unsafe_allow_html=True)
st.image(image1, caption='Source (Picture: Omincalculator/Getty)')
# BUILD FIELDS FOR HH SIZE
budget_plan = ['Daily', 'Weekly', 'Monthly']
selected_hh = st.sidebar.number_input('Select No. of People to Plan for', min_value=0, max_value=1000)
budget_type = st.sidebar.selectbox('Select Budget Type', budget_plan)


# Set HH Segmentation Container
st.beta_container()
hh_expander = st.beta_expander(label='People Segmentation')
with hh_expander:
    cols = st.beta_columns(2)
    # set headers for male and female
    cols[0].subheader('Male Segmentation')
    cols[1].subheader('Female Segmentation')
    
    # get total number of male & female people
    t_mchild = cols[0].number_input('Total Male Child (2-5 years)', min_value=0, max_value=100)
    t_madolescent = cols[0].number_input('Total Male Adolescent (6-19 years)', min_value=0, max_value=100)
    t_mmiddleage = cols[0].number_input('Total Male Middle-age (20-29 years)', min_value=0, max_value=100)
    t_madult = cols[0].number_input('Total Male Adult (30-50 years)', min_value=0, max_value=100)
    t_maged = cols[0].number_input('Total Male Aged (51+ years)', min_value=0, max_value=100)
    t_fchild = cols[1].number_input('Total Female Child (2-5 years)', min_value=0, max_value=100)
    t_fadolescent = cols[1].number_input('Total Female Adolescent (6-19 years)', min_value=0, max_value=100)
    t_fmiddleage = cols[1].number_input('Total Female Middle-age (20-29 years)', min_value=0, max_value=100)
    t_fadult = cols[1].number_input('Total Female Adult (30-50 years)', min_value=0, max_value=100)
    t_faged = cols[1].number_input('Total Female Aged (51+ years)', min_value=0, max_value=100)

# set global available foodlist
foodlist = ['','Jollof Rice','White Rice','Egusi Soup',
                'Spaghetti','Porridge','Eba',
                'Pap','Stew','Vegetable Soup'
                ]

def show_dailyfields():
    # shows the fields for daily budget.
    # Set FoodList Container
    foodlist = ['','Jollof Rice','White Rice','Egusi Soup',
                'Spaghetti','Porridge','Eba',
                'Pap','Stew','Vegetable Soup'
                ]

    foodlistcontainer = st.sidebar.beta_container()
    foodlist_expander = st.beta_expander(label='Foodlist Selector')
    with foodlist_expander:
        foodcols = st.beta_columns(2)
        # set headers for male and female
        foodcols[0].subheader('Select Your Food')
        foodcols[1].subheader('Daily Food Frequency')
        # generate selectfields
        Food1 = foodcols[0].selectbox('Food1', foodlist)
        Food2 = foodcols[0].selectbox('Food2', foodlist)
        Food3 = foodcols[0].selectbox('Food3', foodlist)
        Food4 = foodcols[0].selectbox('Food4', foodlist)
        Food5 = foodcols[0].selectbox('Food5', foodlist)
        Food6 = foodcols[0].selectbox('Food6', foodlist)
        Food7 = foodcols[0].selectbox('Food7', foodlist)
        Food8 = foodcols[0].selectbox('Food8', foodlist)
        Food9 = foodcols[0].selectbox('Food9', foodlist)

        Freq1 = foodcols[1].selectbox('Frequency1', range(0,4))
        Freq2 = foodcols[1].selectbox('Frequency2', range(0,4))
        Freq3 = foodcols[1].selectbox('Frequency3', range(0,4))
        Freq4 = foodcols[1].selectbox('Frequency4', range(0,4))
        Freq5 = foodcols[1].selectbox('Frequency5', range(0,4))
        Freq6 = foodcols[1].selectbox('Frequency6', range(0,4))
        Freq7 = foodcols[1].selectbox('Frequency7', range(0,4))
        Freq8 = foodcols[1].selectbox('Frequency8', range(0,4))
        Freq9 = foodcols[1].selectbox('Frequency9', range(0,4))

    food_freq_mapping = {'Freq1': Food1,'Freq2': Food2,'Freq3': Food3,
                        'Freq4': Food4,'Freq5': Food5,'Freq6': Food6,
                        'Freq7': Food7,'Freq8': Food8,'Freq9': Food9
                        }
    return [food_freq_mapping, [Freq1,Freq2,Freq3,Freq4,Freq5,Freq6,Freq7,Freq8,Freq9]]

# Set Calculate Button
calculateButton = st.sidebar.button('Calculate')


def show_weeklyfields():
    # shows the fields for weekly budget and deactivates the daily fields.
    foodlist = ['','Jollof Rice','White Rice','Egusi Soup',
            'Spaghetti','Porridge','Eba',
            'Pap','Stew','Vegetable Soup'
            ]
    if budget_type == 'Monthly':
        st.info("Monthly food calculation is based on weekly food budget pattern")
    weekly_foodlist_expander = st.beta_expander(label='Weekly Foodlist Selector')
    with weekly_foodlist_expander:
        weekly_foodcols = st.beta_columns(1)
        # set header for weekly food
        weekly_foodcols[0].subheader('Select Your Food')
        # generate food multi-selectfields for all days in week
        weekly_selected_foods = {}
        for days in ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']:
            nday = weekly_foodcols[0].multiselect(days, foodlist)
            if '' in nday:
                nday.pop(nday.index(''))
            weekly_selected_foods[days]=nday
    weekly_food_structure = []
    ct=0
    for nday in weekly_selected_foods:
        temp_dict = {}
        if len(weekly_selected_foods[nday])>0:
            # st.write(weekly_selected_foods)
            nday_expander = st.beta_expander(label=f'{nday} Foods')
            nday_expander.subheader(f'Food Frequency for {nday}')
            for food in weekly_selected_foods[nday]:
                try:
                    meal_recurrence = nday_expander.selectbox(f'{food} Recurrence', range(0,4))
                except:
                    ct+=1
                    meal_recurrence = nday_expander.selectbox(f'{food}{ct} Recurrence', range(0,4))
                temp_dict[food]=meal_recurrence

        weekly_food_structure.append({nday.lower():temp_dict})
    return weekly_food_structure

def check_food_structure(weekly_food_structure):
    # check if all fields are filled
    check_structure = []
    for i in weekly_food_structure:
        for j in i:
            if 0 in i[j].values():
                check_structure.append(False)
            else: check_structure.append(True)
    if False in check_structure:
        st.exception(RuntimeError('Please select foods and recurrence for each day!'))
    else:
        # st.write(weekly_food_structure)
        return True


if budget_type =='Daily':
    daily_food_structure = show_dailyfields()


if budget_type =='Weekly' or budget_type =='Monthly':
    weekly_food_structure = show_weeklyfields()


def daily_algorithm(foodmapping, freq_list):
    track = 0
    foods = {}
    for get_freq in freq_list:
        track+=1
        if get_freq>0 and foodmapping['Freq'+str(track)]!='':
            curr_food = foodmapping['Freq'+str(track)]
            # print(curr_food)
            foods[curr_food] = get_freq

    # print(foods)
    # foods = {'Spaghetti':1, 'Eba': 1, 'Pap':1, 'Vegetable Soup':2}

    # pass in the hh_segmentation to the calculator engine
    calculator.engine(hh_segmentation, **foods)
    st.write(f"Total Ingredients Qty for {', '.join(list(foods.keys()))} for {selected_hh} {['person' if selected_hh==1 else 'people'][0]}")
    foodrez = calculator.result()

    ct = 0
    for k in foods.keys():
        st.write(k)
        ab = pd.DataFrame(foodrez[ct].items(), columns=['Ingredients', 'Qty'])
        st.dataframe(ab)
        ct+=1

def generate_resultcard(budgetresult):
    # aa = [{'monday':{'Spaghetti':2, 'Eba': 2, 'Pap':2, 'Vegetable Soup':2}},
    #         {'tuesday':{'Jollof Rice':2, 'Porridge':2}},
    #         {'wednesday':{'White Rice':2, 'Stew': 2, 'Egusi Soup':2}},
    #         {'thursday':{'Spaghetti':2, 'Eba': 2, 'Pap':2, 'Vegetable Soup':2}},
    #         {'friday':{'Spaghetti':1, 'Eba': 1, 'Pap':1, 'Vegetable Soup':1}},
    #         {'saturday':{'Spaghetti':1, 'Eba': 1, 'Pap':1, 'Vegetable Soup':1}},
    #         {'sunday':{'Spaghetti':2, 'Eba': 2, 'Pap':2, 'Vegetable Soup':2}},
    #         ]

    st.write(f"Total Ingredients Qty for {selected_hh} {['person' if selected_hh==1 else 'people'][0]} Per {budget_type[:-2]}")
    # st.write(budgetresult)

    # ct = 0
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    for day in days:
        final_foodlist = {}
        st.markdown(f'## {day}')
        day= day.lower()
        for foods in budgetresult['daily'][day]:
            # st.write(foods)
            for meal in foods.keys():
                if '_' in meal:
                    meal = meal.replace('_', ' ')

                if 'Garri' in list(foods.keys()) :
                    meal = 'Eba'
                if 'Rice' in list(foods.keys()) and 'Tomato_Paste' in list(foods.keys()) and 'Tomato/Pepper' in list(foods.keys()):
                    meal = 'Jollof Rice'
                if 'Rice' in list(foods.keys()) and 'Tomato_Paste' not in list(foods.keys()) and 'Tomato/Pepper' in list(foods.keys()):
                    meal = 'White Rice'
                if 'Rice' not in list(foods.keys()) and 'Tomato_Paste' in list(foods.keys()) and 'Tomato/Pepper' in list(foods.keys()):
                    meal = 'Stew'
                if 'Egusi' in list(foods.keys()) :
                    meal = 'Egusi Soup'
                if 'Vegetable' in list(foods.keys()) and 'Yam' not in list(foods.keys()) and 'Egusi' not in list(foods.keys()):
                    meal = 'Vegetable Soup'
                if 'Yam' in list(foods.keys()) and 'Vegetable' in list(foods.keys()):
                    meal = 'Porridge'

                if meal in foodlist:
                    meal1 = foodlist[foodlist.index(meal)]
                    if meal1 in foodlist:
                        if meal1 not in final_foodlist:
                            # st.write(meal1)
                            final_foodlist[meal1]=foods

        # st.write(final_foodlist)
        dayfoodcontainer = st.beta_container()
        with dayfoodcontainer:
            foodarray = list(final_foodlist.keys())
            foodcols = st.beta_columns(2)
            # handles food list if only equal to or greater than 2
            ct = 1
            for i in range(len(foodarray)):
                pair = foodarray[i:i+2]
                if ct==1:
                    # st.write(pair)
                    foodcols[0].subheader(pair[0])
                    try:
                        foodcols[1].subheader(pair[1])
                    except:pass
                    # populate dataframes based on no. of columns from data result
                    dataframe1 = pd.DataFrame(final_foodlist[pair[0]].items(), columns=['Ingredients', 'Qty'])
                    foodcols[0].dataframe(dataframe1)
                    # st.write(final_foodlist[pair[0]].values())
                    try:
                        dataframe2 = pd.DataFrame(final_foodlist[pair[1]].items(), columns=['Ingredients', 'Qty'])
                        foodcols[1].dataframe(dataframe2)
                        # st.write(final_foodlist[pair[1]].values())
                    except:pass
                    # foodcols[0].dataframe(dataframe1)
                    # st.write(final_foodlist[pair[0]].values())
                    # try:
                    #     foodcols[1].dataframe(dataframe2)
                    #     st.write(final_foodlist[pair[1]].values())
                    # except:pass
                elif ct%2!=0 and ct!=len(foodarray):
                    # st.write(pair)
                    foodcols[0].subheader(pair[0])
                    try:
                        foodcols[1].subheader(pair[1])
                    except:pass
                    # populate dataframes based on no. of columns from data result
                    dataframe1 = pd.DataFrame(final_foodlist[pair[0]].items(), columns=['Ingredients', 'Qty'])
                    foodcols[0].dataframe(dataframe1)
                    # st.write(final_foodlist[pair[0]].values())
                    try:
                        dataframe2 = pd.DataFrame(final_foodlist[pair[1]].items(), columns=['Ingredients', 'Qty'])
                        foodcols[1].dataframe(dataframe2)
                        # st.write(final_foodlist[pair[1]].values())
                    except:pass
                    # foodcols[0].dataframe(dataframe1)
                    # st.write(final_foodlist[pair[0]].values())
                    # try:
                    #     foodcols[1].dataframe(dataframe2)
                    #     st.write(final_foodlist[pair[1]].values())
                    # except:pass
                elif ct%2!=0 and ct==len(foodarray):
                    foodcols[0].subheader(pair[0])
                    # populate dataframes based on no. of columns from data result
                    dataframe1 = pd.DataFrame(final_foodlist[pair[0]].items(), columns=['Ingredients', 'Qty'])
                    foodcols[0].dataframe(dataframe1)
                    # st.write(final_foodlist[pair[0]].values())
                ct+=1


# calls all functions when the calculate button is pressed
if calculateButton:

    calculator = FoodCalculator(hh_size=selected_hh)
    
    # set hh_segmentation
    hh_segmentation = {'Males': {'total_child': t_mchild, 'total_adolescent': t_madolescent,
                                 'total_middle_age': t_mmiddleage, 'total_adult': t_madult,
                                 'total_aged': t_maged
                                }, 
                       'Females': {'total_fchild': t_fchild, 'total_fadolescent': t_fadolescent,
                                   'total_fmiddle_age': t_fmiddleage, 'total_fadult': t_fadult,
                                   'total_faged': t_faged
                                  }
                      }

    # FOR DAILY BUDGET
    if budget_type =='Daily':
        daily_algorithm(daily_food_structure[0], daily_food_structure[1])

    # FOR WEEKLY BUDGET
    elif budget_type == 'Weekly':
        if check_food_structure(weekly_food_structure) == True:

            # pass in the hh_segmentation to the calculator engine and initialize with dummy food
            dummy_food =  {'food1':0, 'food2':0}
            calculator.engine(hh_segmentation, **dummy_food)

            weeklyresult = calculator.weeklybudget(weekly_food_structure)
            generate_resultcard(weeklyresult)
        else:
            st.exception(RuntimeError('Please select foods and recurrence for each day!'))


    # FOR MONTHLY BUDGET
    elif budget_type == 'Monthly':
        if check_food_structure(weekly_food_structure) == True:
            dummy_food =  {'food1':0, 'food2':0}
            calculator.engine(hh_segmentation, **dummy_food)
            monthlyresult = calculator.monthlybudget(weekly_food_structure)
            # st.write(monthlyresult)
            generate_resultcard(monthlyresult)
        else:
            st.exception(RuntimeError('Please select foods and recurrence for each day!'))