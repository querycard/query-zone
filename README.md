(https://khansa-dinda-queryzone.pbp.cs.ui.ac.id/)

# Tugas 4

1. Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.
    - Django AuthenticationForm adalah sebuah class berupa form untuk proses login user yang akan menangani validasi username dan password user. 
    - Kelebihan dari Django AuthenticationForm adalah sudah terdapat built-in security termasuk password hashing, validasi lengkap saat login, serta terdapat feedback saat login gagal. Django AuthenticationForm juga merupakan tipe yang siap pakai sehingga tidak perlu membuat form dari awal. 
    - Kekurangan dari Django AuthenticationForm adalah default field yang diterimanya terlalu umum, yaitu terbatas pada username dan password. Sehingga, tidak bisa otomatis untuk login yang lebih kompleks seperti email atau OTP. Lalu, Django AuthenticationForm tidak cocok untuk REST API karena dirancang untuk form berbasis HTML. Ditambah, tampilan dari Django AuthenticationForm harus dikustomisasi sendiri dengan membuat template HTML secara manual.
2. Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
    - Autentikasi adalah proses untuk memverifikasi siapa user yang sedang login. Sedangkan, otorisasi adalah proses untuk memverifikasi apakah user mempunyai akses ke suatu hal.
    - Konsep autentikasi diimplementasikan pada sistem login/logout. Contohnya penggunaan fungsi login, logout, dan authenticate.
    - Konsep otorisasi pada django diimplementasikan dengan sistem permission dan group. Contohnya pada decorator pada fungsi seperti @login_required ataupun @permission_required
3. Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
    - Kelebihannya adalah dapat menutupi kekurangan HTTP yang merupakan stateless protocol, dengan cara menyimpan session ID sebagai cookie pada komputer klien dan mengirimnya kepada server saat mengirimkan request. Sehingga, session user yang sedang menggunakan web bisa berjalan selama jangka waktu tertentu tanpa harus login berulang kali. Lalu, data yang disimpan untuk identifikasi session merupakan id acak, sehingga provasi user tetap terjaga.
    - Kekurangannya adalah jika developernya tidak hati-hati, bisa terjadi kekeliruan dalam mengatur data yang disimpan session dan yang disimpan cookie. Sehingga menimbulkan risiko keamanan, kebocoran data, atau inkonsistensi status pengguna.
4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
    - Tidak sepenuhnya aman, karena secara default cookie tidak terenkripsi, lalu bisa diakses JavaScript dan dikirim ke server setiap request. Sehingga, terdapat risiko dicurinya cookie lewat jaringan ataupun manipulasi, dan bahkan CSRF.
    - Django menangani hal tersebut dengan hanya menyimpan session ID di cookie dan bukan data user langsung. Django mengaktifkan CSRF protection secara default. Selain itu, developer dapat mengatur sendiri pengamanan cookie yang diinginkan melalui fitur pengamanan yang disediakan oleh Django. 
5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step
    - Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna mengakses aplikasi sebelumnya sesuai dengan status login/logoutnya.
        - Untuk proses registrasi, saya mengimpor fungsi UserCreationForm dan messages. Setelah itu, saya membuat fungsi register dan membuat file register.html. Lalu, saya menambahkan routing kepada fungsi register pada urls.py.
        - Untuk proses login, saya membuat fungsi login_user pada views.py dan membuat file login.html. Setelahnya saya menambahkan routing kepada fungsi login pada urls.py. Saya juga menambahkan dekorator @login_required pada fungsi show_main dan show_news sehingga fungsi tsb hanya dapat diakses ketika user sudah login.
        - Untuk proses logout, saya membuat fungsi logout_user pada views.py dan menambahkan button Log Out pada main.html yang tersambung dengan fungsi logout_user pada views.py. Setelahnya saya menambahkan routing kepada fungsi logout pada urls.py.
    - Membuat dua (2) akun pengguna dengan masing-masing tiga (3) dummy data menggunakan model yang telah dibuat sebelumnya untuk setiap akun di lokal.
        - <img width="523" height="658" alt="Screenshot 2025-09-23 103431" src="https://github.com/user-attachments/assets/3fa2e533-aae8-4b1d-ac85-737948ad88e5" />
        - <img width="642" height="672" alt="Screenshot 2025-09-23 103535" src="https://github.com/user-attachments/assets/03838389-63fd-4cbd-8420-5a2bcbeb75c9" />
    - Menghubungkan model Product dengan User.
        - Saya menambahkan import user pada file models.py. Kemudian, saya menambahkan user = models.ForeignKey(User, on_delete=models.CASCADE, null=True) pada atribut class Product untuk membuat sebuah relationshop antara satu product dan satu user. Setelah itu saya membuat migration agar perubahan pada model tersimpan di database.
        - Saya juga menambahkan field user pada product yang akan dibuat user, yang nantinya akan berisi akun user yang sedang login saat pembuatan product berlangsung.
    - Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last_login pada halaman utama aplikasi.
        - Saya menambahkan variabel last_login yang berisikan cookie yang diambil dengan request.COOKIES.get('last_login', 'Never'). Setelah itu, saya menampilkan variabel tsb di file main.html. Sehingga, sekarang informasi kapan pengguna terakhir kali login dapat muncul di halaman depan web. Lalu, saya mengubah potongan kode di context main.html, di mana name dari user akan diambil dari user yang sedang login dengan menggunakan kode request.user.username.
        - Saya juga menambahkan kode untuk menghapus cookie last_login pada logout user supaya cookie last_login bisa dihapus dari daftar cookies di response.


# Tugas 3

1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
    - Supaya kita dapat mengirimkan data dari satu stack ke stack lainnya. Misalkan, seperti untuk mengirim data dari stack Frontend ke Backend, di sini JSON menjadi penghubung dari HTML (sebagai bahasa yang digunakan untuk Frontend) ke Django (sebagai bahasa yang digunakan untuk Backend) untuk mengirimkan data di antara dua stack berbed atersebut.

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
    - Menurut saya lebih baik JSON. Karena JSON lebih mudah ditulis daripada XML karena tidak memerlukan end tag. JSON juga lebih mudah dibaca karena syntaxnya relatif lebih pendek daripada XML.
    - Referensi: https://www.w3schools.com/js/js_json_xml.asp

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
    - Fungsi dari method is_valid() pada form Django adalah untuk memberikan validasi terhadap data dari input user yang dikirim melalui form. Method ini dibutuhkan untuk memastikan bahwa input yang diberikan user pada field yang ada sesuai dengan data type yang sudah ditentukan sebelumnya. Sehingga, bisa mencegah error yang terjadi karena data type tidak valid. Lalu, supaya bisa memberikan feedback kepada user semisal input yang diberikan user tidak sesuai.

4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
    - Kita membutuhkan csrf_token saat membuat form di Django untuk mencegah serangan berbahaya.
    - Jika kita tidak menambahkan csrf_token pada form Django, web kita akan lebih rentan terhadap serangan CSRF. Karena kita menggunakan POST request pada form, jika kita tidak menggunakan csrf_token, Django akan menolak request post dan memberikan error 403 (Forbidden). Karena default-nya, Django memberikan proteksi terhadap CSRF di request POST. Lalu, jika tidak ada csrf_token, browser tidak bisa melakukan validasi pada request yang masuk, karena bisa saja request yang masuk berasal dari penyerang dan bukan dari usernya sendiri.
    - Jika kita tidak menambahkan csrf_token pada form Django, penyerang dapat memberikan form palsu dan browser user dapat mengirimkannya seolah-olah request pengiriman dilakukan oleh user sendiri. Hal ini bisa berakibat pada terjadinya suatu aktivitas yang user sebetulnya tidak inginkan ataupun terkirimnya data-data privat user kepada penyerang.
    - Referensi: https://www.geeksforgeeks.org/python/csrf-token-in-django/

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    - Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.
        - Saya membuat fungsi bernama show_xml, show_xml_by_id, show_json, dan show_json_by_id. Untuk show_xml dan show_json akan menampilkan keseluruhan data product dalam format xml atau json. Sedangkan, untuk show_xml_by_id dan show_json_by_id akan menampilkan data satu product sesuai id pada url dalam format xml atau json.
    - Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 1. 
        - Saya menambahkan url pada urlpatterns di file urls.py yang akan meneruskan request yang diterima dari user ke function di views.py yang sesuai.
    - Membuat halaman yang menampilkan data objek model yang memiliki tombol "Add" yang akan redirect ke halaman form, serta tombol "Detail" pada setiap data objek model yang akan menampilkan halaman detail objek.
        - Saya membuat tombol add product serta detail pada file main.html. Nantinya di page tersebut akan ada dua tombol. 
        - Yang pertama + Add Product, di mana user akan diteruskan ke halaman form untuk menambahkan produk. Tombol ini tersambung dengan file (create_product.html). Yang kedua Detail, di mana user bisa melihat detail dari produk yang tadi sudah ditambahkan. Tombol ini tersambung dengan file (product_detail.html).
    - Membuat halaman form untuk menambahkan objek model pada app sebelumnya.
        - Halaman form akan terbuka jika user men-klik tombol add product di landing page. Atribut yang dimiliki oleh produk saya yang dapat dikustomisasi oleh user pada halaman form adalah nama, brand, price. description, thumbnail, category, is_featured, stock, gender, dan bonus_points.
    - Membuat halaman yang menampilkan detail dari setiap data objek model.
        - Saat user sudah submit form untuk add product, produk akan muncul di landing page beserta tombol detail. Jika tombol detail diklik, user dapat melihat detail dari produk tersebut. Atribut yang terlihat pada halaman detail produk adalah nama, kategori, keterangan featured, brand, thumbnail, deskripsi, stok, gender,dan bonus points.

6. Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
    - Tidak ada.

7. Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.
<img width="1920" height="1080" alt="Screenshot 2025-09-13 221056" src="https://github.com/user-attachments/assets/dfbb35e2-5387-407e-8cb8-f0364da927fe" />
<img width="1920" height="1080" alt="Screenshot 2025-09-13 221043" src="https://github.com/user-attachments/assets/f4321c37-e0f9-4f9a-9943-71c8b906c790" />
<img width="1920" height="1080" alt="Screenshot 2025-09-13 221000" src="https://github.com/user-attachments/assets/9548f148-003c-4910-9a68-d90480393dc5" />
<img width="1920" height="1080" alt="Screenshot 2025-09-13 220930" src="https://github.com/user-attachments/assets/b73fb5b3-e994-4478-a8e8-b462a1e45a92" />



# Tugas 2

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step
    - Membuat sebuah proyek Django baru
        - Saya membuat direktori bernama query-zone dan membuat serta mengaktifkan virtual environment dengan perintah (python -m venv env) lalu (env\Scripts\activate).
        - Setelahnya saya membuat fie requirements.txt yang nanti dependencies di dalamnya akan didownload menggunakan perintah (pip install -r requirements.txt). Salah satu dependency yang ada di dalamnya adalah django.
        - Setelah semuanya terinstall, saya membuat proyek django bernama query_zone dengan perintah (django-admin startproject query_zone .).
        - Saya mengubah isi dari file .env serta .env.prod untuk mengatur environment variables yang akan digunakan untuk development lokal serta production deployment.
        - Saya menambahkan fungsi (load_dotenv()) pada file settings.py supaya environment variable syang sudha diset sebelumnya bisa digunakan. Lalu saya mengubah bagian ALLOWED_HOSTS, PRODUCTION, dan DATABASES pada settings.py sesuai dengan kredensial yang saya miliki.
        - Setelah itu, saya melakukan proses migrasi dengan perintah (python manage.py migrate).
        - Setelah melakukan commit dan push ke git, saya mendeploy proyek django saya melalui pws.
    - Membuat aplikasi dengan nama main pada proyek tersebut.
        - Saya menggunakan perintah (python manage.py startapp main) pada terminal untuk membuat aplikasi main. Setelahnya saya mendaftarkan aplikasi main tersebut ke bagian INSTALLED_APPS yang berada pada settings.py di direktori proyek query_zone.
    - Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
        - Saya membuat file urls.py pada direktori aplikasi main dan menambahkan url pattern yang akan me-routing proyek django saya ke fungsi show_main ketika route yang dikunjungi masih root.
        - Setelahnya, saya membuka urls.py yang ada di direktori proyek query-zone. Saya mengimpor path dan include ke file tersebut dan mendaftarkan url pattern dari aplikasi main tadi ke level proyek.
        - Namun, karena pada saat ini show_main() masih belum dibuat, jadinya yang muncul saat sudah dideploy masih 404.
    - Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib.
        - Pada file models.py yang ada di direktori main, saya membuat class Product dan menambahkan atribut wajib sesuai ketentuan tugas.
    - Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
        - Saya membuat fungsi show_main() pada views.py yang berisikan nama, npm, serta kelas saya.
        - Pada template html bernama main.py, saya menuliskan headingnya menjadi Query Zone dan menuliskan kode html yang sesuai supaya bisa menampilkan kode yang sudah dituliskan di views.py.
    - Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
        - Tahap ini sudah dilakukan sekalian dengan proses routing sebelumnya.
    - Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
        - Saya melakukan proses migrasi kembali dengan makemigrations dan migrate karena terdapat model yang saya tambahkan.
        - Karena sebelumnya saya sudah melakukan proses deployment, ketika saya push perubahannya ke pws, maka sudah terlihat perubahan yang saya buat pada proyek saya.

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

<img width="839" height="559" alt="Screenshot 2025-09-10 090946" src="https://github.com/user-attachments/assets/dbd5ccf3-95f7-48d8-a885-e4a9082f8ba9" />

    - Ketika request client ke web aplikasi masuk, request tersebut akan diterima oleh urls. 
    - Request yang diterima oleh urls akan diteruskan ke views. Pada views, akan ditentukan fungsi apa yang tepat untuk request dari client. 
    - Setelah ditemukan fungsi yang tepat, views akan mengambil template berupa berkas html.
    - Views juga akan menuliskan konten dari berkas html dengan data yang dibaca dari models. 
    - Setelah selesai mengisi berkas html, views akan memberikan respons kepada client berupa berkas html yang sudah berisikan data yang sesuai request client.


4. Jelaskan peran settings.py dalam proyek Django!
    - settings.py adalah sebuah modul python dengan variabel berlevel module yang berisikan seluruh konfigurasi dari instalasi django. Contohnya, untuk mengonfigurasi host apa yang diperbolehkan untuk men-hosting proyek django, database yang digunakan, validasi password, dan lain-lain.
    - Referensi: https://docs.djangoproject.com/en/5.2/topics/settings/


5. Bagaimana cara kerja migrasi database di Django?
    - Migrasi database dimulai dengan perintah python manage.py makemigrations. Perintah makemigrations akan menciptakan berkas migrasi yang berisi perubahan model yang belum diaplikasikan ke dalam database. Setelah memiliki berkas migrasi yang berisi perubahan model, dilakukan migrasi ke dalam database lokal dengan menggunakan perintah python manage.py migrate. Perintah migrate akan mengaplikasikan perubahan model yang tercantum dalam berkas migrasi ke database dengan menjalankan perintah sebelumnya.

6. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
    - Alasan utamanya adalah karena Django merupakan framework yang open source sehingga bisa diakses dan dimodifikasi oleh umum tanpa harus membeli lisensi. Pengembangan web dengan django juga relatif mudah dan cepat karena frameworknya yang terorganisir dan sudah tersedia struktur yang siap pakai untuk aplikasi-aplikasi yang sudah umum. Proyek django juga memiliki skalabilitas yang baik karena dapat menerima ribuan permintaan tergantung dengan setting-up yang dilakukan pada hardware atau melalui proses caching.
    - Referensi: https://aws.amazon.com/id/what-is/django/

7. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
    - Tidak ada.
