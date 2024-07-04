from flask import Flask,render_template,request
import pickle
import numpy as np

app = Flask(__name__)

def load_model():
    with open('medicine.pkl','rb') as file:
        data = pickle.load(file)
    return data

obj = load_model()
sim = obj['similarity']
df = obj['data']


med_names = df['name'].values

def recommend(new_med):
    # obtaining the index of the new person from the dataframe
    ind = df[df['name'] == new_med].index[0]
    #'cosine[ind]' obtains the similarity for the 'new person','list(enumerate())'  creates a list of an 
    # iterable that produces pairs of (index, value),'sorted' sorts the list, 'reverse=True' sorts
    # the list in descending order rather than default ascending order,'key = lambda x:x[1]' specifies that 
    # list should be sorted using the similarity not its index i.e [(3,0.98),(2,0.67),(1,0.45)]
    distance = sorted(list(enumerate(sim[ind])),reverse = True,key = lambda x: x[1])
    recos = []
    for i in distance[1:6]:
        recos.append(df['name'].iloc[i[0]])
        
    return recos

@app.route('/')
def homepage():
    return render_template('med.html',med_names = med_names)

@app.route('/recommend',methods=['POST'])
def get_recommendation():
    final = {}
    name_of_medicine = request.form.get('med')
    recos = recommend(name_of_medicine)
    for i in recos:
        matched_rows = df[df['name'] == i]
        for index, row in matched_rows.iterrows():
            final[i] =  row['img']
            
    return render_template('med.html',recommendations = final,med_names =  med_names,name_of_medicine = name_of_medicine)

if __name__ == "__main__":
    app.run(host="0.0.0.0")