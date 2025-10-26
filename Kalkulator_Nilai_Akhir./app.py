from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/hitung', methods=["post"])
def hitung():
    nama = request.form["nama"]
    nilai_tugas = float(request.form["nilai_tugas"])
    nilai_uts = float(request.form["nilai_uts"])
    nilai_uas = float(request.form["nilai_uas"])

    nilai_akhir = (nilai_tugas * 0.3) + (nilai_uts * 0.3) + (nilai_uas * 0.4)

    return render_template('hasil.html', nama=nama, nilai_akhir=round(nilai_akhir, 2))

@app.route('/')
def index():
    return render_template('kalkulatorhasilakhir.html')
