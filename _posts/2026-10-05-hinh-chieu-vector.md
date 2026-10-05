---
layout: post
title: "Hình chiếu vô hướng và hình chiếu vector: giải từng bước"
date: 2026-10-05
categories: [toan, dai-so-tuyen-tinh]
tags: [vector, dot-product, projection]
mathjax: true
---

Bài này giải hai câu hỏi về **phép chiếu vector**: hình chiếu vô hướng (scalar projection) và hình chiếu vector (vector projection). Hai câu dùng chung một cặp vector. Mỗi bước đều có giải thích "tại sao", không chỉ có công thức.

## Đề bài

Cho hai vector trong không gian 3 chiều:

$$
\mathbf{r} = \begin{bmatrix} 3 \\ -4 \\ 0 \end{bmatrix}, \qquad
\mathbf{s} = \begin{bmatrix} 10 \\ 5 \\ -6 \end{bmatrix}
$$

- **Câu 1:** Tìm hình chiếu **vô hướng** của $$\mathbf{s}$$ lên $$\mathbf{r}$$.
- **Câu 2:** Tìm hình chiếu **vector** của $$\mathbf{s}$$ lên $$\mathbf{r}$$.

---

## Hình chiếu là gì?

Đặt $$\mathbf{s}$$ và $$\mathbf{r}$$ chung gốc. Từ đầu mũi tên $$\mathbf{s}$$, kẻ một đường **vuông góc** xuống đường thẳng chứa $$\mathbf{r}$$. Đoạn từ gốc đến chân đường vuông góc chính là **hình chiếu**.

```
              s ↗
               /|
              / |  ← đường vuông góc
             /  |
            / θ |
     gốc   ●====▶──────────────▶ r
           └hình┘
            chiếu
```

Hình dung: rọi đèn thẳng từ trên xuống, **bóng** của $$\mathbf{s}$$ in trên $$\mathbf{r}$$ là hình chiếu.

| Loại | Nghĩa | Kết quả |
|---|---|---|
| Hình chiếu **vô hướng** | Bóng **dài bao nhiêu** | Một con số |
| Hình chiếu **vector** | Bóng **là mũi tên nào** (độ dài + hướng) | Một vector |

Ví dụ đời thường: "đi 2 km" là vô hướng, còn "đi 2 km về phía đông nam" là vector.

---

## Công thức và cách suy ra

### Bước A: Dùng cos trong tam giác vuông

$$\mathbf{s}$$, đường vuông góc và hình chiếu tạo thành tam giác vuông, trong đó $$\mathbf{s}$$ là cạnh huyền và hình chiếu là cạnh kề góc $$\theta$$:

$$
\cos\theta = \frac{\text{cạnh kề}}{\text{cạnh huyền}} = \frac{\text{hình chiếu}}{\lvert \mathbf{s}\rvert }
\quad\Longrightarrow\quad
\text{hình chiếu} = \lvert \mathbf{s}\rvert \cos\theta
$$

Vấn đề: đề **không cho góc** $$\theta$$, chỉ cho tọa độ.

### Bước B: Khử θ bằng tích vô hướng

Tích vô hướng $$\mathbf{r}\cdot\mathbf{s}$$ là **một con số** và có hai cách tính, luôn ra cùng kết quả:

- **Theo tọa độ:** $$\mathbf{r}\cdot\mathbf{s} = r_1s_1 + r_2s_2 + r_3s_3$$
- **Theo góc:** $$\mathbf{r}\cdot\mathbf{s} = \lvert \mathbf{r}\rvert \,\lvert \mathbf{s}\rvert \cos\theta$$

> **Vì sao hai cách bằng nhau?** Nối hai đầu mũi tên lại, ta được cạnh thứ ba là $$\mathbf{r}-\mathbf{s}$$. Tính $$\lvert \mathbf{r}-\mathbf{s}\rvert ^2$$ theo hai cách:
>
> - Định lý cos: $$\lvert \mathbf{r}-\mathbf{s}\rvert ^2 = \lvert \mathbf{r}\rvert ^2 + \lvert \mathbf{s}\rvert ^2 - 2\lvert \mathbf{r}\rvert \lvert \mathbf{s}\rvert \cos\theta$$
> - Tọa độ (2D cho gọn): $$(r_1-s_1)^2 + (r_2-s_2)^2 = \lvert \mathbf{r}\rvert ^2 + \lvert \mathbf{s}\rvert ^2 - 2(r_1s_1 + r_2s_2)$$
>
> Gạch phần giống nhau $$\lvert \mathbf{r}\rvert ^2 + \lvert \mathbf{s}\rvert ^2$$, chia hai vế cho $$-2$$, ta được $$\lvert \mathbf{r}\rvert \lvert \mathbf{s}\rvert \cos\theta = r_1s_1 + r_2s_2$$.

Chia hai vế của $$\mathbf{r}\cdot\mathbf{s} = \lvert \mathbf{r}\rvert \lvert \mathbf{s}\rvert \cos\theta$$ cho $$\lvert \mathbf{r}\rvert $$:

$$
\boxed{\text{Hình chiếu vô hướng} = \lvert \mathbf{s}\rvert \cos\theta = \frac{\mathbf{r}\cdot\mathbf{s}}{\lvert \mathbf{r}\rvert }}
$$

Vế phải tính được **hoàn toàn bằng tọa độ**, không cần biết góc.

---

## Câu 1: Hình chiếu vô hướng

**Đề bài:** Cho $$\mathbf{r} = \begin{bmatrix} 3 \\ -4 \\ 0 \end{bmatrix}$$ và $$\mathbf{s} = \begin{bmatrix} 10 \\ 5 \\ -6 \end{bmatrix}$$. Tìm hình chiếu **vô hướng** của $$\mathbf{s}$$ lên $$\mathbf{r}$$.

### Bước 1: Tính tích vô hướng

Nhân từng cặp thành phần tương ứng rồi cộng lại:

$$
\mathbf{r}\cdot\mathbf{s} = (3)(10) + (-4)(5) + (0)(-6) = 30 - 20 + 0 = 10
$$

### Bước 2: Tính độ dài của r

Độ dài vector là Pytago mở rộng: bình phương từng thành phần, cộng lại, rồi lấy căn.

$$
\lvert \mathbf{r}\rvert  = \sqrt{3^2 + (-4)^2 + 0^2} = \sqrt{9 + 16 + 0} = \sqrt{25} = 5
$$

Lưu ý $$(-4)^2 = 16$$ (dương), nên độ dài không bao giờ âm.

### Bước 3: Chia

$$
\frac{\mathbf{r}\cdot\mathbf{s}}{\lvert \mathbf{r}\rvert } = \frac{10}{5} = 2
$$

### Bước 4: Kiểm tra dấu

$$\mathbf{r}\cdot\mathbf{s} = 10 > 0$$, nghĩa là góc giữa hai vector nhọn, nên kết quả **dương** là hợp lý. Nếu góc lớn hơn $$90^\circ$$ thì $$\cos\theta < 0$$ và hình chiếu tự động mang dấu âm.

### ✅ Đáp án: **2**

**Bẫy thường gặp:**

- $$\tfrac{1}{2}$$: chia ngược ($$5/10$$), hoặc chia cho $$\vert\mathbf{s}\vert$$ thay vì $$\vert\mathbf{r}\vert$$. Chiếu **lên r** thì phải chia cho **độ dài của r**.
- $$-2$$, $$-\tfrac{1}{2}$$: sai dấu.

---

## Câu 2: Hình chiếu vector

**Đề bài:** Với cùng hai vector $$\mathbf{r} = \begin{bmatrix} 3 \\ -4 \\ 0 \end{bmatrix}$$ và $$\mathbf{s} = \begin{bmatrix} 10 \\ 5 \\ -6 \end{bmatrix}$$, tìm hình chiếu **vector** của $$\mathbf{s}$$ lên $$\mathbf{r}$$.

Mũi tên hình chiếu nằm **trên đường của r**, nên:

> **Hình chiếu vector = (độ dài đã tính ở Câu 1) × (hướng của r)**

### Bước 1: Lấy hướng của r (vector đơn vị)

Nhân hoặc chia một vector với một số dương **chỉ đổi độ dài, không đổi hướng**. Vì vậy chia $$\mathbf{r}$$ cho chính độ dài của nó (bằng 5) sẽ được mũi tên **cùng hướng nhưng dài đúng 1**:

$$
\hat{\mathbf{r}} = \frac{\mathbf{r}}{\lvert \mathbf{r}\rvert } = \frac{1}{5}\begin{bmatrix} 3 \\ -4 \\ 0 \end{bmatrix} = \begin{bmatrix} 3/5 \\ -4/5 \\ 0 \end{bmatrix}
$$

Kiểm tra: $$\sqrt{(3/5)^2 + (-4/5)^2} = \sqrt{9/25 + 16/25} = 1$$ ✓

Vector $$\hat{\mathbf{r}}$$ (đọc là "r mũ") giống một chiếc **la bàn**: chỉ cho biết hướng, độ dài luôn bằng 1.

### Bước 2: Kéo dài thành độ dài cần có

Nhân với độ dài hình chiếu (bằng 2):

$$
2 \cdot \hat{\mathbf{r}} = 2 \begin{bmatrix} 3/5 \\ -4/5 \\ 0 \end{bmatrix} = \begin{bmatrix} 6/5 \\ -8/5 \\ 0 \end{bmatrix}
$$

### Công thức gộp

$$
\text{Hình chiếu vector}
= \underbrace{\frac{\mathbf{r}\cdot\mathbf{s}}{\lvert \mathbf{r}\rvert }}_{\text{độ dài}}
\cdot
\underbrace{\frac{\mathbf{r}}{\lvert \mathbf{r}\rvert }}_{\text{hướng}}
= \frac{\mathbf{r}\cdot\mathbf{s}}{\lvert \mathbf{r}\rvert ^2}\,\mathbf{r}
= \frac{10}{25}\begin{bmatrix} 3 \\ -4 \\ 0 \end{bmatrix}
$$

Chú ý mẫu số là $$\vert\mathbf{r}\vert^2$$, vì $$\vert\mathbf{r}\vert$$ xuất hiện hai lần.

### Kiểm tra

Độ dài của đáp án: $$\sqrt{(6/5)^2 + (8/5)^2} = \sqrt{100/25} = 2$$, khớp với Câu 1 ✓

### ✅ Đáp án: $$\begin{bmatrix} 6/5 \\ -8/5 \\ 0 \end{bmatrix}$$

**Bẫy thường gặp:**

| Đáp án sai | Lỗi |
|---|---|
| (6, −8, 0) | Nhân thẳng 2 × r, quên đưa r về độ dài 1. Vì r dài 5 nên kết quả dài 10 chứ không phải 2. |
| (30, −20, 0) | Nhân từng cặp thành phần nhưng quên cộng lại. |
| (6, 4, 0) | Sai dấu, hướng không còn cùng phương với r. |

---

## Bonus: Khi r và s vuông góc

Nếu $$\mathbf{r} \perp \mathbf{s}$$ thì $$\theta = 90^\circ$$ và $$\cos 90^\circ = 0$$, nên:

$$
\mathbf{r}\cdot\mathbf{s} = 0 \quad\Longrightarrow\quad \text{hình chiếu} = \frac{0}{\lvert \mathbf{r}\rvert } = 0
$$

Bóng của $$\mathbf{s}$$ co lại chỉ còn **một điểm**.

Ngược lại, khi $$\mathbf{s}$$ **song song** cùng chiều với $$\mathbf{r}$$ ($$\theta = 0^\circ$$), hình chiếu bằng đúng $$\vert\mathbf{s}\vert$$: $$\mathbf{s}$$ "chiếu trọn vẹn" lên $$\mathbf{r}$$.

---

## Tóm tắt

| | Công thức | Kết quả ví dụ |
|---|---|---|
| Hình chiếu vô hướng | (r · s) / độ dài r | 2 |
| Hình chiếu vector | (r · s) / (độ dài r)² × r | (6/5, −8/5, 0) |

**Mẹo nhớ:**

- Vuông góc thì tích vô hướng bằng 0, nên hình chiếu bằng 0.
- Chiếu **lên** vector nào thì chia cho độ dài **của vector đó**.
- Hình chiếu vector = độ dài × vector đơn vị (chia cho độ dài **hai lần**).
