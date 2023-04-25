import unittest
import requests

class TestAPI(unittest.TestCase): # Test Case
    """
    Test cases for the FindVideo API endpoint.
    """

    def test_get_FindVideo(self):
        """
        Test that the FindVideo API endpoint returns the expected data.
        """

        expected_data = [
            {
                "id": 1,
                "url": "https://www.youtube.com/watch?v=UNeJYRU16Mo&t=64s"
            },  
        ]

        response = requests.get("https://www.chiangmaiarea1.go.th/myapp/public/index.php/admin/api/FindVideo")

        self.assertEqual(response.status_code, 200) # status ที่ได้รับมาถูกต้องไหม
        self.assertIsInstance(response.json(), list)
        self.assertGreaterEqual(len(response.json()), len(expected_data)) # ตรวจสอบว่าค่า response ไม่่ต่ำกว่า ค่าจาก expected_data

if __name__ == '__main__': # เปิดการทำงาน
    unittest.main()
