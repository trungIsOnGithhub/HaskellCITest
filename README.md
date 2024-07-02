##### Học Kì 2, năm học 2023 - 2024
##### Trường Đại Học Bách Khoa - ĐHQG TPHCM

##### Dùng Github Action hỗ trợ chấm điểm môn học Lập Trình Nâng Cao - HCMUT

> Giảng viên: Ms Lê Đình Thuận
> Sinh viên: Nguyễn Việt Trung

### Sơ lược các thành phần
![kiến trúc](/assets/arch.png "Kiến Trúc")
- Môi trường chạy trên Docker container được tạo ra từ image xây dựng sẵn và phân phối qua Docker Hub
- Github Action giúp tạo môi trường chạy cho container và sao chép mã nguồn bài làm để thực hiện chạy trên Docker container
- Chương trình Python tạo các yêu cầu HTTP để thu thập tài nguyên và chạy các đoạn mã bài tập
