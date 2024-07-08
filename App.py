import streamlit as st
from calculator_fuctions.calculator import CarbonFootprintCalculator, generate_recommendations
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

calculator = CarbonFootprintCalculator()

def send_email(carbon_footprint, recommendations, receiver_email):
    # Set up the SMTP server
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "hh50315510@gmail.com"
    password = "itoqxwmuscehohqq"

    # Create message container
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "Carbon Footprint Calculation"

    # Add message body
    body = f"Your total carbon footprint is: {carbon_footprint} kg CO2e\n\nRecommendations to reduce your carbon footprint:\n"
    for recommendation in recommendations:
        body += f"- {recommendation}\n"
    msg.attach(MIMEText(body, 'plain'))

    # Send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

def main():
    st.set_page_config(page_title="Carbon Footprint Calculator", page_icon="🌍", layout="wide")

    st.title("Carbon Footprint Calculator")

    st.write("Welcome to the Planet-Pulse ـــــــــــــﮩ٨ـ❤️ﮩ٨ـﮩﮩ٨ـ!")

    # Add SVG image
    
    st.image("Assets/Untitled design (1).svg", use_column_width=True)

    # User inputs
    transport_method = st.selectbox("Select Transport Method", ["gas_car", "electric_car", "bus", "train", "bike", "walk"]).lower()
    distance = st.number_input("Distance (in miles)")
    usage = st.number_input("Electric Usage (in kWh)")
    category = st.selectbox("Select Food Category", ["Beef", "Pork", "Chicken", "fish", "vegetables", "fruits"])
    num_of_meals = st.number_input("Number of Meals")

    # Allow user to input their email
    receiver_email = st.text_input("Enter your email address")

    # Calculate carbon footprint using the class
    total_carbon_footprint = 0  # Initialize
    if st.button("Calculate Carbon Footprint"):
         calculator.transport_footprint(transport_method.lower(), distance)
         calculator.electricity_footprint(usage)
         calculator.food_footprint(category.lower(), num_of_meals)
         total_carbon_footprint = calculator.calculate_total_carbon_footprint()


        # Display results
         st.write(f"Your total carbon footprint is: {total_carbon_footprint} kg CO2e")
        
        # Generate recommendations
    recommendations = generate_recommendations(total_carbon_footprint)
    st.write("Here are some recommendations to reduce your carbon footprint:")
    for recommendation in recommendations:
            st.write("- " + recommendation)

        # Send email button
    if receiver_email and st.button("Send Email"):
       send_email(total_carbon_footprint, recommendations, receiver_email)
       st.write("Email sent successfully!")

if __name__ == "__main__":
    main()

