from flask import Flask, render_template,url_for, request,redirect, jsonify
import openai
import os
app = Flask(__name__,template_folder='template')


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/process", methods=['POST'])
def process():
    data = request.json
    # # Process the data as needed
    resp1,resp2=easyexplain(data["input"])
    # res=data
    # print(data["input"])
    # return jsonify(res)
    # eg = 'With example explain'
    # text = '''
    # Indian economy: Right from independence, the modernisation of the economy, economic self-sufficiency, and social justice have been the characteristics of the Indian economy. India wanted to acquire modernity and self-reliance by establishing industries. We wanted to establish an economy based on social justice through planning. For this, the National Planning Commission was established to coordinate development through the policy of Five Year Plans.
    # The Narasimha Rao Government started economic reforms from 1991. These economic reforms are called economic liberalisation. The Indian economy flourished as a result of the implementation of this policy. Foreign investment in India increased. Skilled Indian professionals helped reform the Indian economy. The field of information technology opened several avenues of employment in the country. The changes after 1991 are also described as 'globalisation'.
    # '''
    # co = cohere.Client(os.getenv("COHERE_API_KEy")}  # This is your trial API key


    # response = co.generate(
    #     model='command-light-nightly',
    #     prompt= data["input"],
    #     max_tokens=1400,
    #     temperature=1.1,
    #     k=0,
    #     stop_sequences=[],
    #     return_likelihoods='NONE'
    # )
    data = {"text":resp1,"text2":resp2}
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
@app.route("/TextToImg.html")
def TextToImg():
    return render_template("TextToImg.html")


# @app.route("/processimage", methods=['POST'])
# def processimage():
#    img = response.json
#    url = img["url"]
#    return jsonify(url)







def easyexplain(var):
  
  # Set up your OpenAI API credentials
  openai.api_key = os.getenv("OPENAI_API_KEY")

  # Prompt for the model to generate child-like speech

  #variable 
  prompt = f"explain this concept like i am 2 year child , {var}"

  # Generate text with GPT-3.5 model
  response = openai.Completion.create(
  engine="text-davinci-003",  # Specify the GPT model (e.g., text-davinci-003)
  prompt=prompt,
  max_tokens=100,  # Adjust the max tokens based on the desired response length
  temperature=0.8,  # Controls the randomness of the generated output
  n=1,  # Number of responses to generate
  stop=None,  # Stop sequence to end the generated text (optional)
  )
  prompt_ana = f"create an analogy or example for this phrase : \n {var}"
  resp2=generate_analogy(prompt_ana)
  # Print the generated child-like response
  return [response.choices[0].text.strip(), resp2]

def generate_analogy(prompt):
  openai.api_key = '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'

    # Generate text with GPT-3.5 model
  print(" analogy  ")
  response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=200,
        temperature=0.8,
        n=1,
        stop=None,
    )

    # Return the generated analogy
  return response.choices[0].text.strip()

 
    
if __name__ == "__main__":
    app.run(debug=True)