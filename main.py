from flask import Flask, render_template,url_for, request,redirect, jsonify
import cohere
app = Flask(__name__,template_folder='template')


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/process", methods=['POST'])
def process():
    data = request.json
    # # Process the data as needed
    # res=data
    # print(data["input"])
    # return jsonify(res)
    # eg = 'With example explain'
    # text = '''
    # Indian economy: Right from independence, the modernisation of the economy, economic self-sufficiency, and social justice have been the characteristics of the Indian economy. India wanted to acquire modernity and self-reliance by establishing industries. We wanted to establish an economy based on social justice through planning. For this, the National Planning Commission was established to coordinate development through the policy of Five Year Plans.
    # The Narasimha Rao Government started economic reforms from 1991. These economic reforms are called economic liberalisation. The Indian economy flourished as a result of the implementation of this policy. Foreign investment in India increased. Skilled Indian professionals helped reform the Indian economy. The field of information technology opened several avenues of employment in the country. The changes after 1991 are also described as 'globalisation'.
    # '''

    response = co.generate(
        model='command-light-nightly',
        prompt= data["input"],
        max_tokens=1400,
        temperature=1.1,
        k=0,
        stop_sequences=[],
        return_likelihoods='NONE'
    )
    data = {"text":response.generations[0].text}
    return jsonify(data)


# @app.route("/result", methods=['POST'])
# def result():
#     data = request.json
#     # Process the data as needed
#     result=data["input"]
#     return render_template("result.html", result=result)

@app.route("/fullpage")
def fullpage():
   
    return render_template("fullpage.html")

# @app.route('/submit', methods=['POST'])
# def submit():
#     # Process form data
#     data = request.form['input_data']
    
#     # Do something with the data
    
#     # Redirect to the new page
#     return redirect('/result')

if __name__ == "__main__":
    app.run(debug=True)