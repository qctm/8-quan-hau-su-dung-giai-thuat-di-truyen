=========================
Nguyễn Quốc Trầm B1913276
=========================

Đề tài:
Bài toán 8 quân hậu (N-Queen) sử dụng giải thuật di truyền

__Mục đích:
Đặt 8 (N) quân hậu trên 1 bàn cờ NxN sao cho không quân hậu
nào đụng độ với các quân còn lại.

__Thuật ngữ:
1. Gen (Gene): Một cá nhân được đặc trưng bởi một tập hợp các biến

2. Nhiễm sắc thể (Chromosome): Các gen liên kết thành một chuỗi để tạo
thành một Nhiễm sắc thể (dung dịch).
Nhiễm sắc thể là một tập hợp các tham số xác định một giải pháp
được đề xuất cho vấn đề mà thuật toán di truyền đang cố gắng giải quyết

3. Dân số (Population): Tập hợp tất cả các giải pháp

4. Hàm đánh giá độ tốt (Fitness Function): số lượng quân hậu không đụng độ
Giá trị lớn nhất,max = (n(n-1)/2).
(giả sử N = 6, Fmax = 6C2 = 6 * 5/2 = 15)

5. Lai chéo (Crossover): Còn được gọi là tái tổ hợp, là một toán tử di truyền
được sử dụngđể kết hợp thông tin di truyền của hai bố mẹ
để tạo ra con cái mới

6. Đột biến (Mutation): Nó làm thay đổi một hoặc nhiều giá trị gen
trong nhiễm sắc thể so với trạng thái ban đầu

__Cách giải thuật hoạt động:
Bước 1: Một nhiễm sắc thể ngẫu nhiên được tạo ra
Bước 2: Tính Fitness value của nhiễm sắc thể
Bước 3: Nếu fitness value không bằng Fmax
Bước 4: Tái tạo (Crossover) nhiễm sắc thể mới
        từ 2 nhiễm sắc thể tốt nhất được chọn ngẫu nhiên
Bước 5: Có thể xảy ra đột biến
Bước 6: Nhiễm sắc thể mới được thêm vào quần thể
        Lặp lại bước 2 đến bước 6 cho đến khi
        tìm thấy nhiễm sắc thể (giải pháp)
        có giá trị Fitness value = Fmax
