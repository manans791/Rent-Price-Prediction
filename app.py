from flask import Flask , render_template ,request
import pickle
import pandas as pd

app = Flask('__name__')


model = pickle.load(open("grid.pkl","rb"))

df = pd.read_csv('Cleaned_data.csv')

@app.route('/')
def home():

    return render_template('index.html')


@app.route('/predict',methods=["GET","POST"])
def predict():
    BHK = request.form.get('BHK')
    Size = request.form.get('Size')
    Floor = request.form.get('Floor')
    Bathroom = request.form.get('Bathroom')

    City = request.form.get('City')

    # Set the corresponding variable based on the selected city
    if City == 'Mumbai':
        city_status_mumbai = 1
        city_status_Delhi = 0
        city_status_Chennai = 0
        city_status_Kolkata = 0
        city_status_Bangalore = 0
        city_status_Hyderabad =0
    elif City == 'Delhi':
        city_status_mumbai = 0
        city_status_Delhi = 1
        city_status_Chennai = 0
        city_status_Kolkata = 0
        city_status_Bangalore = 0
        city_status_Hyderabad =0
    elif City == 'Chennai':
        city_status_mumbai = 0
        city_status_Delhi = 0
        city_status_Chennai = 1
        city_status_Kolkata = 0
        city_status_Bangalore = 0
        city_status_Hyderabad =0
    elif City == 'Kolkata':
        city_status_mumbai = 0
        city_status_Delhi = 0
        city_status_Chennai = 0
        city_status_Kolkata = 1
        city_status_Bangalore = 0
        city_status_Hyderabad = 0
    elif City == 'Bangalore':
        city_status_mumbai = 0
        city_status_Delhi = 0
        city_status_Chennai = 0
        city_status_Kolkata = 0
        city_status_Bangalore = 1
        city_status_Hyderabad = 0
    else:
        city_status_mumbai = 0
        city_status_Delhi = 0
        city_status_Chennai = 0
        city_status_Kolkata = 0
        city_status_Bangalore = 0
        city_status_Hyderabad = 1

    Furnishing_status = request.form.get('Furnishing_status')

        # Set the corresponding variable based on the selected furnishing status
    if Furnishing_status == 'Furnished':
            Furnishing_status_Furnished = 1
            Furnishing_status_Semi_Furnished = 0
            Furnishing_status_Unfurnished = 0
    elif Furnishing_status == 'Semi-Furnished':
            Furnishing_status_Furnished = 0
            Furnishing_status_Semi_Furnished = 1
            Furnishing_status_Unfurnished = 0
    elif Furnishing_status == 'Unfurnished':
            Furnishing_status_Furnished = 0
            Furnishing_status_Semi_Furnished = 0
            Furnishing_status_Unfurnished = 1
    else:
        print('wtf')
        pass

    Tenant_preferred = request.form.get('Tenant_preferred')

        # Set the corresponding variable based on the selected tenant preference
    if Tenant_preferred == 'Bachelors':
            Tenant_preferred_Bachelors = 1
            Tenant_preferred_Family = 0
            Tenant_preferred_Bachelors_Family = 0
    elif Tenant_preferred == 'Family':
            Tenant_preferred_Bachelors = 0
            Tenant_preferred_Family = 1
            Tenant_preferred_Bachelors_Family = 0
    elif Tenant_preferred == 'Both':
            Tenant_preferred_Bachelors = 0
            Tenant_preferred_Family = 0
            Tenant_preferred_Bachelors_Family = 1
    else:
        print('wtf')
        pass

    print(BHK,Size,Floor,Bathroom,City,Furnishing_status,Tenant_preferred)

    prediction = model.predict([[BHK,Size,Floor,Bathroom,city_status_Bangalore,city_status_Chennai,
    city_status_Delhi,city_status_Hyderabad,city_status_Kolkata,city_status_mumbai,
    Furnishing_status_Furnished,Furnishing_status_Semi_Furnished,Furnishing_status_Unfurnished,
    Tenant_preferred_Bachelors,Tenant_preferred_Bachelors_Family,Tenant_preferred_Family]])

    output = round(prediction[0], 2)
    return render_template('index.html', prediction="Your Rent price in selected city would be RS {}".format(output))

    return render_template('index.html')


if __name__=='__main__':
    app.run(debug=True)