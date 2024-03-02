'''
Created by Narendra for COMP216 June 2020 (modified June 2021)
wk05_a00_server.py

A flask application to handle request for lab05.
Not meant for code inspection
Might contain advanced coding
'''

# from types import resolve_bases
from random import choice, randint
from flask import Flask, url_for
from flask import request, session
from flask.helpers import make_response, send_file

# from requests.sessions import session

f_name = 'Abhi Alisha Amit Amrit Anosh Anuben Arielle Aritra Arpit Auraham Balachander Brandon Chadwick Chaitanya Christine Davut Devanshi Diego Dishank Divya Divyanshu Diwakar Dominic Gagandeep Gurleen Gurvir Harsh Heesoo Hitesh Huseyin Hussam Isaac Jashan Jefil Jiabao Joshua Kautuk Keval Keyurkumar Hung Krunal Luiz Mahmud Manpreet Maximino Shahzaman Mithil Nabil Amani Namirabanu Nestor Nidhi Nikhileswar Niyanta Nusrat Osman Prince Priti Rahul Riaz Robin Rozita Samridhi Shawn Shivam Shrikant Silviya Smit Sreelakshmi Yasmin Vaishali Viktoriia Vishal Wonsuk Xin Yi Xu-Tung'.split()
l_name = 'Ahmed Ambarukhana Bindal Cha Coelho Corlu Mattos Dharmadhikari Duvvuru Ferdaus Ganguly Harding Jin Jitu Johar Mohan Kale Kalwachia Kamal Kansara Kaur Keshavala Kim Kumar Kuru Kweri Lakhan Lam Lapis Liao Lim Malek Malik Mandavia Martin Miroshnikov Mohamed Mueller Nair Narvaez Ommi Palepu Parmar Parvej Patel Phan Pushpan Riaz Rodrigues Romaniuk Romero Roy Sapkota Shah Sheladeeya Siddeshwar Siddhapura Singh Soleimani Tahir Timbol Trivedi Udavant Vandenbrande Velani Verma Yadav Yang'.split()
programs = '3109 3402 3409 3419 3422 3429 3432 3469 3472 3508 3518 3528'.split()
users = {
    'ilia': {
        'fname': 'Ilia',
        'lname': 'Nika',
        'age': 56
    },
    'narendra': {
        'fname': 'Narendra',
        'lname': 'Pershad',
        'age': 45
    },
    'mehrdad': {
        'fname': 'Mehrdad',
        'lname': 'Tirandazian',
        'age': 40
    },
    'mayy': {
        'fname': 'Mayy',
        'lname': 'Habayeb',
        'age': 40
    },
    'vinay': {
        'fname': 'Vinay',
        'lname': 'Vaithilingam',
        'age': 40
    },
    'hao': {
        'fname': 'Hao',
        'lname': 'Lac',
        'age': 40
    }
}

app = Flask(__name__)

app.config['SECRET_KEY'] = 'super secret'           #this is needed for session

def process_docstring(docs):
    raw = docs.splitlines()              #split into lines
    tok = [x.strip() for x in raw]       #remove leading and trailing spaces
    tok = [x for x in tok if len(x) > 0] #remove empty tokens
    result = tok[0] + '</a><br/>'        #first token will the part of the hyper link
    for x in range(1, len(tok)):         #skip the first token
        result += tok[x] + '<br/>'       #just add text to the result
    return result +'</br>'

@app.route('/')
def index():
    '''
    The main landing page
    Builds a lisk of all the routes published by this flask application
    Appends the doc string to each route. The result is what you are seeing now!
    '''
    result = '<ol>'
    for route in app.url_map.iter_rules():
        if  route.endpoint != 'static':
            result += f'<li> <a href="{route}">{process_docstring(eval(route.endpoint).__doc__)}' + '</li>'
    return result + '</ol>'

# @app.route('/a4_headers')    
@app.route('/a4_headers')
def headers():
    '''
    Returns some static text to the client
    Check the server terminal for the request headers
    '''
    print(f'\n\nFrom the client:') 
    print(f'{request.headers}') 
    return 'Check the server terminal for the client headers'

@app.route('/test1') 
def test1():                                
    '''
    returns a single json object (dictionary) to the client<br/>[browser sup]
    '''
    return {'name': 'Narendra', 'course': 'COMP216', 'semester': 'Fall 2020'}

@app.route('/a3_query_string')
def query_strin():
    '''
    Returns the arguments that was sent by the request<br/>[browser sup only if query string supplied]
    '''
    return request.args

@app.route('/a5_user_agents')
def show_user_agent():
    '''
    Returns the user agent to the client
    '''
    # return str(request.user_agent)
    print(f'\n\nClient user agent:') 
    print(f'{request.user_agent}') 
    return 'Check the server terminal for the client headers'


@app.route('/profs/')
def show_profs():
    '''
    Returns all the users in the collection<br/>[browser sup]
    '''
    return users

@app.route('/set_cookies')
def set_cookies():
    '''
    Returns the cookies that was sent to this server
    '''
    response = make_response()
    response.set_cookie('code', 'COMP216')
    response.set_cookie('name', 'Networking for Software Developers')
    response.set_cookie('instructor', 'narendra pershad')
    return response

@app.route('/get_cookies')
def get_cookies():
    '''
    Returns the cookies that was sent to this server
    '''
    print(request.cookies)
    # return 'Check the server terminal for the client headers'
    return(request.cookies)

@app.route('/read_session')
def read_session():
    '''
    Returns the number of time a visitor lands of this page<br/>[Browser sup]
    Checks if the value is in the session variable. 
    If the value is present one is added to it
    If it is not present it is assigned to one 
    '''
    key = 'visits'
    if key in session:
        count = session.get(key) + 1
        session[key] = count
    else:
        print('setting variable for the first time')
        session[key] = 1

    return f'You have visited this site {session.get(key)} times'

@app.route('/students/<int:number_of_students>', methods=['POST', 'GET'])
def get_students(number_of_students):
    '''
    Provides the means for a client to download a file from the server.
    It will append a .bak extension the file when 
    saving and return this new name to the client.
    '''
    result = {}
    for i in range(number_of_students):
        result[i] = {
            'fname': choice(f_name), 
            'lname': choice(l_name), 
            'age': randint(20, 30), 
            'gpa': randint(1, 17)/4,
            'domestic': randint(1, 10) > 5,
            'program': choice(programs),
            'semester': randint(2, 6)}
    return result

@app.route('/download/<path:filename>', methods=['POST', 'GET'])
def a8_file_download(filename):
    '''
    Provides the means for a client to download a file from the server.
    It will append a .bak extension the file when 
    saving and return this new name to the client.
    '''
    return send_file(filename_or_fp=filename)

@app.route('/upload', methods=['POST'])
def a9_file_upload():
    '''
    Provides the means for a client to upload a file to this server.
    File goes into the client_upload folder.
    '''
    path = 'client_upload/'
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        uploaded_file.save(f'{path}{uploaded_file.filename}')
    return f'{uploaded_file.filename} successfully uploaded'


@app.route('/admin/add', methods = ['POST'])
def add_prof(): 
    '''
    Adds a user to the data store
    A message is returned to the client
    This end point can only be accessed via a POST command
    '''     
    prof = request.get_json() 
    users.update(prof)
    return f' {prof} was added to the list of registered users'

@app.route('/auth')
def authRouteHandler():
    '''
    Implements Basic Authorization
    Not completed, more work needed!
    '''
    print(request.authorization["username"])
    print(request.authorization["password"])
 
    return 'ok'

@app.route('/admin-form', methods=['GET', 'POST']) 
def form_example():
    '''
    The endpoint is able to process both GET and POST requests<br/>[browser sup]
    GET returns a table of the form data submitted
    POST returns an input form to capture data
    '''
    if request.method == 'POST':
        print(request.args)                      #returns a table to the client
        return f'''
        <table>
        <tr><td>First name</td><td>-- {request.form.get('fname')} --</td></tr>
        <tr><td>Last name</td><td>-- {request.form.get('lname')} --</td></tr>
        <tr><td>Age</td><td>-- {request.form.get('age')} --</td></tr>
        <tr><td colspan="2"><input type="submit" value="Submit"></td></tr>
        </table>
        '''
    else:                                        #HTTP GET command, returns an html form 
        return '''
        <form method="POST">
        <table>
        <tr><td>First name</td><td><input type="text" name="fname"></td></tr>
        <tr><td>Last name</td><td><input type="text" name="lname"></td></tr>
        <tr><td>Age</td><td><input type="text" name="age"></td></tr>
        <tr><td colspan="2"><input type="submit" value="Submit"></td></tr>
        </table>
        </form>
        '''


@app.route('/blog/<int:postID>')      #using converter type
def show_blog(postID):
    '''
    Returns some text prepended to your parameter<br/>[browser sup only if argument is supplied]
    '''
    return f'Blog Number: {postID}'

if __name__ == '__main__':
	app.run(debug=True)      #app.run(host, port, debug, options)


#curl --request GET --url http://127.0.0.1:5000/

# GET /people reads all the people
# POST /people creates a person and adds to list
# DELETE /people/{key} deletes a person
# GET /people/{key} reads a person
# PUT /people/{key} updates a person

'''
<li> <a href="/admin/add">Adds a user to the collection</a><li/><li> <a href="/admin-form">
    GET returns a table of the form submitted<br/>
    POST returns an input form
    </a><li/>
<li> <a href="/test0">
    Returns some static text<br/>
    Check the server terminal for the request headers
    </a><li/>
<li> <a href="/test1">returns a static json object (dictionary)</a><li/>
<li> <a href="/test2">Returns the arguments that was sent by the request</a><li/>
<li> <a href="/profs/">Returns all the users in the collection </a><li/><li> <a href="/">The main landing page</a><li/><li> <a href="/blog/<int:postID>">Returns some text prepended to your parameter</a><li/>
'''