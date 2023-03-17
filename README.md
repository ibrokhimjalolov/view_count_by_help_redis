# View Count By Help Redis


## View count: ko'rishlar soni
Asosiy g'oya user X-object'ni ko'rganligi haqida vaqtincha redis(cache) da saqlanadi va expire limit qoyiladi.
Endi user X-object single'ni retrieve qilganda, tekshirib view_count ni bitaga oshirib qoyishimiz mumkin.
Request ni uniqligini aniqlashda bizga Frontend'ni yordami kerak boladi, ular bizga headerda fingerprint(https://fingerprint.com/demo/) yuborishadi.


!!! Expire qoyganda key avtomatik ochib ketadi, qolda ochirish shart emas.

## Implementation (RestFramework ishlatyapmiz deb faraz qilamiz))
1. ViewCountMixin (post.view_mixins.ViewCountMixin) class yaratamiz. Dublikat qilmaslik uchun va hamma logika shu klass orqali qilinadi.
2. Va shu ViewCountMixin ni Generic RetrieveAPIView klassiga mixin qilib qo'ysak kifoya, Ozi avtomatik view sanay boshlaydi.