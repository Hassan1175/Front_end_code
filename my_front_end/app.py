from  flask import Flask, render_template
app= Flask(__name__)
@app.route('/')
def home():
  return  render_template('page_home3.html')

@app.route('/about')
def about():
    return render_template('page_about3.html')

@app.route('/projects')
def projects():
    return render_template('page_profile_projects.html')

@app.route('/login')
def login():
    return render_template('page_login.html')


@app.route('/registeration')
def registration():
    return render_template('page_registration.html')

@app.route('/profile')
def profile_main():
    return render_template('page_profile.html')

@app.route('/my_projects')
def my_projects():
    return render_template('page_profile_projects.html')

@app.route('/my_history')
def my_history():
    return render_template('page_profile_history.html')



@app.route('/my_profile')
def my_profile():
    return render_template('page_profile_me.html')






if __name__ ==('__main__'):
    app.run(debug=True)