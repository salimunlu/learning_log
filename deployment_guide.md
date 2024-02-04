# Django Uygulamasını Heroku'ya Dağıtma Rehberi

Bu rehberde, bir Django uygulamasını Heroku'ya nasıl dağıtabileceğinizi adım adım anlatacağım. Lütfen adımları sırasıyla takip edin.

## Ön Koşullar

- Bir Heroku hesabınızın olması gerekmektedir.
- Bilgisayarınıza Git ve Heroku CLI yüklenmiş olmalıdır.
- Python geliştirme ortamınızın hazır olması gerekmektedir.

### 1. Heroku ve Git Yükleme

1. **Heroku Hesabı Açma:**
   - [Heroku'nun web sitesine](https://signup.heroku.com/) gidin ve bir hesap oluşturun.
   - Heroku hesabınızı aktifleştirmek için e-postanızı kontrol edin ve aktifleştirme adımlarını tamamlayın.

2. **Google Authenticator Kurulumu:**
   - Mobil cihazınıza Google Authenticator uygulamasını yükleyin.
   - Heroku hesabınız için iki faktörlü kimlik doğrulamayı etkinleştirdiğinizde bu uygulamayı kullanacaksınız.

3. **Kredi Kartı Bilgilerini Girme (Opsiyonel):**
   - Heroku, bazı eklentiler ve hizmetler için kredi kartı bilgilerinizi isteyebilir.

4. **Git Yükleme:**
   - [Git'in resmi web sitesine](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) gidin ve işletim sisteminize uygun Git sürümünü yükleyin.

5. **Heroku CLI Yükleme:**
   - [Heroku CLI'nin resmi web sitesine](https://devcenter.heroku.com/articles/heroku-cli) gidin ve işletim sisteminize uygun Heroku CLI sürümünü yükleyin.

### 2. Proje Ortamını Hazırlama

1. **Gerekli Paketleri Kurma:**
   ```
   pip install psycopg2
   pip install django-heroku
   pip install gunicorn
   ```

2. **`requirements.txt` Dosyası Oluşturma:**
   - Projenizin kök dizininde (manage.py dosyası ile aynı dizinde) terminal veya komut istemcisini açın.
   - Aşağıdaki komutu çalıştırarak `requirements.txt` dosyasını oluşturun:
     ```
     pip freeze > requirements.txt
     ```

3. **Python Versiyonunu Kaydetme:**
   - Python versiyonunuzu kontrol etmek için terminalde aşağıdaki komutu çalıştırın:
     ```
     python --version
     ```
   - Çıktıyı `runtime.txt` dosyasına yazın (Örneğin: `python-3.9.1`).

4. **Heroku Ayarlarını `settings.py`'a Ekleyin:**
   ```python
   # Heroku settings
   import django_heroku
   django_heroku.settings(locals())
   ```

5. **`Procfile` Dosyası Oluşturun:**
   - Projenizin kök dizininde (manage.py dosyası ile aynı dizinde) `Procfile` adında uzantısız bir dosya oluşturun.
   - Dosyaya aşağıdaki içeriği ekleyin (uygulamanızın adını doğru bir şekilde ayarladığınızdan emin olun):
     ```
     web: gunicorn your_project_name.wsgi --log-file -
     ```

### 3. Git Yapılandırması

1. **Git Kullanıcı Bilgilerini Ayarlayın:**
   ```
   git config --global user.name "your_username"
   git config --global user.email "your_email@example.com"
   ```

2. **`.gitignore` Dosyası Oluşturun:**
   - Projenizin kök dizinine `.gitignore` adında bir dosya oluşturun ve içine aşağıdakileri ekleyin:
     ```
     .venv/
     __pycache__/
     *.sqlite3
     ```

3. **Projeyi Commit Edin:**
   ```
   git init
   git add .
   git commit -am "Ready for deployment to heroku."
   ```

### 4. Projeyi Heroku'ya Yükleme

1. **Heroku'ya Giriş Yapın:**
   ```
   heroku login
   ```
   - Komutu çalıştırdıktan sonra herhangi bir tuşa basın ve web tarayıcınızda açılan Heroku giriş sayfasından giriş yapın.

2. **Heroku Uygulaması Oluşturun:**
   ```
   heroku create
   ```

3. **Projeyi Heroku'ya Push Edin:**
   ```
   git push heroku master
   ```

### 5. Veritabanı Yapılandırması

#### SQLite3 (Varsayılan Yerel Veritabanı)
- Django projeleri, varsayılan olarak hafif ve kullanımı kolay bir veritabanı sistemi olan SQLite3 ile gelir. Projenizde herhangi bir değişiklik yapmanıza gerek yoktur; yerel geliştirme ve test için SQLite3 kullanmaya devam edebilirsiniz.

#### Opsiyonel: Heroku Postgres Kullanımı
Eğer uygulamanızın Heroku'da PostgreSQL veritabanı kullanmasını istiyorsanız, aşağıdaki adımları takip edin. Unutmayın ki, Heroku üzerindeki veritabanı kullanımı ek ücrete tabi olabilir.

1. **Heroku Postgres Eklentisini Ekleyin:**
   Heroku'da PostgreSQL veritabanı eklemek için aşağıdaki komutu kullanın:
   ```
   heroku addons:create heroku-postgresql:hobby-dev
   ```

2. **Veritabanı Migrasyonlarını Çalıştırın:**
   Veritabanı şemasını Heroku Postgres'e uygulamak için aşağıdaki komutu çalıştırın:
   ```
   heroku run python manage.py migrate
   ```
   Bu komut, Django uygulamanızın veritabanı şemasını Heroku Postgres veritabanınıza uygular.

#### Notlar:
- Eğer SQLite3 kullanmaya devam ederseniz, `.gitignore` dosyanızda `.sqlite3` dosyalarını göz ardı ettiğinizden emin olun.
- PostgreSQL kullanıyorsanız, projenizin `settings.py` dosyasında `DATABASES` ayarını Heroku'nun veritabanı URL'sini kullanacak şekilde güncellemeniz gerekebilir.


### 6. Uygulamayı Yeniden Adlandırma (Opsiyonel)

- Uygulamanızı yeniden adlandırmak isterseniz, aşağıdaki komutu kullanabilirsiniz:
  ```
  heroku apps:rename newname
  ```

### 7. Heroku Üzerinde Superuser Oluşturma

- Uygulamanız için bir superuser oluşturmak için aşağıdaki komutu kullanın:
  ```
  heroku run python manage.py createsuperuser
  ```

---
