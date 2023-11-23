from flask import Flask, render_template,url_for, redirect
from flask import request
import csv

app = Flask(__name__)
print(__name__)

app = Flask(__name__, static_folder='static')

@app.route('/<string:page_name>')
def html_page(page_name):
  return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'/n/ {email},{subject},{message}')


def write_to_csv(data):
    with open('mydatabase.csv',newline = '' ,mode='a') as mydatabase:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(mydatabase, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])



@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return'did not save to database'
    else:
        return'something went wrong. Try again!'



    
        
