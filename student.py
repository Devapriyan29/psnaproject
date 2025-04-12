from flask import Flask,request,render_template,redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
import pandas,csv,smtplib
app=Flask(__name__)

#data = pandas.read_csv("pro1.csv")
@app.route('/')
def home():
    return render_template("login.html")


app.secret_key = 'your_secret_key'  # Needed for session management

# Simulated user database (replace with a real database in production)
users = {
    "testuser": generate_password_hash("password123")
}
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and check_password_hash(users[username], password):
            session['username'] = username
            flash('Login successful!', 'success')
            return render_template('student.html')
        else:
            flash('Invalid username or password', 'danger')
            return home()







@app.route("/show",methods=['POST','GET'])
def finish():
    try:
        global ma
        ro1=request.form.get("roll")
        ro=int(ro1)
        data = pandas.read_csv("pro1.csv")
        det = data[data.NewRegNo == ro]
        nam = det.StudentName.tolist()
        date = det.DOB.tolist()
        mob = det.StudentMobileNo.tolist()
        reg = det.NewRegNo.tolist()
        blg=det.BloodGroup.tolist()
        doh=det.daysorhos.tolist()
        co=det.Community.tolist()
        mail=det.PSNAMailId.tolist()
        pm=det.EmailID.tolist()
        fname=det.FatherName.tolist()
        fmob=det.FatherMobileNo.tolist()
#------------------------------------------------------------------------------------------------#
        namm=nam[0]
        datee=date[0]
        mobb=mob[0]
        regg=reg[0]
        bgg=blg[0]
        dh=doh[0]
        coom=co[0]
        ma=mail[0]
        pmm=pm[0]
        fn=fname[0]
        fm=fmob[0]
        l=[]
        return render_template("details.html",ne=namm,da=datee,mo=mobb,re=regg,bg=bgg,dohh=dh,com=coom,mai=ma,pmail=pmm,fath=fn,fathm=fm,reg=ro)
    except(IndexError):
        print("error")


@app.route('/sent',methods=['POST','GET'])
def em():
    return render_template("mesg.html")

@app.route('/message',methods=['POST','GET'])
def anupu():
    con=request.form.get("cont")
    u = "devap3784@gmail.com"
    p = "qesz ombl wesm tdrm"

    a = smtplib.SMTP("smtp.gmail.com", 587)
    a.starttls()
    a.login(user=u, password=p)
    a.sendmail(from_addr=u, to_addrs=ma,msg=f"Subject:Kind attention\n{con}")
    a.close()
    return render_template("success.html")
if __name__=="__main__":
    app.run(debug=True)

