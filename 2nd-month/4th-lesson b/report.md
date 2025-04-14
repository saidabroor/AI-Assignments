Bu model twitter foydalanuvchilarining **depressiyaga tushgan yoki tushmaganiligini bashorat qilish** uchun tayyorlandi.

Dataset **11** ustun va **20 000** qatordan iborat. Target class **label** deb olindi va binary classdan iborat.

Data preprocessing qismida **standard scalerdan** foylanildi chunki dataset outlierdan iborat emas, normally distributed edi.

**Mutual classification** ishlatildi va qaysi ustunlar target classga qanchalik contribute qilishi aniqlandi. Contribution nolga teng bo'lgan va model ta'siri bo'lmagan, id, unnamed va post_id ustunlari tashlab yuborildi.

Model uchun **RandomForestClassifierdan** foylanaildi. Chunki u voting system ishlaydi va ensemble model oilasiga kiradi va aniqlikni yuqori darajada hisoblaydi.

**Classification report** metric ishlatildi chunki model classification model edi.

Natija ikki xil holatda ko'rildi. F**eature engineering, feature transforming qilinmasdan** va natija 0.92, 0.95 va 0.89 ni ko'rsatdi, precision, recall va f1-score holatida.

Huddi shu metriclar, **Feature engineering va feature transformingni** bir necha bosqichlaridan keyin, 1.00, 1.00, 1.00 natilarini ko'rsatdi.

Kaggledan huddi shu dataset uchun qilingan modellar qismida yangilik bo'lganlardan import re va import torch bo'ldi.

Model training qismida ham x, y shaklida variable kiritmasdan quyidagi ko'rinishda dataset bo'lingan:

X_train, X_test, y_train, y_test = train_test_split(
df['processed_text'], df['label'], test_size=0.2, random_state=42
)

Ya'ni train_test_split(x,y, test_size = 0.2) emas, balki
train_test_split(x['processed_text'], df['label]) ko'rinishida.
