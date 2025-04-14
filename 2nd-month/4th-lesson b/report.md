Bu model twitter foydalanuvchilarining **depressiyaga tushgan yoki tushmaganiligini bashorat qilish** uchun tayyorlandi.

Dataset **11** ustun va **20 000** qatordan iborat. Target class **label** deb olindi va binary classdan iborat.

Data preprocessing qismida **standard scalerdan** foylanildi chunki dataset outlierdan iborat emas, normally distributed edi.

**Mutual classification** ishlatildi va qaysi ustunlar target classga qanchalik contribute qilishi aniqlandi. Contribution nolga teng bo'lgan va model ta'siri bo'lmagan, id, unnamed va post_id ustunlari tashlab yuborildi.

Model uchun **RandomForestClassifierdan** foylanaildi. Chunki u voting system ishlaydi va ensemble model oilasiga kiradi va aniqlikni yuqori darajada hisoblaydi.

**Classification report** metric ishlatildi chunki model classification model edi.

Natija ikki xil holatda ko'rildi. F**eature engineering, feature transforming qilinmasdan** va natija 0.92, 0.95 va 0.89 ni ko'rsatdi, precision, recall va f1-score holatida.

Huddi shu metriclar, **Feature engineering va feature transformingni** bir necha bosqichlaridan keyin, 1.00, 1.00, 1.00 natilarini ko'rsatdi.
