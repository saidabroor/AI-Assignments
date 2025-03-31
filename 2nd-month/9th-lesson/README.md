**Loyiha Hisoboti: Uy Narxini Bashorat Qilish**

**1. Kirish**

Ushbu loyiha uy narxlarini bashorat qilish uchun regressiya modellaridan foydalanish orqali uy bozori tendensiyalarini o'rganishga qaratilgan. 1000 ta qatordan iborat bo'lgan ma'lumotlar to'plami quyidagi 8 ta xususiyatni o'z ichiga oladi: maydon (Square_Footage), yotoqxonalar soni (Num_Bedrooms), hammomlar soni (Num_Bathrooms), qurilish yili (Year_Built), yer maydoni (Lot_Size), garaj hajmi (Garage_Size), mahalla sifati (Neighborhood_Quality) va uy narxi (House_Price).

**2. Data preprocessing**

**Missing values**
Tushib qolgan qiymatlar yo'q va dataset numerical datadan iborat.

**Scaling**: Ma'lumotlar ijobiy og'ma (positively skewed) bo'lganligi sababli, **Robust Scaling** usuli qo'llanildi.

**Training va test to'plami**: Ma'lumotlar training va test uchun bo'lindi hamda house_price - target qiymat.

**3. Model tanlash va optimizatsiya**
Quyidagi uchta regressiya modeli ishlatildi:

- **DecisionTreeRegressor**
- **RandomForestRegressor**
- **LGBMRegressor**

Har bir model **GridSearchCV** yordamida quyidagi giperparametrlarga asoslangan holda optimallashtirildi:

- `max_depth`: [None, 10, 20, 30, 40, 50]
- `min_samples_split`: [2, 4, 10]
- `min_samples_leaf`: [1, 2, 4]
- `max_features`: [None, 'sqrt', 'log2']

Model baholash **Mean Squared Error (MSE)** va **R-squared (R²)** ko'rsatkichlari bo'yicha amalga oshirildi.

**4. Natijalar**

---

| Model                 | MSE      | R²       |
| --------------------- | -------- | -------- |
| DecisionTreeRegressor | 0.004862 | 0.985964 |
| RandomForestRegressor | 0.002019 | 0.994171 |
| LGBMRegressor         | 0.001316 | 0.996200 |

---

- **LGBMRegressor** modeli eng yuqori aniqlikni ko'rsatdi (**R² = 0.9962**).
- **RandomForestRegressor** 2-yaxshi natijani ko'rsatdi (**R² = 0.9942**).
- **DecisionTreeRegressor** nisbatan pastroq natija berdi (**R² = 0.9859**), lekin baribir yuqori aniqlikga ega.

**5. Xulosa**

- **Modelni yanada yaxshilash**: Modelning umumiy ishlashini oshirish uchun **ensembling** usullari, masalan, Stacking qo'llanilishi mumkin.
- **Ma'lumotlar boyitilishi**: Qo'shimcha xususiyatlar yaratish va mavjud ma'lumotlarni kengaytirish modelning aniqligini oshirishi mumkin.

Ushbu loyiha natijalari shuni ko'rsatadiki, uy narxlarini bashorat qilishda **LGBMRegressor** eng yaxshi model hisoblanadi.
