(https://khansa-dinda-queryzone.pbp.cs.ui.ac.id/)

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step
    a. Membuat sebuah proyek Django baru
        - Saya membuat direktori bernama query-zone dan membuat serta mengaktifkan virtual environment dengan perintah (python -m venv env) lalu (env\Scripts\activate).
        - Setelahnya saya membuat fie requirements.txt yang nanti dependencies di dalamnya akan didownload menggunakan perintah (pip install -r requirements.txt). Salah satu dependency yang ada di dalamnya adalah django.
        - Setelah semuanya terinstall, saya membuat proyek django bernama query_zone dengan perintah (django-admin startproject query_zone .).
        - Saya mengubah isi dari file .env serta .env.prod untuk mengatur environment variables yang akan digunakan untuk development lokal serta production deployment.
        - Saya menambahkan fungsi (load_dotenv()) pada file settings.py supaya environment variable syang sudha diset sebelumnya bisa digunakan. Lalu saya mengubah bagian ALLOWED_HOSTS, PRODUCTION, dan DATABASES pada settings.py sesuai dengan kredensial yang saya miliki.
        - Setelah itu, saya melakukan proses migrasi dengan perintah (python manage.py migrate).
        - Setelah melakukan commit dan push ke git, saya mendeploy proyek django saya melalui pws.
    b. Membuat aplikasi dengan nama main pada proyek tersebut.
        - Saya menggunakan perintah (python manage.py startapp main) pada terminal untuk membuat aplikasi main. Setelahnya saya mendaftarkan aplikasi main tersebut ke bagian INSTALLED_APPS yang berada pada settings.py di direktori proyek query_zone.
    c. Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
        - Saya membuat file urls.py pada direktori aplikasi main dan menambahkan url pattern yang akan me-routing proyek django saya ke fungsi show_main ketika route yang dikunjungi masih root.
        - Setelahnya, saya membuka urls.py yang ada di direktori proyek query-zone. Saya mengimpor path dan include ke file tersebut dan mendaftarkan url pattern dari aplikasi main tadi ke level proyek.
        - Namun, karena pada saat ini show_main() masih belum dibuat, jadinya yang muncul saat sudah dideploy masih 404.
    d. Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib.
        - Pada file models.py yang ada di direktori main, saya membuat class Product dan menambahkan atribut wajib sesuai ketentuan tugas.
    e. Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
        - Saya membuat fungsi show_main() pada views.py yang berisikan nama, npm, serta kelas saya.
        - Pada template html bernama main.py, saya menuliskan headingnya menjadi Query Zone dan menuliskan kode html yang sesuai supaya bisa menampilkan kode yang sudah dituliskan di views.py.
    f. Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
        - Tahap ini sudah dilakukan sekalian dengan proses routing sebelumnya.
    g. Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
        - Saya melakukan proses migrasi kembali dengan makemigrations dan migrate karena terdapat model yang saya tambahkan.
        - Karena sebelumnya saya sudah melakukan proses deployment, ketika saya push perubahannya ke pws, maka sudah terlihat perubahan yang saya buat pada proyek saya.

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
    a. Ketika request client ke web aplikasi masuk, request tersebut akan diterima oleh urls. 
    b. Request yang diterima oleh urls akan diteruskan ke views. Pada views, akan ditentukan fungsi apa yang tepat untuk request dari client. 
    c. Setelah ditemukan fungsi yang tepat, views akan mengambil template berupa berkas html.
    d. Views juga akan menuliskan konten dari berkas html dengan data yang dibaca dari models. 
    e. Setelah selesai mengisi berkas html, views akan memberikan respons kepada client berupa berkas html yang sudah berisikan data yang sesuai request client.
 
3. Jelaskan peran settings.py dalam proyek Django!
    - settings.py adalah sebuah modul python dengan variabel berlevel module yang berisikan seluruh konfigurasi dari instalasi django. Contohnya, untuk mengonfigurasi host apa yang diperbolehkan untuk men-hosting proyek django, database yang digunakan, validasi password, dan lain-lain.
    - Referensi: https://docs.djangoproject.com/en/5.2/topics/settings/

4. Bagaimana cara kerja migrasi database di Django?
    - Migrasi database dimulai dengan perintah python manage.py makemigrations. Perintah makemigrations akan menciptakan berkas migrasi yang berisi perubahan model yang belum diaplikasikan ke dalam database. Setelah memiliki berkas migrasi yang berisi perubahan model, dilakukan migrasi ke dalam database lokal dengan menggunakan perintah python manage.py migrate. Perintah migrate akan mengaplikasikan perubahan model yang tercantum dalam berkas migrasi ke database dengan menjalankan perintah sebelumnya.

5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
    - Alasan utamanya adalah karena Django merupakan framework yang open source sehingga bisa diakses dan dimodifikasi oleh umum tanpa harus membeli lisensi. Pengembangan web dengan django juga relatif mudah dan cepat karena frameworknya yang terorganisir dan sudah tersedia struktur yang siap pakai untuk aplikasi-aplikasi yang sudah umum. Proyek django juga memiliki skalabilitas yang baik karena dapat menerima ribuan permintaan tergantung dengan setting-up yang dilakukan pada hardware atau melalui proses caching.
    - Referensi: https://aws.amazon.com/id/what-is/django/

6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
    - Tidak ada.