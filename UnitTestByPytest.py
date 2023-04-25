import requests
import pytest

@pytest.fixture
def find_video_api_url():
    return "https://www.chiangmaiarea1.go.th/myapp/public/index.php/admin/api/FindVideo"

@pytest.fixture
def get_other_api_url():
    return "https://www.chiangmaiarea1.go.th/myapp/public/index.php/admin/api/getOther"

def test_get_find_video(find_video_api_url):
    """
    Test that the FindVideo API endpoint returns the expected data.
    """

    expected_data = [
        {
            "id": 1,
            "url": "https://www.youtube.com/watch?v=UNeJYRU16Mo&t=64s"
        },  
    ]

    response = requests.get(find_video_api_url)

    assert response.status_code == 200 # status ที่ได้รับมาถูกต้องไหม
    assert isinstance(response.json(), list)
    assert len(response.json()) >= len(expected_data) # ตรวจสอบว่าค่า response ไม่่ต่ำกว่า ค่าจาก expected_data

def test_get_other(get_other_api_url):
    """
    Test that the getOther API endpoint returns the expected data.
    """

    expected_data = [
  {
    "id": 1,
    "array": [
      "สำนักงานเขตพื้นที่การศึกษาประถมศึกษาเชียงใหม่ เขต 1 อาคารอำนวยการกลาง ชั้น 4 ศาลากลางจังหวัดเชียงใหม่ อำเภอเมืองเชียงใหม่ จังหวัดเชียงใหม่ 50300",
      "ติดต่อเราได้ที่ : 053-112333",
      "โทรสาร : 053-112677 ต่อ 319 : กลุ่มส่งเสริมการศึกษาทางไกล เทคโนโลยีสารสนเทศและการสื่อสาร",
      "ict@chiangmaiarea1.go.th",
      ""
    ]
  }
  ]

    response = requests.get(get_other_api_url)

    assert response.status_code == 200 # status ที่ได้รับมาถูกต้องไหม
    assert isinstance(response.json(), list)
    assert len(response.json()) >= len(expected_data) # ตรวจสอบว่าค่า response ไม่่ต่ำกว่า ค่าจาก expected_data

if __name__ == '__main__':
    pytest.main()
