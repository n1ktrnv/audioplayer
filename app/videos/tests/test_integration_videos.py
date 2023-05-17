import time
import unittest
import requests


class TestAudioStreaming(unittest.TestCase):
    def test_audio_streaming(self):
        # Определение тестовых данных
        video_id = "test_video"
        headers = {'Range': 'bytes=0-1023'}
        filesize = 2048

        # Отправка запроса к API
        response = requests.get(f'http://app:80/videos/{video_id}', headers=headers)

        # Проверка статусного кода ответа
        self.assertEqual(response.status_code, 206)

        # Проверка заголовков ответа
        self.assertEqual(response.headers['Content-Range'], f'bytes 0-1023/{filesize}')
        self.assertEqual(response.headers['Accept-Ranges'], 'bytes')

        # Проверка типа содержимого ответа
        self.assertEqual(response.headers['Content-Type'], 'audio/mp4')

        # Проверка данных ответа
        self.assertGreater(len(response.content), 0)


if __name__ == "__main__":
    unittest.main()