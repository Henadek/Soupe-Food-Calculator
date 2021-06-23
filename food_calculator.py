# # PHASE 1 - DATA FORMATTING AND ENTRY

# #### Income Level, Household Size, Total Male and Female
import malefoodqty as mfq
import femalefoodqty as ffq
import streamlit as st
import pandas as pd
















# ### IMPLEMENT CALCULATOR MODEL

from collections import Counter


class FoodCalculator:
    def __init__(self, income = None, hh_size = None):
        self.income = income
        self.hh_size = hh_size
        self.__data = {}
        self.__result = {}
        
        
    def __str__(self):
        return str(self.__result)
    
    
    def __getIncomeLvl(self, option_no):
        '''
         *** INSTRUCTION FOR USING FUNCTION ***
        INPUT IS ANY VALUE FROM 0 - 3
        Accepts one input - The select one choice input (referenced as option_no)
        Gets the Income Level of the head of household
        Returns a dictionary of income_level
        '''
        try:
            option_no = int(option_no)
            income_range = ['10,000 - 40,000', '41,000 - 100,000',
                            '101,000 - 200,000', '201,000+']

            if option_no in range(len(income_range)):
                get_level = {'income_level': income_range[option_no]}
            return get_level

        except:
            return f'Please select an income range within the available options'
    
    def __getHouseholdsize(self, hh_size):
        try:
            hh_size = int(hh_size)
        except:
            return f'Please enter a valid value for household size'
        return hh_size
    
    
    def __getMale(self, male_segmentation = None):
        '''
         *** INSTRUCTION FOR USING FUNCTION ***
        ACCEPTS 1 INPUT VALUE; A dictionary of household segmentation in the format below:
        
        {'Males': {'total_child': 0, 'total_adolescent': 0,
                   'total_middle_age': 0, 'total_adult': 0, 
                   'total_aged': 0
                   }, 
         'Females': {'total_fchild': 0, 'total_fadolescent': 0, 
                     'total_fmiddle_age': 0, 'total_fadult': 0, 
                     'total_faged': 0
                     }
        }
        
        Returns dictionary with the total value for males   
        '''
        male_segmentation = male_segmentation['Males']
        total_male = 0
        
        # looping through to dictkeys and compute total_male to main dictionary
        for i in male_segmentation.keys():
            total_male += int(male_segmentation[i])


        result = {'total_male': total_male, 'total_child': int(male_segmentation['total_child']),
                  'total_adolescent': int(male_segmentation['total_adolescent']), 'total_middle_age': int(male_segmentation['total_middle_age']),
                  'total_adult': int(male_segmentation['total_adult']),'total_aged': int(male_segmentation['total_aged'])}
        
        return result

        
        
    def __getFemale(self, female_segmentation = None):
        '''
         *** INSTRUCTION FOR USING FUNCTION ***
        ACCEPTS 1 INPUT VALUE; A dictionary of household segmentation in the format below:
        
        {'Males': {'total_child': 0, 'total_adolescent': 0,
                   'total_middle_age': 0, 'total_adult': 0, 
                   'total_aged': 0
                   }, 
         'Females': {'total_fchild': 0, 'total_fadolescent': 0, 
                     'total_fmiddle_age': 0, 'total_fadult': 0, 
                     'total_faged': 0
                     }
        }
        
        Returns dictionary with the total value for females               
        '''
        female_segmentation = female_segmentation['Females']
        total_female = 0
        
        # looping through to dictkeys and compute total_male to main dictionary
        for i in female_segmentation.keys():
            total_female += int(female_segmentation[i])


        result = {'total_female': total_female, 'total_fchild': int(female_segmentation['total_fchild']),
                  'total_fadolescent': int(female_segmentation['total_fadolescent']), 'total_fmiddle_age': int(female_segmentation['total_fmiddle_age']),
                  'total_fadult': int(female_segmentation['total_fadult']),'total_faged': int(female_segmentation['total_faged'])}
        
        return result
    
        

    def __checkHouseholdsize(self, hh_size, m, f):
        '''
        check if male and female are the total sum of the household size
        '''
        assert hh_size == m['total_male'] + f['total_female']
    
    
    def __dailybudget(self, **selected_foods):
        '''
        Checks that number of meals do not exceed 3 times per day.
        '''
        # MAX number of meal per day for breakfast, lunch and dinner == 3.
        max_no = 3
        total_meal = 0

#         for v in selected_foods.values():
#             total_meal+=v
        
#         assert total_meal > 0
#         assert total_meal <= max_no
        return selected_foods
    
    
    def weeklybudget(self, selected_foods):
        '''
        1. select all foods you need for per day
        Format:
        [{'monday':{'Spaghetti':1, 'Eba': 1, 'Pap':1, 'Vegetable Soup':2}},
        {'tuesday':{'Spaghetti':1, 'Eba': 1, 'Pap':1, 'Vegetable Soup':2}},
        {'wednesday':{'Spaghetti':1, 'Eba': 1, 'Pap':1, 'Vegetable Soup':2}},
        {'thurday':{'Spaghetti':1, 'Eba': 1, 'Pap':1, 'Vegetable Soup':2}},
        {'friday':{'Spaghetti':1, 'Eba': 1, 'Pap':1, 'Vegetable Soup':2}},
        {'saturday':{'Spaghetti':1, 'Eba': 1, 'Pap':1, 'Vegetable Soup':2}},
        {'sunday':{'Spaghetti':1, 'Eba': 1, 'Pap':1, 'Vegetable Soup':2}},
        ]
        '''
        daily_result = {}
        for day in selected_foods:
            foods = list(day.values())[0]
            day = list(day.keys())[0]
            self.engine(self.__hhl_segmentation, budget_plan = 0, **foods)
            daily_result[day] = self.result()

        self.__result = {'daily':daily_result, 'Aggregate':None}
        
        return self.__result

    
    
  
    
    
    def __monthlybudget(self):
        pass
    
    
    
    def __cumulate_food(self, foodlist):
        '''
        This is called only for a daily budget
        '''
        nwlist = [] 
        while len(foodlist)>0:
            if len(foodlist)>1 and len(foodlist)%2==0:
                if len(nwlist)>0:
                    for food1,food2 in zip(nwlist,foodlist[0]):
                        counter = Counter()
                        counter += Counter(food1)+Counter(food2)
                        nwlist[nwlist.index(food1)] = counter
                    foodlist = foodlist[1:]
                else:
                    for food1,food2 in zip(foodlist[0],foodlist[1]):
                        counter = Counter()
                        counter += Counter(food1)+Counter(food2)
                        nwlist.append(counter)
                    foodlist = foodlist[2:]

            elif len(foodlist)>1 and len(foodlist)%2!=0:
            #loop it in 2's and finally add last one.
                if len(nwlist)>0:
                    for food1,food2 in zip(nwlist,foodlist[0]):
                        counter = Counter()
                        counter += Counter(food1)+Counter(food2)
                        nwlist[nwlist.index(food1)] = counter
                    foodlist = foodlist[1:]
                else:
                    for food1,food2 in zip(foodlist[0],foodlist[1]):
                        counter = Counter()
                        counter += Counter(food1)+Counter(food2)
                        nwlist.append(counter)
                    foodlist = foodlist[2:]

            elif len(foodlist)==1:
                # checks that it remains only one item in the list
                if len(nwlist)==len(foodlist[0]):
                    for food1,food2 in zip(nwlist,foodlist[0]):
                        counter = Counter()
                        counter += Counter(food1)+Counter(food2)
                        nwlist[nwlist.index(food1)] = counter
                    foodlist.pop()
                else:
                    for k in foodlist[0]:
                        counter = Counter()
                        counter += Counter(k)
                        nwlist.append(counter)
                    foodlist.pop()
        if len(foodlist)==0:
            for i in nwlist:
                nwlist[nwlist.index(i)] = dict(i)
            for i in nwlist:
                for a,b in i.items():
                    i[a] = round(b)
            return nwlist
        else:
            self.__cumulate_food(foodlist)
    
    
    def __ingredientsQtyCompiler(self, hh_segmentedFoods, **selected_foods):
        '''
        Logic that iteratively sorts out selected foods and cumulates the qty value
        Returns a dictionary of ingredients with ingredient as key and total qty as value.
        
        '''
        
        foodlist = []
        for food,freq in selected_foods.items():
            if food in hh_segmentedFoods.keys():
                # set food frequency to value from selected food dictionary
                hh_segmentedFoods[food][1]['freq'] = freq
    #             print(hh_segmentedFoods[food])

                # compute the ingredients qty with the frequency of consumption
                total_ingredients_qty = {}
                ct = 0
                for ingredient in hh_segmentedFoods[food][0]:
                    ct+=1
                    total_ingredients_qty[ingredient] = hh_segmentedFoods[food][0][ingredient]*hh_segmentedFoods[food][1]['freq']
                    if ct == len(hh_segmentedFoods[food][0]):
    #                     print(ct)
                        foodlist.append(total_ingredients_qty)
                        break
        return foodlist
                      

                
        # TODO:
        # USE DICTIONARIES TO MAP EACH INGREDIENTS AND CUMULATE THE VALUE, 
        # THEN SPIT OUT THE TOTAL

        
    def engine(self, hhl_segmentation, budget_plan = 0, **selected_foods):
        """
        Accepts 3 arguments; 
          A) dictionary of household segmentation
          B) mapping of selected foods to their frequency of consumption
          C) optional argument, budget_plan
             budget_plan is set to a default of Daily.
             
        Accepted values for budget_plan is 0, 1, 2;
        Where;
          0 -> Daily
          1 -> Weekly
          2 -> Monthly
        
        A) Household segmentation
        
        hh_segmentation = {'Males': {'total_child': 2, 'total_adolescent': 1,
                             'total_middle_age': 0, 'total_adult': 0, 
                             'total_aged': 0
                            }, 
                   'Females': {'total_fchild': 0, 'total_fadolescent': 0, 
                               'total_fmiddle_age': 0, 'total_fadult': 0, 
                               'total_faged': 0
                              }
                  }
                  
                  
      B) Selected foods is a dictionary of food(s), the food as key and frequency of consumption as value. As in:
         -> selected_foods = {'Jollof Rice': 1,'Spaghetti':1,'Pap':1}
        """
        assert budget_plan in range(3)
        self.__budget_plan = budget_plan
        self.__data['budget_plan'] = self.__budget_plan
        self.__hhl_segmentation = hhl_segmentation
        
        # handle budget plan with appropriate function, make function calls for each plans
        # call dailybudget
        if self.__budget_plan == 0:
            budget_result = self.__dailybudget(**selected_foods)
        
          
        # call monthlybudget
        elif self.__budget_plan == 2:
            budget_result = self.__monthlybudget(**selected_foods)
        
        
        # get Income Level
        self.__data['Income'] = self.__getIncomeLvl(self.income)
        
        # get Household Size
        self.__data['HH-Size'] = self.__getHouseholdsize(self.hh_size)
        
        # get Household Segmentation
        self.__data['Males'] =  self.__getMale(hhl_segmentation)
        self.__data['Females'] =  self.__getFemale(hhl_segmentation)
        self.__checkHouseholdsize(self.hh_size, self.__data['Males'], self.__data['Females'])
        
        
        # TODO:
        # food selection for each segmentation group
        for males, females in zip(self.__data['Males'], self.__data['Females']):
            if males == 'total_male' or females == 'total_female': pass
            else:
                if self.__data['Males'][males] > 0:
                    if 'child' in males:
                        childqty = self.__ingredientsQtyCompiler(mfq.male_child_foods, **budget_result)
                        totalmchildqty = []
                        for food in childqty:
                            for k,v in food.items():
                                food[k] = self.__data['Males'][males]*v
                            totalmchildqty.append(food)
                        # print(totalmchildqty)
                            
                    if 'adolescent' in males:
                        adolescentqty = self.__ingredientsQtyCompiler(mfq.male_adolescent_foods, **budget_result)
                        totalmadolescentqty = []
                        for food in adolescentqty:
                            for k,v in food.items():
                                food[k] = self.__data['Males'][males]*v
                            totalmadolescentqty.append(food)
                        # print(totalmadolescentqty)
                        
                    if 'middle_age' in males:
                        middleage_qty = self.__ingredientsQtyCompiler(mfq.male_middleage_foods, **budget_result)
                        total_mmiddleage_qty = []
                        for food in middleage_qty:
                            for k,v in food.items():
                                food[k] = self.__data['Males'][males]*v
                            total_mmiddleage_qty.append(food)
                        # print(total_mmiddleage_qty)
                        
                    if 'adult' in males:
                        adultqty = self.__ingredientsQtyCompiler(mfq.male_adult_foods, **budget_result)
                        totalmadultqty = []
                        for food in adultqty:
                            for k,v in food.items():
                                food[k] = self.__data['Males'][males]*v
                            totalmadultqty.append(food)
                        # print(totalmadultqty)
                        
                    if 'aged' in males:
                        agedqty = self.__ingredientsQtyCompiler(mfq.male_aged_foods, **budget_result)
                        totalmagedqty = []
                        for food in agedqty:
                            for k,v in food.items():
                                food[k] = self.__data['Males'][males]*v
                            totalmagedqty.append(food)
                        # print(totalmagedqty)
                        
                        
                    # ADD ALL MALE RESULTS WITH COUNTER
                    for i in self.__data['Males']:
                        if self.__data['Males'][i]>0 and i!='total_male':pass
#                             print(i)
#                             Counter()
                    
                    
                        
                if self.__data['Females'][females] > 0:
                    if 'child' in females:
                        childqty = self.__ingredientsQtyCompiler(ffq.female_child_foods, **budget_result)
                        totalfchildqty = []
                        for food in childqty:
                            for k,v in food.items():
                                food[k] = self.__data['Females'][females]*v
                            totalfchildqty.append(food)
                        # print(totalfchildqty)

                    if 'adolescent' in females:
                        adolescentqty = self.__ingredientsQtyCompiler(ffq.female_adolescent_foods, **budget_result)
                        totalfadolescentqty = []
                        for food in adolescentqty:
                            for k,v in food.items():
                                food[k] = self.__data['Females'][females]*v
                            totalfadolescentqty.append(food)
                        # print(totalfadolescentqty)

                    if 'middle_age' in females:
                        middleage_qty = self.__ingredientsQtyCompiler(ffq.female_middleage_foods, **budget_result)
                        total_fmiddleage_qty = []
                        for food in middleage_qty:
                            for k,v in food.items():
                                food[k] = self.__data['Females'][females]*v
                            total_fmiddleage_qty.append(food)
                        # print(total_fmiddleage_qty)

                    if 'adult' in females:
                        adultqty = self.__ingredientsQtyCompiler(ffq.female_adult_foods, **budget_result)
                        totalfadultqty = []
                        for food in adultqty:
                            for k,v in food.items():
                                food[k] = self.__data['Females'][females]*v
                            totalfadultqty.append(food)
                        # print(totalfadultqty)

                    if 'aged' in females:
                        agedqty = self.__ingredientsQtyCompiler(ffq.female_aged_foods, **budget_result)
                        totalfagedqty = []
                        for food in agedqty:
                            for k,v in food.items():
                                food[k] = self.__data['Females'][females]*v
                            totalfagedqty.append(food)
                        # print(totalfagedqty)
                        
        result_list = []
        for i in ['totalmchildqty', 'totalmadolescentqty', 'total_mmiddleage_qty', 'totalmadultqty', 'totalmagedqty', 'totalfchildqty', 'totalfadolescentqty', 'total_fmiddleage_qty', 'totalfadultqty', 'totalfagedqty']:
            if i in locals() and len(locals()[i])!=0:
                result_list.append(locals()[i])
        # print(result_list)
        
        # compute calculation of all foods gotten from result_list based on type of budget
        if self.__budget_plan == 0:
            self.__result = self.__cumulate_food(result_list)
        
#         elif self.__budget_plan == 1:
#             self.__result = self.__cumulate_food(result_list)
            # TODO: Implement for weekly plan
#             final_result = self.__cumulate_food(result_list)
#             return final_result
        
        elif self.__budget_plan == 2:
            pass
            # TODO: Implement for monthly plan
#             final_result = self.__cumulate_food(result_list)
#             return final_result


    def userData(self):
        '''
        Returns a dictionary of the user inputs
        '''
        return self.__data
    
    
    def result(self):
        # TO BE IMPLEMENTED
#         print(f"Total Ingredients for {self.__data['Males']['total_male']} Males & {self.__data['Females']['total_female']} Females is:")
        for i in self.__result:
            for k,v in i.items():
                if 'Oil' in k:
                    i[k] = str(v)+'ml'
                else:
                    i[k] = str(v)+'g'
        return self.__result
#         return self.__dailybudget()
    
    # Establish some ground rules for deciding qty of ingredients for different classes of persons
    # DONE!! 03/06/21
    

#######################################################################    
#####   Instantiate Food Calculator With Income Level & HH_Size   #####
#######################################################################


# hh_segmentation = {'Males': {'total_child':1, 'total_adolescent': 0,
#                              'total_middle_age': 0, 'total_adult': 0,
#                              'total_aged': 0
#                             }, 
#                    'Females': {'total_fchild': 1, 'total_fadolescent': 0,
#                                'total_fmiddle_age': 0, 'total_fadult': 0,
#                                'total_faged': 0
#                               }
#                   }

budget_plan = {'daily':0, 'monthly':2}

selected_foods = ['Jollof Rice','White Rice','Egusi Soup',
                  'Spaghetti','Porridge','Eba','Pap',
                  'Stew','Efo-riro','Vegetable Soup',
                  'Moin-moin'
                 ]

# calculator = FoodCalculator(income= 0, hh_size=2)


# FOR DAILY BUDGET
# foods = {'Spaghetti':1, 'Eba': 1, 'Pap':1, 'Vegetable Soup':2}
# # pass in the hh_segmentation to the calculator engine
# calculator.engine(hh_segmentation, budget_plan = 0, **foods)
# calculator.result()


# FOR WEEKLY BUDGET
# aa = [{'monday':{'Spaghetti':1, 'Eba': 1, 'Pap':1, 'Vegetable Soup':2}},
#         {'tuesday':{'Pap':1, 'Porridge':1}},
#         {'wednesday':{'White Rice':1, 'Stew': 1, 'Egusi Soup':2}},
#         {'thurday':{'Spaghetti':1, 'Eba': 1, 'Pap':1, 'Vegetable Soup':2}},
#         {'friday':{'Spaghetti':1, 'Eba': 1, 'Pap':1, 'Vegetable Soup':2}},
#         {'saturday':{'Spaghetti':1, 'Eba': 1, 'Pap':1, 'Vegetable Soup':2}},
#         {'sunday':{'Spaghetti':1, 'Eba': 1, 'Pap':1, 'Vegetable Soup':2}},
#         ]
# calculator.weeklybudget(aa)






# GUI BEGINS HERE
st.markdown('''# SOUPE FOOD CALCULATOR

    ''')

# BUILD FIELDS FOR INCOME LEVEL AND HH SIZE
income_range = ['10,000 - 40,000', '41,000 - 100,000',
                '101,000 - 200,000', '201,000+']
hh_size = range(1,501)
budget_plan = ['Daily', 'Weekly', 'Monthly']
selected_income = st.sidebar.selectbox('Select Income Level', income_range)
selected_hh = st.sidebar.selectbox('Select HH-Size', hh_size)
budget_type = st.sidebar.selectbox('Select Budget Type', budget_plan)


# Set HH Segmentation Container
st.beta_container()
hh_expander = st.beta_expander(label='Household Segmentation')
with hh_expander:
    cols = st.beta_columns(2)
    # set headers for male and female
    cols[0].subheader('Male Household Segmentation')
    cols[1].subheader('Female Household Segmentation')
    # generate selectfields
    t_mchild = cols[0].selectbox('Total Male Child', range(10))
    t_madolescent = cols[0].selectbox('Total Male Adolescent', range(10))
    t_mmiddleage = cols[0].selectbox('Total Male Middle-age', range(10))
    t_madult = cols[0].selectbox('Total Male Adult', range(10))
    t_maged = cols[0].selectbox('Total Male Aged', range(10))
    t_fchild = cols[1].selectbox('Total Female Child', range(10))
    t_fadolescent = cols[1].selectbox('Total Female Adolescent', range(10))
    t_fmiddleage = cols[1].selectbox('Total Female Middle-age', range(10))
    t_fadult = cols[1].selectbox('Total Female Adult', range(10))
    t_faged = cols[1].selectbox('Total Female Aged', range(10))


# Set FoodList Container
foodlist = ['Jollof Rice','White Rice','Egusi Soup',
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


# Set Calculate Button
calculateButton = st.sidebar.button('Calculate')




food_freq_mapping = {'Freq1': Food1,'Freq2': Food2,'Freq3': Food3,
                    'Freq4': Food4,'Freq5': Food5,'Freq6': Food6,
                    'Freq7': Food7,'Freq8': Food8,'Freq9': Food9
                    }
if calculateButton:
    calculator = FoodCalculator(income= selected_income, hh_size=selected_hh)

    # FOR DAILY BUDGET
    if budget_type =='Daily':
        track = 0
        foods = {}
        for get_freq in [Freq1,Freq2,Freq3,Freq4,Freq5,Freq6,Freq7,Freq8,Freq9]:
            track+=1
            if get_freq>0:
                curr_food = food_freq_mapping['Freq'+str(track)]
                # print(curr_food)
                foods[curr_food] = get_freq

        # print(foods)
        # foods = {'Spaghetti':1, 'Eba': 1, 'Pap':1, 'Vegetable Soup':2}


        # pass in the hh_segmentation to the calculator engine

        hh_segmentation = {'Males': {'total_child': t_mchild, 'total_adolescent': t_madolescent,
                                 'total_middle_age': t_mmiddleage, 'total_adult': t_madult,
                                 'total_aged': t_maged
                                }, 
                       'Females': {'total_fchild': t_fchild, 'total_fadolescent': t_fadolescent,
                                   'total_fmiddle_age': t_fmiddleage, 'total_fadult': t_fadult,
                                   'total_faged': t_faged
                                  }
                      }




        calculator.engine(hh_segmentation, budget_plan = 0, **foods)
        st.write(f"Total Ingredients Qty for {', '.join(list(foods.keys()))}")
        foodrez = calculator.result()

        ct = 0
        for k in foods.keys():
            st.write(k)
            ab = pd.DataFrame(foodrez[ct].items(), columns=['Ingredients', 'Qty'])
            st.dataframe(ab)
            ct+=1
    elif budget_plan == 'Weekly': pass
        # FOR WEEKLY BUDGET
        # aa = [{'monday':{'Spaghetti':1, 'Eba': 1, 'Pap':1, 'Vegetable Soup':2}},
        #         {'tuesday':{'Pap':1, 'Porridge':1}},
        #         {'wednesday':{'White Rice':1, 'Stew': 1, 'Egusi Soup':2}},
        #         {'thurday':{'Spaghetti':1, 'Eba': 1, 'Pap':1, 'Vegetable Soup':2}},
        #         {'friday':{'Spaghetti':1, 'Eba': 1, 'Pap':1, 'Vegetable Soup':2}},
        #         {'saturday':{'Spaghetti':1, 'Eba': 1, 'Pap':1, 'Vegetable Soup':2}},
        #         {'sunday':{'Spaghetti':1, 'Eba': 1, 'Pap':1, 'Vegetable Soup':2}},
        #         ]
        # calculator.weeklybudget(aa)
    else:
        st.write('Not Yet Implemented!')