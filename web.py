import csv
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    try:
        weight = float(request.form['weight'])
        height = float(request.form['height'])
        bmi = weight / (height ** 2)

        goal = request.form['goal']

        food_items = []
        with open('food.csv', mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                food_items.append(row)

        recommended_food = {'Breakfast': [], 'Lunch': [], 'Dinner': []}
        for item in food_items:
            food_name = item['Food_items']
            gain_weight = item['Gain weight']
            lose_weight = item['Lose weight']
            breakfast = item['Breakfast']
            lunch = item['Lunch']
            dinner = item['Dinner']

            if goal == 'gain_weight' and gain_weight == '0':
                if breakfast == '0' and lunch == '0' and dinner == '0':
                    recommended_food['Breakfast'].append(food_name)
                    recommended_food['Lunch'].append(food_name)
                    recommended_food['Dinner'].append(food_name)
            elif goal == 'lose_weight' and lose_weight == '1':
                if breakfast == '1':
                    recommended_food['Breakfast'].append(food_name)
                if lunch == '1':
                    recommended_food['Lunch'].append(food_name)
                if dinner == '1':
                    recommended_food['Dinner'].append(food_name)

        result_html = f'''
        <h2>Result:</h2>
        <p>BMI: {bmi:.2f}</p>
        <p>Goal: {goal}</p>
        <h3>Recommended Food:</h3>
        <table border="1" style="width: 100%; border-collapse: collapse;">
            <tr>
                <th style="padding: 10px;">Meal</th>
                <th style="padding: 10px;">Recommended Food</th>
            </tr>
            <tr>
                <td style="padding: 10px;">Breakfast</td>
                <td style="padding: 10px; text-align: center; vertical-align: middle; height: 150px;">{', '.join(recommended_food['Breakfast'])}</td>
            </tr>
            <tr>
                <td style="padding: 10px;">Lunch</td>
                <td style="padding: 10px; text-align: center; vertical-align: middle; height: 150px;">{', '.join(recommended_food['Lunch'])}</td>
            </tr>
            <tr>
                <td style="padding: 10px;">Dinner</td>
                <td style="padding: 10px; text-align: center; vertical-align: middle; height: 150px;">{', '.join(recommended_food['Dinner'])}</td>
            </tr>
        </table>
        '''
        return result_html
    except Exception as e:
        print("Error occurred:", e)
        return "An error occurred while processing the request."

if __name__ == '__main__':
    app.run(port=8080, debug=True)
