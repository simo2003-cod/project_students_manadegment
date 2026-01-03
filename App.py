from flask import Flask, request,  render_template, redirect, url_for,flash
from bson.objectid import ObjectId
from config import students

pro = Flask(__name__)
pro.secret_key = "something_super_secret_and_random"
 
@pro.route('/')
def home():
    count = students.count_documents({})
    return render_template('home.html', count = count)

@pro.route('/students')
def list_students():
    data = list(students.find())
    return render_template('list.html',data = data)

@pro.route("/update_student",methods=['POST'])
def update():
    if request.method == 'POST':
        if request.form['update'] == "false":
            cod = request.form['id']
            data = list(students.find({"id":cod}))
            print(data)
            return render_template('update.html',student = data[0])
        else:
            cod = request.form['id']
            name = request.form['name']
            email = request.form['email']
            age = request.form['age']
            students.update_one({"id":cod},{"$set":{"name":name,"email":email,"age":age}})
            flash({"msg": "Student updated successfully","class": "upd","action": "updated"})      
            return redirect(url_for('list_students'))
        
    return redirect(url_for('home'))

@pro.route('/delete_student',methods=["POST"])
def delete():
    if request.method == "POST":
        cod = request.form['id']
        students.delete_one({"id":cod})
        flash({"msg": "Student deleted successfully","class": "del","action": "delete"})      
        return redirect(url_for('list_students'))
    return redirect(url_for('home'))
    
    
@pro.route('/add_student',methods=['GET','POST'])
def add_students():
    if request.method == 'POST':
        last_student = students.find_one(sort=[('id',-1)])
        if (last_student):
            cod = str(int(last_student['id'])+1)
        else:
            cod = "1"
        name = request.form['name']
        email = request.form['email']
        age = request.form['age']
        students.insert_one({"id":cod,"name":name,"email":email,"age":age})
        flash({"msg": "Student added successfully","class": "add","action": "add"})      
        return redirect(url_for('list_students'))
    return render_template('add.html')
        


if __name__ == "__main__":
    pro.run(debug=True)



"""
/
/add_student
/update_student 
/students
/delete
"""



