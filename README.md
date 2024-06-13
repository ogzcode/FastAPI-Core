# FastAPI CRUD ve Authentication, Authorization Örneği

Bu proje, FastAPI kullanarak basit bir CRUD (Create, Read, Update, Delete),authentication (kimlik doğrulama), ve yetki doğrulama özelliklerini içerir.

## Kurulum ve Kullanım

1. Projeyi klonlayın:

    ```bash
    git clone https://github.com/ogzcode/FastAPI-Core.git
    ```

2. Proje dizinine gidin ve gerekli kütüphaneleri yükleyin:

    ```bash
    cd proje_adı
    pip install -r requirements.txt
    ```

3. Uygulamayı başlatın:

    ```bash
    uvicorn main:app --reload
    ```

4. Tarayıcınızda [http://localhost:8000/docs](http://localhost:8000/docs) adresine giderek API belgelerine erişebilirsiniz.


# Docker ile Çalıştırma
Bu projeyi Docker kullanarak çalıştırmak için aşağıdaki adımları izleyin:

1. Docker'ı bilgisayarınıza yükleyin ve çalıştırın.

2. Proje dizinine gidin:

    ```bash
    git clone https://github.com/ogzcode/FastAPI-Core.git
    cd /C:/Users/Windows 11/Desktop/FastAPI-Core/
    ```

3. Docker imajını oluşturun:

    ```bash
    docker build -t fastapi-core .
    ```

4. Docker konteynerını başlatın:

    ```bash
    docker run -p 8000:8000 fastapi-core
    ```

5. Tarayıcınızda [http://localhost:8000/docs](http://localhost:8000/docs) adresine giderek API belgelerine erişebilirsiniz.


## Authentication

- Kullanıcı kaydı yapmadan önce, `/auth/signup` endpoint'i kullanarak yeni bir kullanıcı kaydı oluşturun.
- Kayıtlı kullanıcılar, `/auth/login` endpoint'i kullanarak giriş yapabilirler ve bir erişim tokeni alabilirler.
- Elde edilen erişim tokeni, diğer işlemlerde kullanılabilir.

## CRUD İşlemleri

- `/users` endpoint'leri, öğelerle ilgili CRUD işlemlerini gerçekleştirir.
- Yeni öğe oluşturmak için `POST` isteği yapılırken, mevcut öğeleri listelemek için `GET` isteği yapılır.
- Belirli bir öğeyi güncellemek veya silmek için `PUT` veya `DELETE` isteği yapılırken, `item_id` parametresi ile öğenin kimliği belirtilmelidir.
