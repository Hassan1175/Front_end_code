from  flask import Flask, render_template
project = Flask(__name__)
@project.route('/hello')
def index():
    # return "hello word"
  return  render_template('page_home3.html')
if __name__ ==('__main__'):
    project.run(debug=True)