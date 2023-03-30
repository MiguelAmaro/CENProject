
'''
first_name = st.text_input("Enter your name")
st.write(f"your last name {first_name}")
last_name = st.text_input("Enter you last name")
year_of_birth = st.number_input("Eter your year of birth")
fiu_start_date = st.number_input("Enter the year you started at FIU")

current_year = datetime.date.today().year
age = current_year-year_of_birth
year_at_fiu = current_year-fiu_start_date

if first_name and last_name and fiu_start_date:
    st.write(f"{first_name} {last_name}"
            f"you are {age} years old and you have"
            f"been at fiu for {year_at_fiu} years")
'''

