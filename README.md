# FastAPI CRUD ve Authentication, Authorization Örneği

Bu proje, FastAPI kullanarak basit bir CRUD (Create, Read, Update, Delete),authentication (kimlik doğrulama), ve yetki doğrulama özelliklerini içerir.

## Kurulum ve Kullanım

1. Projeyi klonlayın:

    ```bash
    git clone https://github.com/kullanici/adı.git
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

## API Endpointleri

- **POST /users/createUser:** Yeni bir kullanıcı kaydı oluşturur.
- **POST /users/login:** Kullanıcı girişi yapar ve bir erişim tokeni döndürür.
- **GET /users/getUserById:** Mevcut kullanıcı bilgilerini döndürür(Admin erişebilir).
- **PUT /users/updateUser:** Mevcut kullanıcı bilgilerini günceller.
- **DELETE /users/deleteUserById:** Mevcut kullanıcıyı siler.
- **GET /users/getUsers:** Tüm kullanıcıları listeler.
- **DELETE /users/deleteAllUsers:** Tüm kullanıcıları siler.

## Authentication

- Kullanıcı kaydı yapmadan önce, `/users/createUser` endpoint'i kullanarak yeni bir kullanıcı kaydı oluşturun.
- Kayıtlı kullanıcılar, `/users/login` endpoint'i kullanarak giriş yapabilirler ve bir erişim tokeni alabilirler.
- Elde edilen erişim tokeni, diğer işlemlerde kullanılabilir.

## CRUD İşlemleri

- `/users` endpoint'leri, öğelerle ilgili CRUD işlemlerini gerçekleştirir.
- Yeni öğe oluşturmak için `POST` isteği yapılırken, mevcut öğeleri listelemek için `GET` isteği yapılır.
- Belirli bir öğeyi güncellemek veya silmek için `PUT` veya `DELETE` isteği yapılırken, `item_id` parametresi ile öğenin kimliği belirtilmelidir.
