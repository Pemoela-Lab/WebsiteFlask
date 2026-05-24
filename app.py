from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Ganti dengan data asli Pemoela Lab
CONTACT = {
    'email': 'pemoela.lab@gmail.com',
    'wa': '6281234567890',
    'address': 'Solo, Jawa Tengah, Indonesia',
    'instagram': 'https://instagram.com/pemoelalab',
    'linkedin': '',
}

SERVICES = [
    {
        'icon': 'M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6',
        'title': 'Website Profil Perusahaan',
        'short_description': 'Tampilkan identitas bisnis Anda secara profesional dengan website yang modern dan menarik.',
        'description': 'Kami merancang dan mengembangkan website profil perusahaan yang merepresentasikan brand Anda secara profesional. Mulai dari desain yang disesuaikan dengan identitas bisnis, hingga konten yang menarik dan informatif.',
    },
    {
        'icon': 'M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z',
        'title': 'Website Komersil / Toko Online',
        'short_description': 'Platform e-commerce lengkap dengan manajemen produk, pembayaran, dan laporan penjualan.',
        'description': 'Bangun toko online yang siap menghasilkan konversi. Dilengkapi dengan fitur manajemen produk, integrasi payment gateway, dan dashboard laporan penjualan yang komprehensif.',
    },
    {
        'icon': 'M5.121 17.804A13.937 13.937 0 0112 16c2.5 0 4.847.655 6.879 1.804M15 10a3 3 0 11-6 0 3 3 0 016 0z',
        'title': 'Website Profil Pribadi',
        'short_description': 'Portfolio digital yang menonjolkan keahlian dan karya Anda kepada dunia.',
        'description': 'Tampilkan diri Anda secara profesional dengan website portfolio pribadi yang unik dan berkesan. Ideal untuk freelancer, profesional, dan kreator konten.',
    },
    {
        'icon': 'M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17H3a2 2 0 01-2-2V5a2 2 0 012-2h14a2 2 0 012 2v10a2 2 0 01-2 2h-2',
        'title': 'Aplikasi Web',
        'short_description': 'Aplikasi web custom sesuai kebutuhan bisnis Anda, dari sistem manajemen hingga platform SaaS.',
        'description': 'Kami membangun aplikasi web yang powerful dan scalable. Dari sistem informasi internal, dashboard analytics, hingga platform SaaS yang siap untuk ribuan pengguna.',
    },
    {
        'icon': 'M7 21a4 4 0 01-4-4V5a2 2 0 012-2h4a2 2 0 012 2v12a4 4 0 01-4 4zm0 0h12a2 2 0 002-2v-4a2 2 0 00-2-2h-2.343M11 7.343l1.657-1.657a2 2 0 012.828 0l2.829 2.829a2 2 0 010 2.828l-8.486 8.485M7 17h.01',
        'title': 'Desain UI/UX',
        'short_description': 'Desain antarmuka yang intuitif dan pengalaman pengguna yang menyenangkan untuk produk digital Anda.',
        'description': 'Tim desainer kami menciptakan antarmuka yang tidak hanya indah secara visual, tetapi juga mudah digunakan dan berfokus pada pengalaman pengguna yang optimal.',
    },
    {
        'icon': 'M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z M15 12a3 3 0 11-6 0 3 3 0 016 0z',
        'title': 'Maintenance & Support',
        'short_description': 'Layanan pemeliharaan website berkala agar performa dan keamanan selalu terjaga.',
        'description': 'Kami menyediakan layanan pemeliharaan rutin untuk memastikan website Anda selalu berjalan optimal, aman dari ancaman siber, dan selalu up-to-date.',
    },
]

PORTFOLIO = []  # Tambahkan proyek di sini saat ada


def ctx():
    return dict(contact_email=CONTACT['email'], contact_wa=CONTACT['wa'])


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static', 'img'),
                               'favicon.png', mimetype='image/png')


@app.route('/')
def home():
    return render_template('index.html', services=SERVICES, portfolio=PORTFOLIO, **ctx())

@app.route('/layanan')
def services():
    return render_template('services.html', services=SERVICES, **ctx())

@app.route('/portofolio')
def portfolio():
    return render_template('portfolio.html', portfolio=PORTFOLIO, **ctx())

@app.route('/tentang-kami')
def about():
    return render_template('about.html', **ctx())

@app.route('/kontak')
def contact():
    return render_template('contact.html', contact=CONTACT, **ctx())


if __name__ == '__main__':
    app.run(debug=True)
