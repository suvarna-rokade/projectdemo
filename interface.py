from project_app.utils import MedicalInsurance
from flask import Flask, jsonify, render_template, request
import config

app = Flask(__name__)

##################################################################################
 ################################# Base API #####################################
##################################################################################

@app.route('/')
def insurance_model():
    print('Welcome to Medical Insurance Model')
    return render_template('home.html')

##################################################################################
 ################################# Model API #####################################
##################################################################################

@app.route('/predict_charges  ',methods = ['POST','GET'])
def get_insurance_charges():
    if request.method == 'POST':
        print('We are using POST Method')
        data = request.form
        age = eval(data['age'])
        sex = data['sex']
        bmi = eval(data['bmi'])
        children = eval(data['children'])
        smoker = data['smoker']
        region = data['region']

        print(f'age >> {age}, sex >> {sex}, bmi >> {bmi}, children >> {children}, smoker >> {smoker}, region >> {region}  ')
        med_ins = MedicalInsurance(age,sex, bmi, children,smoker, region)
        charges = med_ins.get_predicted_charges()
        # return jsonify({'Result':f"Predicted Medical Insurance Charges are: RS.{charges}"})
        return render_template('index.html', charges=charges)

    else:
        print('We are in GET Method')
        input_data = request.json
        # print('INPUT DATA >> ', input_data)
        age = input_data['age']
        sex = input_data['sex']
        bmi = input_data['bmi']
        children = input_data['children']
        smoker = input_data['smoker']
        region = input_data['region']
        print(f'age >> {age}, sex >> {sex}, bmi >> {bmi}, children >> {children}, smoker >> {smoker}, region >> {region}  ')
        med_ins1 = MedicalInsurance(age,sex, bmi, children,smoker, region)
        charges1 = med_ins1.get_predicted_charges()
        return jsonify({'Result':f"Predicted Medical Insurance Charges are: RS.{charges1}"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = config.PORT_NUMBER, debug= False)


