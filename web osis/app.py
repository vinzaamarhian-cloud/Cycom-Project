from flask import Flask, render_template, request

app = Flask(__name__)

sekbid_osis = {
    1: {"nama": "Sekbid 1",
        "bidang": "Pembinaan Keimanan dan Ketakwaan terhadap Tuhan Yang Maha Esa",
        "anggota": [
            ("Koordinator", "Abdul Hakim"),
            ("Wakil Koordinator", "Haidar Rabbani Winarno"),
            ("Subsie Islam I", "Rakha Fairuz Rafii'udin"),
            ("Subsie Islam II", "Nur Arifah"),
            ("Subsie Protestan", "Yolanda Helena Kezhia Margareth Sinaga"),
            ("Subsie Katolik", "Fiona Febriana Angeline"),
            ("Subsie Hindu", "I Ketut Genta Kusumabuana"),
            ("Subsie Buddha", "Reynaldi Wijaya"),
        ]
        },
    2: {"nama": "Sekbid 2",
        "bidang": "Pembinaan Budi Pekerti Luhur dan Akhlak Mulia",
        "anggota": [
            ("Koordinator", "Abiyan Faiz Prayogo"),
            ("Wakil Koordinator", "Titania Rezky Yumistya Heriyanto Winarno"),
            ("Abdi Masyarakat", "Sessa Asia Puteri"),
            ("Budi Pekerti Luhur I", "Shaliha Rarasita Adiva"),
            ("Budi Pekerti Luhur II", "Bintang Utami Dahayu")
        ]
        },
    3: {"nama": "Sekbid 3",
        "bidang": "Pembinaan Kepribadian Unggul, Wawasan Kebangsaan, dan Bela Negara",
        "anggota": [
            ("Koordinator", "M. Aryasatya Raihan Dzaky"),
            ("Wakil Koordinator", "M. Nabil Zhafran"),
            ("Subsie Pelajar Siaga", "Hannan Akmal Alhanif"),
            ("Subsie Inswapala", "Prabu Pradipta Aryana"),
            ("Subsie Chadika", "Kinaura April Aulia"),
            ("Subsie Pisus", "Uzziel Van Askarillah")
        ]},
    4: {"nama": "Sekbid 4",
        "bidang": "Pembinaan Prestasi Akademik, Seni, dan/atau Olahraga Sesuai Bakat dan Minat",
        "anggota":[
            ("Koordinator", "M. Yazin Atqiya"),
            ("Wakil Koordinator", "Damar Agatha Ibaragi"),
            ("Subbid Prestasi I", "Amelia Tania Putri"),
            ("Subbid Prestasi II", "Fauziah Putri Zahira"),
            ("Subsie Kisma", "Naura Syahirah Rully")
        ]},
    5: {"nama": "Sekbid 5",
        "bidang": "Pembinaan Demokrasi, Hak Asasi Manusia, Pendidikan Politik, Lingkungan Hidup, Kepekaan, dan Toleransi Sosial dalam Konteks Masyarakat Plural",
        "anggota":[
            ("Koordinator", "Omar Alfaridzi Reed"),
            ("Wakil Koordinator", "Fadilah Evan Adriana"),
            ("Sie Litbang I", "Rahmi Hikmatul Layli"),
            ("Sie Litbang II", "Felicia Bintari Samodro"),
            ("Sie Polog I", "Marissa Hafiyani Gumilar"),
            ("Sie Polog II", "Anis Ita Aufa"),
            ("Sie Lingkungan", "Shatara Nareswari Ahmadino")
        ]},
    6: {"nama": "Sekbid 6",
        "bidang": "Pembinaan Kreativitas, Keterampilan, dan Kewirausahaan",
        "anggota":[
            ("Koordinator", "M. Radja Jangkar"),
            ("Wakil Koordinator", "Fathur Muhammad Ayman"),
            ("Subsie Prisma", "Annisa Humaira"),
            ("Subsie Kopsis", "Andi Shira Ramadhani Taslim")
        ]},
    7: {"nama": "Sekbid 7",
        "bidang": "Pembinaan Kualitas Jasmani, Kesehatan, dan Gizi Berbasis Sumber Gizi yang Terdiversifikasi",
        "anggota":[
            ("Koordinator", "M. Guardiano Angelio Zainal"),
            ("Wakil Koordinator", "M. Farhan Raqilla"),
            ("Subbid Bola Besar ", "Fatih Adhwa Ghifari"),
            ("Subbid Bola Kecil", "Firsto Algiven Zerinov Faturochman"),
            ("Subsie SMAC", "Emir Wildansyah Hidayat"),
            ("Subsie PMR", "Driantama Isathrya")
        ]},
    8: {"nama": "Sekbid 8",
        "bidang": "Pembinaan Sastra dan Budaya",
        "anggota":[
            ("Koordinator", "M. Rakha Satrio Bayu"),
            ("Wakil Koordinator", "Kayyisah Jasmine Nara"),
            ("Subbid Seni", "Callysta Salsabila Rivani"),
            ("Subbid Bahasa", "Ayesha Lathifa Zahra Nuriyanto")
        ]},
    9: {"nama": "Sekbid 9",
        "bidang": "Pembinaan Teknologi, Informasi, dan Komunikasi",
        "anggota":[
            ("Koordinator", "Argya Danendra Permana"),
            ("Wakil Koordinator", "Yocalvin Manggala Ananta"),
            ("Subbid Aptek I", "Kilau Ramadhanti Mumpuni Sembada"),
            ("Subbid Aptek II", "Kaylila Aletta Kusuma"),
            ("Subbid Aptek III", "Everett East Damaindah"),
            ("Subsie Cycom", "Rais Affan Zahi")
        ]},
    10: {"nama": "Sekbid 10",
        "bidang": "Pembinaan Komunikasi dalam Berbahasa Inggris",
        "anggota":[
            ("Koordinator", "Rafa Trystan Bagaskara"),
            ("Wakil Koordinator", "Raditya Firlian Komala"),
            ("Subbid English I", "Marsya Inetha Rozandar"),
            ("Subbid English II", "Agnes Charissa Oktaviani"),
            ("Subsie ECC", "Clarissa Putriana Khoirunnisa")
        ]}
}
kegiatan_osis = [
    {
        "id": 1,
        "nama": "SOTY",
        "kategori": "pendidikan",
        "tanggal": "-",
        "deskripsi": "🏆 𝐒𝐎𝐓𝐘 🏆 merupakan program kerja dengan kegiatan pemilihan siswa/i berprestasi rekaputilasi prestasi terbanyak yang diperoleh para siswa/i melalui registrasi 🏆 𝐒𝐎𝐓𝐘 🏆. Dengan mengangkat tema “𝘾𝙖𝙝𝙖𝙮𝙖 𝙋𝙧𝙚𝙨𝙩𝙖𝙨𝙞 𝙈𝙚𝙣𝙪𝙟𝙪 𝙈𝙖𝙨𝙖 𝘿𝙚𝙥𝙖𝙣 𝙂𝙚𝙢𝙞𝙡𝙖𝙣𝙜” 🏆 𝐒𝐎𝐓𝐘 🏆 sukses dilaksanakan.",
    },
    {
        "id": 2,
        "nama": "TREE FOR LIFE AND GREEN",
        "kategori": "lingkungan",
        "tanggal": "2025-06-12",
        "deskripsi": "🪴𝑻𝑹𝑬𝑬 𝑭𝑶𝑹 𝑳𝑰𝑭𝑬 𝑨𝑵𝑫 𝑮𝑹𝑬𝑬𝑵 ⋆.˚ ᡣ𐭩 .𖥔˚🪴 adalah kegiatan peringatan Hari Lingkungan Hidup Sedunia di SMAN 1 Bekasi yang bertujuan mewujudkan sekolah ramah lingkungan melalui penanaman, pembuatan ecobricks, dan pembuatan kompos dengan partisipasi aktif dari seluruh kelas.",
    },
    {
        "id": 3,
        "nama": "Gebyar Kartini",
        "kategori": "pendidikan",
        "tanggal": "2025-04-21",
        "deskripsi": "⋆.˚🎊𝙂𝙚𝙗𝙮𝙖𝙧 𝙆𝙖𝙧𝙩𝙞𝙣𝙞🎊⋆.˚ adalah kegiatan untuk memperingati serta mengenang kembali perjuangan R.A. Kartini sebagai pelopor emansipasi wanita di Indonesia.",
    },
    {
        "id": 4,
        "nama": "Hari Buku",
        "kategori": "sosial",
        "tanggal": "2025-03-08",
        "deskripsi": "📚𝐇𝐚𝐫𝐢 𝐁𝐮𝐤𝐮📚 merupakan kegiatan kunjungan serta sosialisasi pada asrama yatim oleh OSIS SMAN 1 Bekasi serta pemberian donasi buku dan perlengkapan pembelajaran yang dikumpulkan oleh siswa-siswi SMAN 1 Bekasi.",
    },
    {
        "id": 5,
        "nama": "Bulan Bahasa",
        "kategori": "pendidikan",
        "tanggal": "2025-10-11",
        "deskripsi": "Pada 28 Oktober 2024, SMAN 1 Bekasi memperingati Hari Sumpah Pemuda dengan penuh semangat melalui 𝘽𝙪𝙡𝙖𝙣 𝘽𝙖𝙝𝙖𝙨𝙖  dengan tema “𝗠𝗲𝗻𝗷𝘂𝗻𝗷𝘂𝗻𝗴 𝗦𝗮𝘀𝘁𝗿𝗮 𝗱𝗮𝗻 𝗕𝘂𝗱𝗮𝘆𝗮 𝗜𝗻𝗱𝗼𝗻𝗲𝘀𝗶𝗮 𝘂𝗻𝘁𝘂𝗸 𝗠𝗲𝗻𝗴𝗴𝗮𝗽𝗮𝗶 𝗜𝗺𝗽𝗶𝗮𝗻 𝗣𝗲𝗺𝘂𝗱𝗮 𝗣𝗲𝗺𝘂𝗱𝗶 𝗜𝗻𝗱𝗼𝗻𝗲𝘀𝗶𝗮.”",
    }
]

pengurus_osis = [
    {"nama": "Nayma Taqiyya Syarif", "jabatan": "Ketua Umum"},
    {"nama": "Fahri Fathurrahman", "jabatan": "Ketua I"},
    {"nama": "Esa Darma Faiza Rahman", "jabatan": "Ketua II"},
    {"nama": "Khaira Lubna Arifatunnisa", "jabatan": "Sekretaris Umum"},
    {"nama": "Cheverly Ananqya Tourishia", "jabatan": "Bendahara Umum"}
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/pengurus")
def pengurus():
    sort_by = request.args.get("sort")
    
    data = pengurus_osis
    
    if sort_by == "nama":
        data = sorted(data, key=lambda x: x["nama"].lower())
    elif sort_by == "jabatan":
        sorted(data, key=lambda x: x["jabatan"].lower())
    
    return render_template("pengurus.html", pengurus=data)

@app.route("/kegiatan")
def kegiatan():
    keyword = request.args.get("search")
    kategori = request.args.get("kategori")
    
    hasil = kegiatan_osis
    
    if keyword:
        hasil = [
            k for k in hasil
            if keyword.lower() in k["nama"].lower()
            or keyword.lower() in k["deskripsi"].lower()
        ]
            
    if kategori:
        hasil = [
            k for k in hasil
            if k["kategori"] == kategori
        ]
    return render_template("kegiatan.html", kegiatan=hasil)

@app.route("/kegiatan/<int:id>")
def detail_kegiatan(id):
    kegiatan = next(
        (k for k in kegiatan_osis if k["id"] == id),
        None
    )
    return render_template("detail_kegiatan.html", kegiatan=kegiatan)

@app.route("/sekbid/<int:no>")
def sekbid(no):
    data = sekbid_osis.get(no)
    if not data:
        return "Sekbid tidak ditemukan", 404
    
    return render_template(
        "sekbid.html",
        no=no,
        sekbid=data
    )

if __name__ == "__main__":
    app.run(debug=True)
