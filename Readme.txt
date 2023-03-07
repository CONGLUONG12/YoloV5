Step 1: Run "docker build -t detect ."
Step 2: Run "docker run detect"
	Sau khi run câu lệnh này, ta sẽ nhận được 1 urls là: http://172.17.0.2:5000
	Mở url này trong postman và post vào json có dạng:
{
    "urls": "https://cdn.dailyxe.com.vn/image/autodaily-street-shots-p8-rolls-royce-cullinan-mau-doc-quay-lai-ha-noi-190519j.jpg, https://live.staticflickr.com/65535/49932658111_30214a4229_b.jpg,https://i.imgur.com/y2SGZym_lq.mp4, https://i.imgur.com/aDsCFlS.mp4"
}
Trong đó các ảnh và video được ngăn cách bởi dấu ","

==> Ta sẽ nhận được 1 dictionary với key là url và value là Safe hoặc Unsafe
